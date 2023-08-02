

from image import Image
import numpy as np

def adjust_brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    x_pixels, y_pixels , num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    # for x in x_pixels:
    #     for y in y_pixels:
    #         for nc in num_channels:
    #             new_img.array[x,y,nc] = new_img.array[x,y,nc]*factor 
    # return new_img
    
    # vectorized version
    new_img.array = image.array *factor
    
    return new_img

def adjust_contrast(image, factor, mid):
    x_pixels, y_pixels , num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    new_img.array = (image.array - mid)*factor +mid
    return new_img

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels , num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    neighbor_range = kernel_size//2

    for x in x_pixels:
        for y in y_pixels:
            for nc in num_channels:
                total = 0                
                for x_neighbor in range (max(0, x-neighbor_range), min(x_pixels-1,x+neighbor_range)+1):
                    for y_neighbor in range (max(0, y-neighbor_range), min(y_pixels-1,y+neighbor_range)+1):
                        total += image.array[x_neighbor, y_neighbor, nc]
                new_img.array[x,y,nc] = total / (kernel_size**2)

    return new_img

def apply_kernel(image, kernel):
    # the kernel should be a numpy 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels , num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    kernel_size = kernel.shape[0]
    neighbor_range = kernel_size//2

    for x in x_pixels:
        for y in y_pixels:
            for nc in num_channels:
                total = 0
                for x_neighbor in range (max(0, x-neighbor_range), min(x_pixels-1,x+neighbor_range)+1):
                    for y_neighbor in range (max(0, y-neighbor_range), min(y_pixels-1,y+neighbor_range)+1):
                        x_kernel = x_neighbor + neighbor_range - x
                        y_kernel = y_neighbor + neighbor_range - y
                        kernel_val = kernel[x_kernel, y_kernel]
                        total += new_img.array[x,y,nc] *kernel_val
                new_img.array[x,y,nc] =total
    return new_img

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    x_pixels, y_pixels , num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    for x in x_pixels:
        for y in y_pixels:
            for nc in num_channels:
                new_img.array[x,y,nc]= (image1.array[x,y,nc]**2 + image2.array[x,y,nc]**2)**0.5
    return new_img
    
if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # brightening
    brightened_im = adjust_brighten(lake, 1.7)
    brightened_im.write_image('brightened.png')

    # darkening
    darkened_im = adjust_brighten(lake, 0.3)
    darkened_im.write_image('darkened.png')

    # increase contrast
    incr_contrast = adjust_contrast(lake, 2, 0.5)
    incr_contrast.write_image('increased_contrast.png')

    # decrease contrast
    decr_contrast = adjust_contrast(lake, 0.5, 0.5)
    decr_contrast.write_image('decreased_contrast.png')

    # blur using kernel 3
    blur_3 = blur(city, 3)
    blur_3.write_image('blur_k3.png')

    # blur using kernel size of 15
    blur_15 = blur(city, 15)
    blur_15.write_image('blur_k15.png')

    # let's apply a sobel edge detection kernel on the x and y axis
    sobel_x = apply_kernel(city, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
    sobel_x.write_image('edge_x.png')
    sobel_y = apply_kernel(city, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
    sobel_y.write_image('edge_y.png')

    # let's combine these and make an edge detector!
    sobel_xy = combine_images(sobel_x, sobel_y)
    sobel_xy.write_image('edge_xy.png')
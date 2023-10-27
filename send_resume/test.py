import requests

# Replace these values with your actual data
api_url = 'https://recruit.servicerocket.io/resumes'

pdf_file_path = r'C:\Users\Eidniuet\OneDrive\Desktop\Hong\Job\Resume.pdf'

# Additional data fields
data = {
    'name': 'Tong Weng Hong',
    'email': 'wenghongtong27@gmail.com',
    'about': 'A fresh graduate mechanical engineering but highly motivated job applicant with a strong background in software development.',
}

try:
    with open(pdf_file_path, 'rb') as pdf_file:
        files = {
            'file': ('resume.pdf', pdf_file, 'application/pdf'),
        }

        response = requests.post(api_url, data=data, files=files,)

        # Check the response
        if response.status_code == 200:
            print('Resume uploaded successfully.')
        else:
            print(f'Failed to upload resume. Status code: {response.status_code}')
except FileNotFoundError:
    print(f'PDF file not found at {pdf_file_path}')
except Exception as e:
    print(f'An error occurred: {str(e)}')

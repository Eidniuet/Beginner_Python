import requests

# Define the URL of the API endpoint
url = 'https://recruit.servicerocket.io/resume'

# Define the data you want to send in the request
data = {
    'name': 'Tong Weng Hong',
    'email': 'wenghongtong27@gmail.com',
    'about': 'A fresh graduate from mechanical engineering but highly motivated individual with a passion for technology.',
}

# Load the PDF file as an attachment
files = {'file': ('Resume.pdf', open('Resume.pdf', 'rb'))}

# Send the POST request
response = requests.post(url, data=data, files=files)

# Check the response
if response.status_code == 200:
    print('POST request was successful!')
else:
    print('POST request failed with status code:', response.status_code)

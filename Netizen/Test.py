import requests
import base64

name = "Tong Weng Hong"
email = "wenghongtong27@gmail"
resume_pdf_path = r"C:\Users\Eidniuet\OneDrive\Desktop\Hong\Job\Resume.pdf"

with open(resume_pdf_path, "rb") as file:
    resume_pdf_base64 = base64.b64encode(file.read()).decode("utf-8")


data = {
    "name": name,
    "email": email,
    "file": resume_pdf_base64
}


url = "https://career.netizenexperience.com/api/resume"

try:
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Resume submitted successfully!")
    else:
        print(f"Failed to submit the resume. Status code: {response.status_code}")
        print(response.json())  

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
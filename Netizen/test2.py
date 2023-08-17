import requests
import base64

resume_pdf_path = r"C:\Users\Eidniuet\OneDrive\Desktop\Hong\Job\Resume.pdf"
with open(resume_pdf_path, "rb") as file:
    resume_pdf_base64 = base64.b64encode(file.read()).decode("utf-8")

r = requests.post('https://career.netizenexperience.com/api/resume', json={
  "name": "Tong Weng Hong",
  "email": "wenghongtong27@gmail.com",
  "file": resume_pdf_base64,
  
})
print(f"Status Code: {r.status_code}, Response: {r.json()}")
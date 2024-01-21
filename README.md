# PythonEmailService
Microservice in Python to send email via SMTP using Flask with Health Check end point


git clone git@github.com:ThomasJay/PythonEmailService.git

cd PythonEmailService

python3 -m venv venv

Install all Libs

pip3 install -r requirements.txt


source venv/bin/activate


python3 email_service.py

curl -X GET http://localhost:8085/api/v1/health

curl -X POST http://localhost:8085/api/v1/send \\n   -H 'Content-Type: application/json' \\n   -d '{"email" : "thomasjay200@gmail.com", "subject" : "Hi there you", "message" : "This message is sent from Python3"}'\n


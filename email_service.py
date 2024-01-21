from flask import Flask, request, jsonify
import smtplib, ssl
import os

from dotenv import load_dotenv

load_dotenv()


port = os.getenv("port") or 466
smtp_server = os.getenv("smtp_server")
sender_email = os.getenv("sender_email")
password = os.getenv("password")

print("Port=", port)


def send_email(receiver_email, subject, message):
    message = f"Subject: {subject}\n\n{message}"

    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email Queued")


app = Flask(__name__)

api_v1_prefix = "/api/v1/"


@app.route("/", methods=["GET"])
def get_home():
    return "Email Microservice"


@app.route(api_v1_prefix + "/health", methods=["GET"])
def get_health():
    healthy_status = {"status": "Healthy"}
    return jsonify(healthy_status), 200, {"Content-Type": "application/json"}


@app.route(api_v1_prefix + "/send", methods=["POST"])
def post_send_email():
    post_data = request.json

    # {
    #    "email" : "thomasjay200@gmail.com",
    #    "subject" : Hi there",
    #    "message" : "This message is sent from Python3"
    # }

    send_email(
        post_data.get("email"), post_data.get("subject"), post_data.get("message")
    )

    result = {"status": "Queued"}

    return jsonify(result), 201, {"Content-Type": "application/json"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8085)  # Auto reload

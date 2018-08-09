from flask import Flask, request
import os
import requests

GATEWAY_EMAIL = os.environ.get('GATEWAY_EMAIL')
FROM_EMAIL = os.environ.get('FROM_EMAIL')
API_KEY = os.environ.get('API_KEY')
app = Flask(__name__)


def build_payload(to_email, subject, body, is_html=False):
    content_type = 'text/html' if is_html else 'text/plain'
    return {
        "personalizations": [
            {
                "to": [
                    {
                        "email": to_email
                    }
                ]
            }
        ],
        "from": {
            "email": FROM_EMAIL
        },
        "subject": subject,
        "content": [
            {
                "type": content_type,
                "value": body
            }
        ]
    }


@app.route("/")
def send_email():
    to_email = request.args.get('to', GATEWAY_EMAIL)
    subject = request.args.get('title', 'esender')
    body = request.args.get('body', '_')
    is_html = request.args.get('html', False)
    data = build_payload(to_email, subject, body, is_html)
    return requests.post('https://api.sendgrid.com/v3/mail/send', headers={'Authorization': 'Bearer ' + API_KEY}, json=data).text


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)

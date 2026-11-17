import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_email(subject: str, body: str) -> None:
    sender = os.environ["GMAIL_ADDRESS"]
    password = os.environ["GMAIL_APP_PASSWORD"]

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = sender
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

def format_events(events) -> str:
    lines = []
    for e in events:
        title = f" ({e.title})" if e.title else ""
        lines.append(
            f"- {e.artist}{title}: {e.date or 'date unknown'} | {e.city or '?'} | {e.venue or '?'}"
        )
    return "\n".join(lines)

if __name__ == "__main__":
    send_email("Test from job-agent", "If you read this, email works.")
    print("Sent")
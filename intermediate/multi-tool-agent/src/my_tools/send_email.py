import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config
from agents import function_tool


SMTP_USER = config("SMTP_USER")
SMTP_PASSWORD = config("SMTP_PASSWORD")


@function_tool
def send_email(to_email: str, subject: str, body: str) -> dict:
    """
    Sends an email using SMTP
    """
    try:
        msg = MIMEMultipart()

        msg['From'] = SMTP_USER
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # connect to SMTP server and send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)

        print("Email sending tool fired ---->")
        return {
          "status": "success",
          "tool": "send_email",
          "to_email": to_email,
          "subject": subject,
          "message": f"Email sent successfully"
      }
        

    except Exception as e:
      return {
        "status": "error",
        "tool": "send_email",
        "to_email": to_email,
        "subject": subject,
        "body": body,
        "message": str(e)
     }

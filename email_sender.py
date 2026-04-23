import smtplib
from email.mime.text import MIMEText
import os
import datetime

def send_email(subject, body, to, login, app_password):
    smtp_server = "smtp.gmail.com"
    port = 465
    message = MIMEText(body, "html", "utf-8")
    message["Subject"] = subject
    message["From"] = login
    message["To"] = to

    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(login, app_password)
    server.sendmail(login, [to], message.as_string())
    server.quit()

if __name__ == '__main__':
    with open(f"daily_news_{datetime.datetime.now().strftime('%Y-%m-%d')}.html", encoding="utf-8") as f:
        body = f.read()
    send_email(
        subject="今日全球重要新闻日报",
        body=body,
        to=os.environ["EMAIL_TO"],
        login=os.environ["EMAIL_USER"],
        app_password=os.environ["EMAIL_PASS"]
    )

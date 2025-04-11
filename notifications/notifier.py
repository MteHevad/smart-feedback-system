import yagmail

def send_notification(subject, body, to):
    yag = yagmail.SMTP("your.email@example.com", "yourpassword")
    yag.send(to=to, subject=subject, contents=body)

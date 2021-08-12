import smtplib ,ssl


def send_email(message):
    port = 465 #For SSL
    smtp_server = ""
    sender_email = ""
    receiver_email = ""
    password = ""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server ,port , context=context) as server:
        try:
            server.login(sender_email ,password)
            res = server.sendmail(sender_email ,receiver_email ,message)
            print("email sent!!")
        except:
            print("Could not login or Receiver address not found")
send_email("This is an email sent")
def sendMail(mail, to):
    SERVER = "smtp.office365.com"

    FROM = "<Your email>"

    SUBJECT = mail[0]
    TEXT = mail[1]

    message = '\r\n'.join(['To: %s' % to,
                        'From: %s' % FROM,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    print(message)

    import smtplib

    server = smtplib.SMTP(SERVER, 587)
    server.connect(SERVER, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("<Your email login>", "<Email password>") # email credentials
    server.sendmail(FROM, to, message)
    server.quit()













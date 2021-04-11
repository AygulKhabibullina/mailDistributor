def readMail():

    import imaplib
    import email
    import base64
    email_user = input('Email: ')
    email_pass = input('Password: ')

    M = imaplib.IMAP4_SSL('outlook.office365.com', 993)
    M.login(email_user, email_pass)
    M.select()

    typ, message_numbers = M.search(None, '(UNSEEN)')
    mail = []
    for num in message_numbers[0].split():
        typ, data = M.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        typ, data = M.store(num, '-FLAGS', '\\Seen')
        print(msg)
        myString = msg.as_string()
        subject = myString[myString.find('Subject: ')+9:myString.find('\nTo:')]
        message = myString[
                  myString.find('Content-Type: text/plain; charset="UTF-8"\n')+43
                  :myString.find('\nContent-Type: text/html; charset="UTF-8"')]
        message = message[0:message.find('\n--')]
        mail = [subject, message]
    M.close()
    M.logout()
    return mail

















from ReadMail import readMail
from SendMail import sendMail


dictionary = {
    "developer": ["bug", "feature", "doesn't", "crashed"],
    "analytic": ["customer", "research", "analyze"],
    "tester": ["test", "UI", "UX", "integration test"]
}

# readSend = sendMail(readMail())

read = readMail()
to = ''
if any(word in read[1].lower() for word in dictionary["developer"]):
    to = "developer@test.ru"
elif any(word in read[1].lower() for word in dictionary["analytic"]):
    to = "analytic@test.ru"
elif any(word in read[1].lower() for word in dictionary["tester"]):
    to = "tester@test.ru"
else:
    to = "general@test.ru"

readSend = sendMail(read, to)

















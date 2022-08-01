# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import imaplib
from datetime import date

import post_notif
import email
def handler(name):
    # Use a breakpoint in the code line below to debug your script.
    server = "imap.world4you.com"
    email_address = 'jevnishioka1@gmail.com'
    password = 'zqssjnjfcxtgtmjk'
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(email_address, password)
    imap.select("Inbox")
    today = date.today()
    typ, data = imap.search(None,'(FROM "cicconem01@gmail.com")')
    for msg in data[0].split():
        _, msgs = imap.fetch(msg,"(RFC822)")
        message = email.message_from_bytes(msgs[0][1])
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            print(part.as_string())
    imap.close()

    print(message)
    print("works")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    handler('Guy')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

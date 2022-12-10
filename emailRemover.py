import imaplib
import email

# Connect to the Gmail server
imap_host = 'imap.gmail.com'
imap_user = 'your_gmail_username'
imap_pass = 'your_gmail_password'

imap = imaplib.IMAP4_SSL(imap_host)
imap.login(imap_user, imap_pass)

# Select the inbox folder
imap.select('inbox')

# Search for all messages that match the given criteria
status, messages = imap.search(None, '(SUBJECT "promotion")')
message_ids = messages[0].split()

# Loop through the matching messages and delete them
for message_id in message_ids:
    status, message = imap.fetch(message_id, '(RFC822)')
    email_message = email.message_from_bytes(message[0][1])

    # Check the subject of the email to confirm it's a promotional message
    if email_message['Subject'].lower().startswith('promotion'):
        imap.store(message_id, '+FLAGS', '\\Deleted')

# Close the connection to the Gmail server
imap.close()
imap.logout()

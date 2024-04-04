import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

senderEmail = os.environ.get('SENDER_EMAIL', 'NoEmailFound')
receiverNumber1 = os.environ.get('RECEIVER_NUMBER1', 'NoNumberFound')
receiverNumber2 = os.environ.get('RECEIVER_NUMBER2', 'NoNumberFound')
# If adding more numbers to the list, don't forget to add them to the array below, the .env, and the script####.yml files
receiverNumbers = [receiverNumber1, receiverNumber2]
appKey = os.environ.get('APP_KEY', 'NoKeyFound')

# Sends texts using the email as the sender to the number(s) given, both provided in the .env file
def sendText(numberToText):
    # Composing the email/text
    message = EmailMessage()
    message.set_content("\nNeato runs at noon!")
    message['From'] = senderEmail
    message['To'] = numberToText
    
    # Don't touch, server stuff
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, appKey)
    server.send_message(message)
    server.quit()
    
    print("Texting:", numberToText)

# Main function
def main():
    # Excludes numbers which hold default value (NoNumberFound)
    validNumbers = [number for number in receiverNumbers if number != 'NoNumberFound']
    for number in validNumbers:
        sendText(number) 
                   
if __name__ == "__main__":
    main()  
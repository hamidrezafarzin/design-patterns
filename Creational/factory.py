class Message:
    def send(self): 
        pass

class EmailMessage(Message):
    def send(self):
        print("Send Email")

class SMSMessage(Message):
    def send(self):
        print("Send SMS")

class MessageCreator:
    def create_message(self): 
        pass

    def send_message(self):
        message = self.create_message()
        message.send()

class EmailMessageCreator(MessageCreator):
    def create_message(self):
        return EmailMessage()

class SMSMessageCreator(MessageCreator):
    def create_message(self):
        return SMSMessage()


email_creator = EmailMessageCreator()
email_creator.send_message()

sms_creator = SMSMessageCreator()
sms_creator.send_message()

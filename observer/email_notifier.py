from base import Observer
from email_service import EmailService

class EmailObserver(Observer):
    
    def notify(self):
        email = EmailService.send_email()
        
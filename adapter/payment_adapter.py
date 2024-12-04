from stripe_payment import StripePayment
from payment_processor import PaymentProcessor


class PaymentAdapter:
    
    def __init__(self, processor: StripePayment):
        self.processor = processor
    
    def process_payment(self):
        self.processor.make_payment()
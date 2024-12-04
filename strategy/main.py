from payment_processor import PaymentProcessor
from base import PaymentStrategy
from payment import CreditCardPayment, RazorpayPayment


def main():
    
    p = PaymentProcessor(CreditCardPayment())
    
    p.process_payment()
    

if __name__ == "__main__":
    main()
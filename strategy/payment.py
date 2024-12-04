from base import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    
    def pay(self):
        print("Paying using credit card...")

class RazorpayPayment(PaymentStrategy):
    
    def pay(self):
        print("Paying using razorpay...")
        

from base import PaymentStrategy


class PaymentProcessor:
    
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def process_payment(self):
        self.strategy.pay()
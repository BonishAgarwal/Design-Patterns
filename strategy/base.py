from abc import ABC, abstractmethod

# Strategy design pattern is used when we know that the behavior might change at run-time and we don't want to change the existing client code
class PaymentStrategy(ABC):
    
    @abstractmethod
    def pay(self):
        pass
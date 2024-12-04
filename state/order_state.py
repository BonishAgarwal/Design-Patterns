from abc import ABC, abstractmethod


class OrderState(ABC):
    
    @abstractmethod
    def proceed(self):
        pass
    
    @abstractmethod
    def cancel(self):
        pass
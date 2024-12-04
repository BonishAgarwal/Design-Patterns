from order_state import OrderState
from shipped import ShippedState


class PlacedState(OrderState):
    
    def proceed(self, order):
        print("Order has been shipped")
        order.state = ShippedState()
    
    def cancel(self, order):
        print("Order has been cancelled")
        order.state = None
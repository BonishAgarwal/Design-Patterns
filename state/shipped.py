from order_state import OrderState
from delivered import DeliveredState


class ShippedState(OrderState):
    
    def proceed(self, order):
        print("Order is out for delivery")
        order.state = DeliveredState()
    
    def cancel(self, order):
        print("Order cannot be canceeled. Already shipped!!")
        order.state = None
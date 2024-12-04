from order_state import OrderState


class DeliveredState(OrderState):
    
    def proceed(self, order):
        print("Order delivered")
    
    def cancel(self, order):
        print("Order cannot be cancelled. It has already been delivered!!")
    

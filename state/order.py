from placed import PlacedState


class Order:
    
    def __init__(self):
        self.state = PlacedState()
        
    def proceed(self):
        if self.state:
            self.state.proceed(self)
        
        else:
            print("Order is not active")
        
    def cancel(self):
        if self.state:
            self.state.cancel(self)
        else:
            print("Order is not active.")
    

order = Order()
# Initial state: Placed
order.proceed()  # Proceed to Paid
order.cancel()   # Cannot cancel in Paid state
order.proceed()  # Proceed to Shipped
order.cancel()   # Cannot cancel in Shipped state
order.proceed()  # Proceed to Delivered
order.proceed()  # Already delivered
order.cancel()   # Cannot cancel delivered order

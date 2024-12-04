class Singelton:
    _instance = None
    
    def __new__(cls):
        # If _instance is None, create the instance
        if cls._instance is None:
            cls._instance = super(Singelton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize the instance with any necessary attributes
        self.value = 42  # Example attribute
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

singelton1 = Singelton()
singelton2 = Singelton()

print(singelton1)
print(singelton2)

    
from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"
    
    def add_item(self, name,quantity,price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
class Authoizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class AuthoizerSMS(Authoizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self,code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
    
class AuthoizerRobot(Authoizer):

    def __init__(self) -> None:
        super().__init__()
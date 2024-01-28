from abc import ABC, abstractmethod

# Order Class:
# Represents an order with items, quantities, prices, and a status.
# __init__ method initializes the order with empty lists for items, quantities, and prices, and sets the status to "open."
# add_item method adds an item to the order with a specified quantity and price.
# total_price method calculates and returns the total price of the items in the order.

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

# Authoizer Abstract Class:
# An abstract class representing an authorizer with one abstract method is_authorized.
    
class Authoizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

#AuthoizerSMS Class:
# A concrete class that extends Authoizer.
# Implements the is_authorized method by checking if a code has been verified.

class AuthoizerSMS(Authoizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self,code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

# AuthoizerRobot Class:
# Another concrete class that extends Authoizer.
# Implements the is_authorized method by setting authorization to true when it's not a robot.
    
class AuthoizerRobot(Authoizer):

    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

# PaymentProcessor Abstract Class:
# An abstract class representing a payment processor with one abstract method pay.
    
class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

# DebitPaymentProcessor Class:
# A concrete class that extends PaymentProcessor.
# Requires a security code and an Authoizer object during initialization.
# Implements the pay method, which processes the payment if the authorizer is authorized.

class DebitPaymentProcessorr(PaymentProcessor):

    def __init__(self, security_code, authoizer: Authoizer):
        self.security_code = security_code
        self.authoizer = authoizer

    def pay(self, order):
        if not self.authoizer.is_authorized():
            raise Exception('Not authorized')
        print("Processing debit payment type")
        print(f'Verifying security code: {self.security_code}')
        order.status = "paid"

# CreditPaymentProcessor Class:
# A concrete class that extends PaymentProcessor.
# Requires a security code during initialization.
# Implements the pay method, which processes the credit card payment.
# python
class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'

# PaypalPaymentProcessor Class:
# A concrete class that extends PaymentProcessor.
# Requires an email address and an Authoizer object during initialization.
# Implements the pay method, which processes the PayPal payment if the authorizer is authorized.
        
class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authoizer: Authoizer):
        self.email_address = email_address
        self.authoizer = authoizer

    def pay(self, order):
        if not self.authoizer.is_authorized():
            raise Exception('Not authorized')
        print("Processing paypal payment type")
        print(f'Using email address: {self.email_address}')
        order.status = 'paid'

# Example Usage:
# An order is created and items are added to it.
# The total price of the order is calculated and printed.
# An instance of AuthoizerRobot is created, and the not_a_robot method is called to authorize the robot.
# A PaypalPaymentProcessor is created with an email address and the AuthoizerRobot.
# The pay method of the processor is called, which will print a message if the authorization is successful.

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

# Create an instance of AuthoizerRobot
print(order.total_price())
auth = AuthoizerRobot()
auth.not_a_robot()

# Use the instance when creating the PaypalPaymentProcessor
processor = PaypalPaymentProcessor("hi@pypi.com", auth)
processor.pay(order)

# This code demonstrates a basic structure for processing orders and handling payments with different payment processors and authorization mechanisms.
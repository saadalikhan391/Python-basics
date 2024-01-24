#payment info

class Payslips:
    def __init__(self,name,payment,amount):
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + "is paid " + str(self.amount)
        else:
            return self.name + "is not paid yet"
    
khan = Payslips("khan ", "no", 1000)
saad = Payslips("saad ", "no", 3000)

print(khan.status(),"\n",saad.status())

khan.pay()
print("After payment")
print(khan.status(),"\n",saad.status())
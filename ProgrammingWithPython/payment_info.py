class paySlip:
    def __init__(self, name ,payment , amount) -> None:
        self.name = name
        self.payment = payment
        self.amount =amount

    def pay(self):
        self.payment == "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + "is pay" +" "+ str(self.amount)
        else:
            return self.name + 'not pay ' +  str(self.amount)

saqlain = paySlip("saqlain " , 'yes' , '300' )

print(saqlain.status())
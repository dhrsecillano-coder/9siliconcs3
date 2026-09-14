class Brand:

    def __init__(self, Name, Founder, Contact_No):
        self.Name = Name
        self.Founder = Founder
        self.__Contact_No = Contact_No
        self.basketballs = []

    def read_Name(self):
        return self.Name

    def read_Founder(self):
        return self.Founder

    def read_Contact_No(self):
        return self.__Contact_No

    def update_info(self, Name, Founder, Contact_No):
        self.Name = Name
        self.Founder = Founder
        self.__Contact_No = Contact_No


class Basketball:

    def __init__(self, Brand, Size, Serial_Number):
        self.Brand = Brand
        self.Size = Size
        self.__Serial_Number = Serial_Number

    def read_Serial_Number(self):
        return self.__Serial_Number

brand1 = Brand("Nike", "Phil Knight", "123-456-7890")

ball1 = Basketball("Nike", 7, "NIK323")
ball2 = Basketball("Nike", 6, "NIK143")

print("BEFORE RELATIONSHIP")

print(f"Brand: {brand1.Name}, {brand1.Founder}, {brand1.read_Contact_No()}")

print(f"Basketball 1: {ball1.Brand}, {ball1.Size}, {ball1.read_Serial_Number()}")
print(f"Basketball 2: {ball2.Brand}, {ball2.Size}, {ball2.read_Serial_Number()}")

print("BUILDING RELATIONSHIP")

brand1.basketballs.append(ball1)
brand1.basketballs.append(ball2)

print("AFTER RELATIONSHIP")
print(f"Brand: {brand1.Name}")

print("Related object(s)")

for item in brand1.basketballs:
    print("Brand:", item.Brand)
    print("Size:", item.Size)
    print("Serial No.:", item.read_Serial_Number())
    print()

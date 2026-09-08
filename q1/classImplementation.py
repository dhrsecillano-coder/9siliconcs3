class Basketball:
    def __init__(self, Brand, Size, Serial_Number):
        self.Brand = Brand
        self.Size = Size
        self.__Serial_Number = Serial_Number

    def change_size(self, new_size):
        self.Size = new_size

    def read_Brand(self):
        return self.Brand

    def read_Serial_Number(self):
        return self.__Serial_Number

ball1 = Basketball("Molten", 7, 1234)
ball2 = Basketball("Wilson", 6, 43542)

print("BEFORE")
print(f"Basketball 1: {ball1.Brand}, {ball1.Size}, {ball1.read_Serial_Number()}")
print(f"Basketball 2: {ball2.Brand}, {ball2.Size}, {ball2.read_Serial_Number()}")

ball1.change_size(5)
print("Changing the ball size of Basketball 1 from 7 to 5.")

print("AFTER")
print(f"Basketball 1: {ball1.Brand}, {ball1.Size}, {ball1.read_Serial_Number()}")
print(f"Basketball 2: {ball2.Brand}, {ball2.Size}, {ball2.read_Serial_Number()}")
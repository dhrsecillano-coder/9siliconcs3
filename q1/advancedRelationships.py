class Sports:
    def __init__(self, name, players, equipments, venue):
        self.name = name
        self.players = players
        self.equipments = equipments
        self.venue = venue

    def read_info(self):
        print(f"Sport: {self.name}, Players: {self.players}, Equipment: {self.equipments}, Venue: {self.venue}")

class Basketball(Sports):
    def __init__(self, name, player, equipments, venue, brand, size, weight, serial_number):
        super().__init__(name, player, equipments, venue)
        self.brand = brand
        self.size = size
        self.weight = weight
        self.__serial_number = serial_number

    def display_brand(self):
        print(f"Brand: {self.brand}")

    def change_size(self, new_size):
        self.size = new_size

    def add_brand(self, new_brand):
        self.brand = new_brand
    
class Game:
    def __init__(self, name, platform):
        self.name = name
        self.platform = platform

    def read_info(self):
        print(f"Game: {self.name} on {self.platform}")

class Brand:
    def __init__(self, name, founder, contact_No):
        self.name = name
        self.founder = founder
        self.__contact_No = contact_No

    def display_name(self):
        print(f"Brand Name: {self.name}")

    def display_founder(self):
        print(f"Founder: {self.founder}")

    def update_info(self, name, founder):
        self.name = name
        self.founder = founder

print("Test 1")
bball = Basketball("Basketball", 5, "Ball, Hoop", "Court", "Nike", 7, 0.62, "SN-98234")
bball.read_info()
bball.display_brand()

game = Game("NBA 2K24", "PlayStation 5")
brand = Brand("Nike", "Phil Knight", "+1-800-806-6453")

print("Test 2")
game.read_info()
brand.display_name()
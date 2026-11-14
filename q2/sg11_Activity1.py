class Patient:
    def __init__(self, name, bill_amount, patient_type):
        self.name = name
        self.bill_amount = bill_amount
        self.patient_type = patient_type

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient.")

class SeniorCitizen(Patient):

    def calculate_bill(self):
        discount = self.bill_amount * 0.2
        return self.bill_amount - discount

    def display_patient_type(self):
        print("Patient Type: Senior Citizen.")

class PhilHealth(Patient):

    def calculate_bill(self):
        discount = self.bill_amount * 0.15
        return self.bill_amount - discount

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member.")


Patient1 = Patient("Juan Dela Cruz", 15000, "Regular Patient")
Patient2 = SeniorCitizen("Maria Santos", 15000, "Senior Citizen")
Patient3 = PhilHealth("Pedro Reyes", 15000, "PhilHealth Member")

print("Hospital Billing System")
print("------------------------")

print("Patient Name:", Patient1.get_name())
print("Patient Type: Regular Patient")
print("Original Bill: ₱", Patient1.get_bill_amount())
print ("Final Bill: ₱", Patient1.calculate_bill())

print("Patient Name:", Patient2.get_name())
print("Patient Type: Senior Citizen")
print("Original Bill: ₱", Patient2.get_bill_amount())
print("Final Bill: ₱", Patient2.calculate_bill())

print("Patient Name:", Patient3.get_name())
print("Patient Type: PhilHealth Member")
print("Original Bill: ₱", Patient3.get_bill_amount())
print("Final Bill: ₱", Patient3.calculate_bill())

class Bankaccount:
    def __init__(self, account_number, Balance):
        self.__account_number = account_number
        self.__Balance = Balance

    @property
    def get_account_number(self):
            return f"{self.__account_number}"

    @property
    def get_Balance(self):
         return f"{self.__Balance}"

    def Set_Balance(self, Balance):
        if Balance > 0:
            self.__Balance = Balance
        else:
            print("The balance must not be a negative number.")

    def Set_account_number(self, account_number):
        self.__account_number = account_number
        
a1 = Bankaccount(12345, 1000)
print("Account 1")
print(f"Account Number: {a1.get_account_number}")
print(f"Balance: {a1.get_Balance}")

a1.Set_Balance(-2032)
print("Update balance to -2032")
print("The balance must be a negative number.")
print(f"Account Number: {a1.get_account_number}")
print(f"Balance: {a1.get_Balance}")

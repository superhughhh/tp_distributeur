### A finir : menu technicien

class Machine():
    can_price = 1.5
    code_identification = "iamtechnician"
    identification_state = False

    def __init__(self, can_number=100, currency_machine=11.5):
        self.can_number = can_number
        self.currency_machine = currency_machine

    def __repr__(self) -> str:
        return f"{self.can_number},{self.currency_machine}"


    ##### User possibility
    def sell_can(self):
        currency_user = float(input("Please, insert coins"))
        currency_returned = 0
        if self.can_number < 1:
            print("Sorry, The automatic distributor is empty !")
            return None
        if currency_user > self.can_price or currency_user == self.can_price:
            self.currency_machine += self.can_price
            self.can_number -= 1
            currency_returned = currency_user - self.can_price
            if currency_returned == 0:
                print("Thank you for your purchase, take you drink please.")
                return None
            print("Thank you for your purchase, take you drink please.")
            print(f"get your money please -- ${currency_returned}")
            return None
        else:
            missing_currency = self.can_price - currency_user
            print(f"Sorry, you don't have introduce money enough, add another $ {missing_currency} ")
            return None


    ##### Technician identification
    def indentification(self):
        my_password = input("Please, Enter the identication code\n")
        if my_password == self.code_identification:
            self.identification_state = True
            return None
        else:
            print("Incorrect Password")
            return None


    def display_stock_and_money(self):
        print('#####')
        print(f"{self.can_number} cans left in the ditributor")
        print(f"cash available : ${self.currency_machine}")
        print('#####')
        print()
        return None


    def add_cans(self):
        cans_to_add = int(input("How many cans do you want to add"))
        self.can_number += cans_to_add
        print(f"you add {cans_to_add} cans, the machine contains {self.can_number} cans now")
        print()
        return None


    def withdrew_cash(self):
        if self.currency_machine > 11.5:
            money_withdrawn = self.currency_machine - 11.5
            self.currency_machine = 11.5
            print(f"you withdrew ${money_withdrawn}")
            print()
            return None
        else:
            print("Amount of cash in the machine insufficient to withdrawn")
            print()
            return None

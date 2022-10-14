
from machine_function import Machine
from pick import pick
from time import sleep

class Interface():

    def __init__(self) -> None:
        pass


    def main_menu(self, Machine):
        title = 'Welcome, What do you want: '
        options = ['Buy a can', 'Make a technician operation', 'Nothing']
        option, index = pick(options, title)
        print(f"You choose : {option}")
        if index == 0:
            Machine.sell_can()
            sleep(5)
            self.main_menu(Machine)
        if index == 1:
            Machine.indentification()
            sleep(3)
            self.technician_menu(Machine)
        if index == 2:
            print("Goodbye")
            return None


    def technician_menu(self, Machine):
        title = 'Welcome Technician, What operation do you want to realize : '
        options = ['Consult Stock and $$$ Availabl', 'Add Can', 'Withdrew $$$', 'Return to Main menu']
        option, index = pick(options, title)
        print(f"You choose : {option}")
        if index == 0:
            Machine.display_stock_and_money()
            sleep(5)
            self.technician_menu(Machine)
        if index == 1:
            Machine.add_cans()
            sleep(5)
            self.technician_menu(Machine)
        if index == 2:
            Machine.withdrew_cash()
            sleep(5)
            self.technician_menu(Machine)
        if index == 3:
            self.main_menu(Machine)

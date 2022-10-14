
from csv import reader
from machine_function import Machine


class Data():

    def __init__(self) -> None:
        pass


    def upload_data(self, Machine):
        file = open("data.csv", "r")
        my_data = file.read()
        data_list = my_data.split(",")
        Machine.can_number = int(data_list[0])
        Machine.currency_machine = float(data_list[1])
        return None



    def save_data(self, Machine):
        my_data = Machine.__repr__()
        file = open("data.csv", "w")
        file.write(my_data)
        file.close
        return None

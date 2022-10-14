## A finir : l'app
## systeme d'enregristrement des données
## systeme de lecture des données


from machine_function import Machine
from data_management import Data
from my_interface import Interface


def App():
    distributor = Machine()
    data = Data()
    interface = Interface()
    data.upload_data(distributor)
    interface.main_menu(distributor)
    data.save_data(distributor)

App()


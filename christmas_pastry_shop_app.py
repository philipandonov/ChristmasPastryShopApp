from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        correct_delicacy = ['Gingerbread', 'Stolen']
        if any(d.name == name for d in self.delicacies):
            raise Exception(f"{name} already exists!")
        if type_delicacy not in correct_delicacy:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if type_delicacy == 'Gingerbread':
            delicacy = Gingerbread(name, price)
        else:
            delicacy = Stolen(name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        correct_booth = ['Open Booth', 'Private Booth']
        if any(b.booth_number == booth_number for b in self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in correct_booth:
            raise Exception(f"{type_booth} is not a valid booth!")
        if type_booth == 'Open Booth':
            booth = OpenBooth(booth_number, capacity)
        else:
            booth = PrivateBooth(booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and number_of_people <= booth.capacity:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if not any(b.booth_number == booth_number for b in self.booths):
            raise Exception(f"Could not find booth {booth_number}!")
        if not any(d.name == delicacy_name for d in self.delicacies):
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        for booth in self.booths:
            if booth_number == booth.booth_number:
                current_booth = booth
        for delicacy in self.delicacies:
            if delicacy_name == delicacy.name:
                current_delicacy = delicacy
        current_booth.delicacy_orders.append(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                current_booth = booth
        sum_delicacy = 0
        for delicacy in current_booth.delicacy_orders:
            sum_delicacy += delicacy.price
        bill = sum_delicacy + current_booth.price_for_reservation
        self.income += bill
        current_booth.delicacy_orders = []
        current_booth.is_reserved = False
        current_booth.price_for_reservation = 0
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

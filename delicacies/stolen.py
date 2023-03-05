from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name: str, price: float):
        super(Stolen, self).__init__(name,250, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
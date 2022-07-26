
class Product:
    def __init__(self, name, amount, cost):
        self.name = name
        self.amount = amount
        self.cost = cost

    def purchase(self):
        """
        Calculate and update user purchase
        :return:
        """
        self.amount -= 1


class User:
    def __init__(self, user, deposit, product_name):
        self.user = user
        self.deposit = deposit
        self.product_name = product_name
        self.change = 0

    def get_change(self, product_cost):
        """
        Get user change
        :param product_cost:
        :return:
        """
        self.change = self.deposit - product_cost
        return self.change

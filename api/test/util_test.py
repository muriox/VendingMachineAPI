import unittest
from api.util import test_products, create_product, validate_user_input, process_user_deposit
from api.model import *
from api.constants import INPUT_COIN_STRING_MSG

test_products_2 = create_product(Rice=Product("Rice", 10, 50),
                                 Bread=Product("Bread", 5, 10),
                                 Orange=Product("Coke", 33, 5))
# User
user_1 = User("0", 50, "Juice")
user_2 = User("1", 70, "Rice")


class TestCreateProduct(unittest.TestCase):

    def test_create_product(self):
        product = create_product(Rice=test_products["Rice"])

        self.assertEqual(product["Rice"].amount, test_products_2["Rice"].amount)
        self.assertNotEqual(product["Rice"].amount, test_products_2["Bread"].amount)


class TestValidateInput(unittest.TestCase):

    def test_validate_input(self):
        is_product_1 = validate_user_input(test_products, user_1.user)
        is_product_2 = validate_user_input(test_products, user_2.user)
        is_product_3 = validate_user_input(test_products, "d")

        self.assertFalse(is_product_1)
        self.assertTrue(is_product_2)
        self.assertFalse(is_product_3)


class TestProcessUserDeposit(unittest.TestCase):

    def test_process_user_deposit(self):
        product = test_products["Rice"]
        # Note: Using total of 70 coin deposit
        process_user = process_user_deposit(product, INPUT_COIN_STRING_MSG, "1")

        self.assertEqual(product.name, process_user.product_name)
        self.assertEqual(process_user.get_change(product.cost), 20)
        self.assertNotEqual(process_user.get_change(product.cost), 30)


if __name__ == '__main__':
    unittest.main()

import sys
from api.model import *
from api.constants import *


def create_product(**kwargs):
    """
    Create product
    :param kwargs:
    :return: product(s)
    """
    product = {}
    for key, value in kwargs.items():
        # print("key: {}, val: {}".format(key, value))
        product[key] = value

    return product


def get_dict_of_ordered_products(products_dict):
    """
    Get dictionary of ordered test_products
    :param products_dict:
    :return: product order and names
    """
    product_dict = {}
    count = 1
    for key, value in products_dict.items():
        product_dict[str(count)] = key
        count += 1

    return product_dict


def get_product_names(position_dict):
    """
    Get product names from get_dict_of_ordered_products function.
    :param position_dict:
    :return: String names
    """
    names = ""
    count = 1
    for key, value in position_dict.items():
        names = names + str("\t{} - {}\n").format(count, key)
        count += 1

    return names


def validate_user_input(products_available, user_input):
    """
    Validate user input
    :param products_available:
    :param user_input:
    :return: is_product - confirming if product exist or not
    """
    product_dict = get_dict_of_ordered_products(products_available)
    is_product = user_input in product_dict.keys()

    return is_product


def process_user_deposit(current_product, input_coin_message, user_count):
    """
    Process coins input
    :param current_product:
    :param input_coin_message:
    :param user_count:
    :return:
    """
    user_deposit = 0
    product_cost = int(current_product.cost)
    cost_remaining = product_cost - user_deposit
    print("\tProduct Cost: {}".format(product_cost))

    # while not cost_covered:
    while product_cost > user_deposit and cost_remaining != 0:
        try:
            coin_input = int(input(input_coin_message))

            # Calculate user deposit against cost of product
            if str(coin_input).isnumeric() and coin_input in ALLOWED_COINS:
                user_deposit = user_deposit + coin_input
                cost_remaining = product_cost - user_deposit

                print("\tYour deposits: ", user_deposit)
                print("\tProduct cost remaining: " + str(cost_remaining))

        except ValueError:
            print("\tInvalid Input. Only Integers and {} allowed.".format(ALLOWED_COINS))

    # Create user
    user = User(user_count, user_deposit, current_product.name)

    return user


def process_coin_input(validated_product, products, users, user_input, user_count):
    """

    :param validated_product:
    :param products:
    :param users:
    :param user_input:
    :param user_count:
    :return:
    """
    if validated_product:
        print("\n----- Input Coin Stage ------")
        # Get ordered test_products and names
        product_dict = get_dict_of_ordered_products(products)
        # Get product selected by user
        current_product = products[product_dict[user_input]]
        # Process user deposits and return user object. Object holds relevant data of user actions
        user = process_user_deposit(current_product, INPUT_COIN_STRING_MSG, user_count)

        # Update Product data
        current_product.purchase()
        products[product_dict[user_input]] = current_product
        # Add user transaction to users dictionary
        users[str(user_count)] = user
        # Get the updated product data purchased by user
        product_purchased = products[product_dict[user_input]]

        # Process user transaction report and change (if any)
        user_change = user.get_change(product_purchased.cost)
        display_result(product_purchased, user.deposit, user_change)

        # Order/Purchase completed
        user_input = input(LAST_INPUT_STRING_MSG)
    else:
        print("\nProduct selected doesn't exist")
        user_input = input(FIRST_INPUT_STRING_MSG)

        if user_input == "0":
            sys.exit()


def display_result(product_purchased, user_deposit, user_change):
    """

    :param product_purchased:
    :param user_deposit:
    :param user_change:
    :return:
    """

    print("\n------- Purchase Details ------- " + product_purchased.name)
    print("\tProduct Purchased: " + product_purchased.name)
    print("\tProduct cost: " + str(product_purchased.cost))
    print("\tProduct Left: " + str(product_purchased.amount))
    print("\tYour total deposit: " + str(user_deposit))
    print("\tYour change: " + str(user_change))


"""
 ---------- Products setup ------------
"""
# Create test_products
test_products = create_product(Rice=Product("Rice", 10, 50),
                               Beans=Product("Beans", 8, 30),
                               Coke=Product("Coke", 21, 70))
# Get product names
product_position_dict = get_dict_of_ordered_products(test_products)
product_names = get_product_names(test_products)


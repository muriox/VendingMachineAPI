import sys
from api.util import *

if __name__ == "__main__":
    print("Starting API...")
    users = {}
    user_count = 1

    # Get start up input
    user_input = input(FIRST_INPUT_STRING_MSG)
    while user_input != "0":
        # Get User input
        print("\n----- Buy a product Stage ------")
        user_input = input(INPUT_PRODUCTS_STRING_MSG.format(product_names))
        print("\tYour selected: ", user_input)

        # Validate input
        is_product = validate_user_input(test_products, user_input)
        #
        process_coin_input(is_product, test_products, users, user_input, user_count)

    sys.exit()

ALLOWED_COINS = [5, 10, 20, 50, 100]
# Strings
FIRST_INPUT_STRING_MSG = "\tEnter any key - to buy a product:\n" \
                           "\tor Enter 0 to exit app: "
LAST_INPUT_STRING_MSG = "\tPurchase complete. Next customer or Make new purchase." \
                        " \tEnter any key to buy a product:\n" \
                           "\tor Enter 0 to exit app: "
INPUT_PRODUCTS_STRING_MSG = "\tProducts list:\n {} \tEnter Product No.: "
INPUT_COIN_STRING_MSG = "\tInsert coin. Coins allowed {}\n\t: ".format(str(ALLOWED_COINS))
INPUT_COIN_STRING_MSG_WITH_EXIT = "\tInsert coin. Coins allowed {} OR " \
                                  "Input \"0\" for exit application\n\t: ".format(str(ALLOWED_COINS))

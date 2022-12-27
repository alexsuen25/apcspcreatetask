print("Hi, welcome to the Stock Tracker Program!")
print("Here is the default starting portfolio that you will manage over the course of this game")
print("Please input specific information when prompted.")

def show_portfolio(stock_list, cash_left):
    print('---------------------------------------------------------------------------------------')
    print("Stock Name  Average Purchase Price  Total Number of Shares Owned  Current Share Price")
    print('---------------------------------------------------------------------------------------')
    for item in stock_list:
        for index in range(4):
            if index > 0:
                print("{:.2f}".format(item[index]), '\t\t\t\t\t', end='')
            else:
                print(item[index], '\t\t\t\t\t', end='')
        print('')
        print('---------------------------------------------------------------------------------------')
    print('Total Cash Left        ', "{:.2f}".format(cash_left))
    print('---------------------------------------------------------------------------------------')

def get_price_and_share(stock, buy_sell):
    while True:
        price = input("What is the current price of " + stock + "?")
        shares = input("How many shares did you "+buy_sell+" of " + stock + "?")
        try:
            price = float(price)
            shares = int(shares)
            break
        except ValueError:
            print("Please enter integer number of shares and decimal of price")
    return price, shares

def transaction(stock_list, cash):
    cash_left = cash
    for item in stock_list:
        stock = item[0]
        while True:
            user_request = input("Did you buy, sell, or hold " + stock + "?")
            if user_request == 'buy' or user_request == 'sell' or user_request == 'hold':
                break
            else:
                print('Please enter buy, sell. or hold')
        if user_request == "buy":
            new_price, new_shares = get_price_and_share(stock, 'buy')
            old_share_price = item[1] * item[2]
            new_share_price = new_price * new_shares
            if new_share_price <= cash_left:
                new_average = (old_share_price + new_share_price) / (new_shares + item[2])
                item[1] = new_average
                item[3] = new_price
                item[2] += new_shares
                cash_left -= new_share_price
            else:
                print("You don't have enough money!")
            show_portfolio(stock_list, cash_left)
        elif user_request == "sell":
            new_price, new_shares = get_price_and_share(stock, 'sell')
            old_share_price = item[1] * item[2]
            new_share_price = new_price * new_shares
            if item[2] > new_shares:
                item[3] = new_price
                item[2] -= new_shares
                cash_left += new_share_price
            elif item[2] == new_shares:
                item[1] = 0
                item[3] = new_price
                item[2] -= new_shares
                cash_left += new_share_price
            else:
                print("You don't have enough shares to sell!")
            show_portfolio(stock_list, cash_left)
        else:
            show_portfolio(stock_list, cash_left)
    return cash_left

def add_new_stock(stock_list, cash):
    cash_left = cash
    item = ["", 0.0, 0.0, 0.0]
    stock = input("Please enter new stock name:")
    new_price, new_shares = get_price_and_share(stock, 'buy')
    new_share_price = new_price * new_shares
    if new_share_price <= cash_left:
        item[0] = stock
        item[1] = float(new_price)
        item[3] = float(new_price)
        item[2] = float(new_shares)
        cash_left -= new_share_price
        stock_list.append(item)
    else:
        print("You don't have enough money!")
    show_portfolio(stock_list, cash_left)
    return cash_left

stock_list = [["StockA", 100.0, 50.0, 100.0], ["StockB", 30.0, 100.0, 30.0], ["StockC", 54.0, 35.0, 54.0]]
remain_cash = 10000.0

while True:
    show_portfolio(stock_list, remain_cash)
    remain_cash = transaction(stock_list, remain_cash)
    while True:
        user_response = input("Do you want to enter new stocks in your portfolio?")
        if user_response == "Yes" or user_response == "yes":
            remain_cash = add_new_stock(stock_list, remain_cash)
        else:
            break
    user_response = input("Do you want to continue updating your portfolio?")
    if user_response == "Yes" or user_response == "yes":
        continue
    else:
        print("Thank you for inputting your stock. I hope you had fun!")
        break
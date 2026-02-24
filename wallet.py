import json
import importlib
config = importlib.import_module("config")

wallet = {
    "p" : 0,
    "g" : 10,
    "e" : 0,
    "s" : 0,
    "c" : 0
}

values_in_copper = {
    "p" : 1000,
    "g" : 100,
    "e" : 50,
    "s" : 10,
    "c" : 1
}

def create_wallet():
    with open(f"{config.char_name}/wallet_{config.char_name}.json", 'x') as file:
        json.dump(wallet, file, indent = 4)
    return None

def save_to_wallet():
    with open(f"{config.char_name}/wallet_{config.char_name}.json", 'w') as file:
        json.dump(wallet, file, indent = 4)
    return None

def load_wallet():
    global wallet
    try:
        with open(f"{config.char_name}/wallet_{config.char_name}.json", 'r') as file:
            wallet = json.load(file)
    except:
        create_wallet()
    return None

def setup_wallet():
    global wallet
    for i in wallet:
        tmp = False
        while not tmp:
            amount = input(f"amount of {i}:    ")
            tmp, amount = config.is_pos_int(amount)
            if not tmp:
                print("your input needs to be a positive integer!")
        wallet[i] = amount
    save_to_wallet()
    return None

def currency_exchange():
    global wallet
    tmp = False
    while not tmp:
        c1 = input("which currency do you want to change?    ")
        try:
            v1 = values_in_copper[c1]
            tmp = True
        except:
            print(f"'{c1}' is not a valid type of currency!")
    tmp = False
    while not tmp:
        c2 = input("to which currency do you want to convert?    ")
        if c1 != c2:
            try:
                v2 = values_in_copper[c2]
                tmp = True
            except:
                print(f"'{c2}' is not a valid type of currency!")
        else:
            print(f"you cannot convert {c1} to {c1} - why would you even try?")
    tmp = False
    while not tmp:
        amount = input(f"how much {c1} do you want to convert to {c2}?    ")
        tmp, amount = config.is_pos_int(amount)
        if not tmp:
            print("your input needs to be a positive integer!")
    result = amount * v1 / v2
    if result < 1:
        return print(f"{amount}{c1} is worth only {result}{c2}, which is less than one, so you cannot complete this conversion as there are no floats in dnd's currencies.")
    elif result % 1 != 0:
        print(f"{amount}{c1} is worth {result}{c2}, but the amount you hold of any currency must be an integer as there there are no floats in dnd's currencies.")
        tmp = False
        while not tmp:
            answer = input("would you like to proceed and convert as much as you can without loss? y/n   ")
            try:
                answer = config.y_or_n(answer)
                tmp = True
            except:
                print("that is not a valid answer! please enter 'y' for 'yes' or 'n' for 'no'!")
        if answer:
            # round down to the next convertable value - subtract that which cannot be converted without using floats
            # that means we have to flip v2 and v1 because we need the fraction's enumerator, not the fraction, and v2 is always > v1 in this scenario
            # if it wasn't, we would be converting to a less valuable currency, which cannot leave us with result % 1 != 0.
            amount -= (amount % (v2 // v1))
            amount = int(amount)
        else:
            return print("conversion aborted")
    wallet[c1] = wallet[c1] - amount
    result = int(result)
    wallet[c2] = wallet[c2] + result
    save_to_wallet()
    return print(f"you have successfully converted {amount}{c1} to {result}{c2}!")

def payment():
    global wallet
    tmp = False
    while not tmp:
        currency = input("with which currency will you pay?    ")
        if currency in wallet:
            tmp = True
        else:
            print(f"'{currency}' is not a valid currency!")
    tmp = False
    while not tmp:
        amount = input("how much will you spend?    ")
        tmp, amount = config.is_pos_int(amount)
        if not tmp:
            print("your input needs to be a positive integer!")
    new_amount = wallet[currency] - amount
    if new_amount < 0:
        print(f"you don't have that much {currency}")
    else:
        wallet[currency] = new_amount
        print(f"you now have {new_amount}{currency}")
        save_to_wallet()
    return None

def payday():
    global wallet
    tmp = False
    while not tmp:
        currency = input("which currency did you get?    ")
        if currency in wallet:
            tmp = True
        else:
            print(f"'{currency}' is not a valid currency!")
    tmp = False
    while not tmp:
        amount = input("how much did you get?    ")
        tmp, amount = config.is_pos_int(amount)
        if not tmp:
            print("your input needs to be a positive integer!")
    new_amount = wallet[currency] + amount
    wallet[currency] = new_amount
    print(f"you now have {new_amount}{currency}")
    save_to_wallet()
    return None

def init_wallet():
    load_wallet()
    return None


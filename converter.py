from menu_currency import Menu as CurrencyMenu
def to_dollars():
    return 20.27

def to_euros():
    return 23.51

def opt_exchange_factor(opt):
    if opt == 1:
        return to_dollars()
    elif opt == 2:
        return to_euros

def main():
    pesos = float(input("Amount in MXN: $"))
    (opt, new_coin_label) = CurrencyMenu().menu()
    exchange_factor = opt_exchange_factor(opt)
    new_coin = pesos/exchange_factor
    new_coin = round(new_coin,2)
    new_coin = str(new_coin)
    print("Equivalent: ${} {}".format(new_coin, new_coin_label))


if __name__ == "__main__":
    main()
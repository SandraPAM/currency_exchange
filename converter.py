def main():
    pesos = float(input("Amount in MXN: $"))
    exchange_factor = 20.27
    new_coin = pesos/exchange_factor
    new_coin = round(new_coin,2)
    new_coin = str(new_coin)
    print("Equivalent : ${} dollars".format(new_coin))


if __name__ == "__main__":
    main()
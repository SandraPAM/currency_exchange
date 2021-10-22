def main():
    pesos = float(input("Ingrese la cantidad en pesos MXN: $"))
    factor_dolar = 20.27
    dolares = pesos/factor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("El equivalente es : ${} dólares".format(dolares))


if __name__ == "__main__":
    main()
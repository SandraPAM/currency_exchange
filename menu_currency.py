class Menu:
    def __init__(self) -> None:
        self.options = [(1, "dollars"), (2, "euros")]

    def main(self):
        self.menu()

    def menu(self):
        print("1. To dollars")
        print("2. To euros")
        opt = int(input("Type exchange option: "))
        return self.options[opt-1]

    def opt_validation(self):
        pass



if __name__ == "__main__":
    Menu().main()



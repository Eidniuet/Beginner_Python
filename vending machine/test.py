class Vending_Machine:
    def get_quantity(self):  # Note the 'self' parameter
        while True:
            num = input("Please enter the quantity to buy: ")
            if num.isdigit():
                return int(num)
            else:
                print("Invalid Value. Please enter a valid integer.")

    def main(self):
        num = self.get_quantity()  # Call instance method using 'self'
        print(f"You selected {num} items.")

if __name__ == '__main__':
    vending_machine = Vending_Machine()  
    vending_machine.main()
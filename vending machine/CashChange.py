# Requirements:

# Code a vending machine application that has 5 different beverages of different prices in RM, no coins.

# Application is in Python language.


# Outcome:

# The logic of the vending machine will be able to return the least amount of notes back to the customers.

import pandas as pd
import numpy as np

class Vending_Machine:
    def __init__(self):
        self.products = [
            {   
                'itemName': 'Coke',
                'itemID': '1',
                'itemPrice': 10 
            },{   
                'itemName': 'Milk',
                'itemID': '2',
                'itemPrice': 8 
            },{   
                'itemName': '100Plus',
                'itemID': '3',
                'itemPrice': 5
            },{   
                'itemName': 'Tea',
                'itemID': '4',
                'itemPrice': 12 
            },{   
                'itemName': 'Mineral Water',
                'itemID': '5',
                'itemPrice': 3 
            }   
        ]
        self.product_df = pd.DataFrame(self.products)

        self.money_notes = {
                "RM50": 50, 
                "RM20": 20, 
                "RM10": 10, 
                "RM5": 5, 
                "RM1": 1}
        
    
    def show_products(self):
        # for product in self.products:
        #     print(f"Product: {product['itemName']} | ID: {product['itemID']} | Price: {product['itemPrice']}")
        print(self.product_df)

    def total_prices(self, selected_products):
        total_price = 0
        for item_name, quantity in selected_products.items():
            product = next((product for product in self.products if product['itemName'] == item_name), None)
            if product:
                item_price = product['itemPrice']
                total_price += item_price * quantity
        return total_price

    def return_notes(self, remaining):
        change = remaining
        notes_list = {}
        for note_key, note_value in self.money_notes.items():
            if change >= note_value:
                num = change // note_value
                change = change % note_value
                notes_list[note_key] = num
        return notes_list

    
    def main(self):
        selected_products = {}
        print('------Drinks Vending Machine------')
        self.show_products()
        
        while True:
            input_product = input('Enter the product ID (1-5) for the product you want to buy or "n" to stop or "r" to reset or "d" to delete product: ')
            if (input_product.lower() == 'n' or input_product.lower() =='no'):
                if not selected_products:
                    continue
                else:
                    print(f'Current Product: {selected_products} | Current Price: {total_prices}')
                    break

            elif input_product.lower() == 'r':
                selected_products = {}
                total_prices = 0
                print("Selected reset product.")
                continue

            elif input_product.lower() == 'd':
                while True:
                    del_id = input("Enter the product ID (1-5) for the product you want to delete: ")
                    if not del_id.isdigit() or int(del_id) < 1 or int(del_id) > 5:
                        print("Invalid product . Please enter a valid product ID (1-5).")
                        continue
                    del_num = input("Please enter the quantity to buy: ")
                    while not del_num.isdigit() and not isinstance(del_num, int):
                        print("Invalid Value")
                        del_num = input("Please enter correct the quantity to buy: ")
                    
                    del_num = int(del_num)
                    product = next((product for product in self.products if product['itemID'] == del_id), None)

                    if product:
                        product_name = product['itemName']
                        
                    if product_name in selected_products:
                        if selected_products[product_name] < del_num:
                            del selected_products[product_name]
                            break
                        else:
                            selected_products[product_name] -= del_num
                            break
                    else:
                        print("No valid products")
                        break
                total_prices = self.total_prices(selected_products)
                print(f'Current Products: {selected_products} | Total Prices: {total_prices}')
                continue

            elif not input_product.isdigit() or int(input_product) < 1 or int(input_product) > 5:
                print("Invalid product ID. Please enter a valid product ID (1-5).")
                continue

            if any(product['itemID'] == input_product for product in self.products):
                num = input("Please enter the quantity to buy: ")
                while not num.isdigit() and not isinstance(num, int):
                    print("Invalid Value")
                    num = input("Please enter correct the quantity to buy: ")
            
            num = int(num)
            product = next((product for product in self.products if product['itemID'] == input_product), None)

            if product:
                product_name = product['itemName']
            if product_name in selected_products:
                selected_products[product_name] += num
            else:
                selected_products[product_name] = num
            
            total_prices = self.total_prices(selected_products)
            print(f'Current Products: {selected_products} | Total Prices: {total_prices}')
        

        while True:
            try:
                cash = int(input("Please enter the cash amount: "))
                break  # Exit the loop if a valid integer is provided
            except ValueError:
                print("Invalid input. Please enter a valid integer for cash.")

        while cash < total_prices:
            print(f"Insufficient money: Cash In: {cash} less than Total Price: {total_prices}")
            while True:
                try:
                    extra_cash = int(input("Please enter additional cash amount: "))
                    cash += extra_cash
                    break  # Exit the loop if a valid integer is provided
                except ValueError:
                    print("Invalid input. Please enter a valid integer for cash.")
        
        remaining = cash - total_prices
        money_list = self.return_notes(remaining)
        bill_dict = [{'': 'Cash', 'RM': cash},
                    {'': 'Total Price', 'RM': total_prices},
                    {'': 'Return Money',  'RM': remaining }]
        bill_df = pd.DataFrame(bill_dict)
        print('-----Bills-----')
        print(bill_df)
        print(f'Money Notes: {money_list}')
        
        


if __name__ == '__main__':
    vending_machine = Vending_Machine()  
    vending_machine.main()




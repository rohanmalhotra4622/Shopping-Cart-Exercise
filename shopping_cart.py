
# shopping_cart.py

#from pprint import pprint

import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50 , "price_per_pound" : "Y"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99 , "price_per_pound" : "N"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49 , "price_per_pound" : "Y"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99 , "price_per_pound" : "N"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99 , "price_per_pound" : "Y"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99 , "price_per_pound" : "N"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50 , "price_per_pound" : "Y"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25 , "price_per_pound" : "N"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50 , "price_per_pound" : "Y"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99 , "price_per_pound" : "N"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99 , "price_per_pound" : "Y"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50 , "price_per_pound" : "N"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00 , "price_per_pound" : "Y"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99 , "price_per_pound" : "N"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50 , "price_per_pound" : "Y"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50 , "price_per_pound" : "N"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99 , "price_per_pound" : "Y"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50 , "price_per_pound" : "N"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99 , "price_per_pound" : "Y"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25 , "price_per_pound" : "N"},
    {"id":21, "name": "Organic Bananas", "department": "fruits", "aisle": "produce", "price": 0.79 , "price_per_pound" : "Y"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

# Information Capture Input

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")

print('    ')  # to make it more appealing to the eye and easier to read
print('---------------------')
print('GREEN FOODS GROCERY')
print('Website: ' + 'green_foods_grocery.com')
print('phone: ' + '212-111-0000')
print('---------------------')
print('CHECKOUT AT: ' + now)
print('---------------------')

# Define Variables

total_price = 0
selected_ids = []
tax = .0875

# Enter product and weight if applicable and calculate total price

product_length = range(0,len(products))

while True:
    try:
        selected_id = input('Please enter a product identifier: ')
        if selected_id == 'DONE' or selected_id == 'done':
            break
        elif int(selected_id) not in range(0, len(products) + 1):
            print('Selected ID not in list; please renter!')
        elif products[int(selected_id) -1]['price_per_pound'] == 'Y':
            weight = input('Please enter weight in pounds:')
            price = products[int(selected_id) -1]['price'] * float(weight)
            total_price = total_price + price
            selected_ids.append(selected_id)
        elif products[int(selected_id) -1]['price_per_pound'] == 'N':
            #weight = input('Please enter weight in pounds:')
            price = products[int(selected_id) -1]['price']
            total_price = total_price + price
            selected_ids.append(selected_id)
    except ValueError:
        print('Invalid entry; please try again!')

#print(selected_ids)

# Print product name and prices


print('---------------------')
print('SHOPPING CART ITEMS:')
for id in selected_ids:
    matching_products = [p for p in products if str(p['id']) == str(id)]
    matching_product = matching_products[0]
    print('  +  ' + matching_product['name'] + ' ' + ' ($' + '{0:.2f}'.format(matching_product['price']) + ')')
print('---------------------')

# Calculate tax, final total and format accordingly

print('SUBTOTAL: ' + ' $' + '{0:.2f}'.format(total_price))
total_tax = total_price * tax 
print('NYC SALES TAX (8.75%):'  + ' $' + '{0:.2f}'.format(total_tax))
final_total = total_price + total_tax
print('TOTAL PRICE:  ' + ' $' + '{0:.2f}'.format(final_total))
print('---------------------')
print('THANK YOU FOR YOUR BUSINESS! PLEASE COME AGAIN')


from pprint import pprint
import vault
import pref
import display
import filter

appliances = {
    'laptop': vault.laptop(),
    'smartphone': vault.smartphone(),
    'earphones': vault.earphones(),
    'television': vault.television(),
    'refrigerator': vault.refrigerator(),
}


def getdata(selection):
    if selection in appliances:
        return appliances[selection]


cart = []
cart_value = 0

while True:
    print("Products available here:")
    for index, item in enumerate(appliances):
        print(index, item)
    appliance = input("Enter appliance name: ")

    data = getdata(appliance)
    new_data = data

    _pref = input("Would you like to enter in your preferences before you look at buying options? (y/n) : ")
    if _pref == 'y':
        pref_data = pref.pref_input(appliance)
        new_data = filter.data_filter(appliance, pref_data, data)
        display.all_items(appliance, new_data)
    else:
        display.all_items(appliance, new_data)

    cart.append(new_data[int(input("Add to cart by typing the index of the product: "))])
    for item in cart:
        cart_value += int(item['price'])
    print("Product added to cart successfully! Cart Value = ", )
    if input("Would you like to keep browsing? (y/n) ") == 'y':
        continue
    else:
        break

print("INITIATING CHECKOUT")
print("Items in cart: ")
pprint(cart)
print("Please proceed by paying ₹" + str(cart_value), end="\n")
print("T H A N K Y O U")

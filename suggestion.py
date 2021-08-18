from pprint import pprint

data = {
    'laptop': [
        {
            'company': 'Dell',
            'RAM': 8,
            'Storage': 512,
            'processor': 'intel core i3'
        },
        {
            'company': 'HP',
            'RAM': 16,
            'Storage': 2046,
            'processor': 'intel core i5'
        },
        {
            'company': 'Lenovo',
            'RAM': 4,
            'Storage': 512,
            'processor': 'ryzen 3'
        },
        {
            'company': 'Asus',
            'RAM': 8,
            'Storage': 1024,
            'processor': 'ryzen 5'
        },
        {
            'company': 'Acer',
            'RAM': 8,
            'Storage': 512,
            'processor': 'intel core i7'
        },
    ],
    'Washing Machine': [
        {
            'company': 'LG',
            'type': 'front',
            'price': 30000,
            'capacity': 6
        },
        {
            'company': 'LG',
            'type': 'front',
            'price': 30000,
            'capacity': 6
        },
        {
            'company': 'LG',
            'type': 'front',
            'price': 30000,
            'capacity': 6
        },
        {
            'company': 'Samsung',
            'type': 'top',
            'price': 15000,
            'capacity': 4
        },
        {
            'company': 'Whirlpool',
            'type': 'front',
            'price': 45000,
            'capacity': 7
        },
    ]
}

# appliance_type = data['washing machine']
#
# for appliance in appliance_type:
#     if appliance['company'] == 'LG':
#         pprint(appliance['price'])

print(
    "Hello there! Looking products to buy? Let us know what you need from our catalogue: "
)
for item in data.keys():
    print(item)
user_appliance = input("Enter appliance: ")

appliance_type = data[user_appliance]

# To print all items

print("Here's the list of available items")
for item in appliance_type:
    print("Company:", item['company'] + '\t', '\t', "Type:",
        item['type'] + '\t', "Capacity:", str(item['capacity']),
        'Kgs' + '\t', "Price:", '$', str(item['price']))

user_type = input("Enter " + user_appliance + " type: ")
# user_price_low, user_price_high = input("Enter your budget: ")
user_company = input("Enter " + user_appliance + " company: ")

for item in appliance_type:
    if(item['type'] == user_type and item['company'] == user_company): 
        pprint(item)
        
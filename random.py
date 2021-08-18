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
            'type': 'top',
            'price': 15000,
            'capacity': 4
        },
        {
            'company': 'LG',
            'type': 'front',
            'price': 45000,
            'capacity': 7
        },
    ]
}


list1 = data['Washing Machine']

for item in list1:
    if (item['price'] <= 20000):
        pprint(item) 
    if (item['price'] <= 30000):
        pprint(item)
    if (item['price'] <= 40000):
        pprint(item)     
    if (item['price']  >40000):
        pprint(item)          
    elif(item['company']==LG):
        pprint(item)    
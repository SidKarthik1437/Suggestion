import vault


def all_items(appliance, data):
    print("Here's the list of available items")
    if appliance == 'laptop':
        for index, item in enumerate(data):
            print(str(index) + '\t',
                  "COMPANY:", item['company'] + '\t', '\t',
                  "RAM:", str(item['ram']) + 'gb' + '\t',
                  "SSD:", str(item['ssd']) + 'gb' + '\t',
                  "HDD:", str(item['hdd']) + 'gb' + '\t',
                  "PROCESSOR:", item['processor'] + '\t',
                  "PRICE: ", '₹' + str(item['price']) + '\t'
                  "URL: " + item['url']
                  )
    if appliance == 'smartphone':
        for index, item in enumerate(data):
            print(str(index) + '\t',
                  "COMPANY:", item['company'] + '\t',
                  "MODEL:", item['model'] + '\t',
                  "PRICE:", '₹' + str(item['price']) + '\t',
                  "RAM:", str(item['ram']) + 'GB' + '\t',
                  "STORAGE:", str(item['storage']) + 'GB' + '\t',
                  "CAMERA:", item['camera'], 'MP' + '\t',
                  "PROCESSOR:", item['processor'] + '\t',
                  "URL: " + item['link'])

    if appliance == 'earphones':
        for index, item in enumerate(data):
            print(str(index) + '\t',
                  "COMPANY:", item['company'] + '\t',
                  "MODEL:", item['model'] + '\t',
                  "PRICE:", '₹' + str(item['price']) + '\t',
                  "COLOR:", item['color'] + '\t',
                  "CONNECTIVITY:", item['connectivity'] + '\t',
                  "URL: " + item['link'])

    if appliance == 'television':
        for index, item in enumerate(data):
            print(str(index) + '\t',
                  "BRAND:", item['brand'] + '\t',
                  "MODEL:", item['resolution'] + '\t',
                  "RAM:", str(item['ram']) + 'GB' + '\t',
                  "SCREEN SIZE:", str(item['screensize']) + 'inches' + '\t',
                  "WARRANTY:", str(item['warranty']) + 'years' + '\t',
                  "PRICE:", '₹' + str(item['price']) + '\t',
                  "URL: " + item['url']
                  )
    if appliance == 'refrigerator':
        for index, item in enumerate(data):
            print(str(index) + '\t',
                  "BRAND:", item['brand'] + '\t',
                  "CHARACTERISTICS:",item['characteristics'] + '\t'
                  "CAPACITY:", str(item['capacity']) + 'liters' + '\t',
                  "PRICE:", '₹' + str(item['price']) + '\t',
                  "URL: " + item['url']
                  )
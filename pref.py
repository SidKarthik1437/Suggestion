import vault


def availitems(data):
    keys = []
    avail = []
    for item in data:
        for key in item.keys():
            if key not in keys:
                keys.append(key)
    for key in keys:
        temp = []
        for item in data:
            if item[key] not in temp:
                temp.append(item[key])
        avail.append(temp)
    return avail


def pref_input(appliance):
    print("AVAILABLE FILTERS FOR", appliance + "(select from displayed options / leave empty if none)")

    if appliance == 'laptop':
        data = vault.laptop()
        avail = availitems(data)

        print("IN STOCK " , avail[0])
        company = input("Enter preferred company: ")
        print("IN STOCK " ,avail[1])
        ram = input("Enter preferred memory size: ")
        print("IN STOCK " ,avail[2])
        ssd = input("Enter preferred SSD size: ")
        print("IN STOCK " ,avail[3])
        hdd = input("Enter preferred HDD size: ")
        print("IN STOCK " ,avail[4])
        processor = input("Enter preferred processor: ")
        low = input("Enter minimum budget: ")
        high = input("Enter maximum budget: ")

        return {'company': company, 'ram': ram, 'hdd': hdd, 'ssd': ssd, 'processor': processor,
                'low': low,
                'high': high
                }

    if appliance == 'smartphone':
        data = vault.smartphone()
        avail = availitems(data)

        print("IN STOCK ", avail[0])
        company = input("Enter preferred company: ")
        print("IN STOCK ", avail[1])
        model = input("Enter preferred model: ")
        print("IN STOCK ", avail[2])
        ram = input("Enter preferred memory size: ")
        print("IN STOCK ", avail[3])
        storage = input("Enter preferred storage size: ")
        print("IN STOCK ", avail[4])
        camera = input("Enter preferred camera specification (in MP): ")
        print("IN STOCK ", avail[5])
        processor = input("Enter preferred processor: ")
        low = input("Enter minimum budget: ")
        high = input("Enter maximum budget: ")

        return {'company': company,
                'ram': ram,
                'model': model,
                'storage': storage,
                'camera': camera,
                'processor': processor,
                'low': low,
                'high': high
                }

    if appliance == 'earphones':
        data = vault.earphones()
        avail = availitems(data)

        print("IN STOCK ", avail[0])
        company = input("Enter preferred company: ")
        print("IN STOCK ", avail[1])
        model = input("Enter preferred model: ")
        print("IN STOCK ", avail[2])
        color = input("Enter preferred color: ")
        print("IN STOCK ", avail[3])
        connectivity = input("Enter preferred type ")
        low = input("Enter minimum budget: ")
        high = input("Enter maximum budget: ")

        return {'company': company,
                'model': model,
                'color': color,
                'connectivity': connectivity,
                'low': low,
                'high': high
                }

    if appliance == 'television':
        data = vault.television()
        avail = availitems(data)

        print("IN STOCK ", avail[0])
        company = input("Enter preferred brand: ")
        print("IN STOCK ", avail[1])
        ram = input("Enter preferred memory size: ")
        print("IN STOCK ", avail[2])
        model = input("Enter preferred model: ")
        print("IN STOCK ", avail[3])
        screensize = input("Enter preferred screen size (inches): ")
        print("IN STOCK ", avail[4])
        warranty = input("Enter preferred warranty period (years) ")
        low = input("Enter minimum budget: ")
        high = input("Enter maximum budget: ")

        return {'company': company,
                'resolution': model,
                'ram': ram,
                'screensize': screensize,
                'warranty': warranty,
                'low': low,
                'high': high
                }
    if appliance == 'refrigerator':
        data = vault.refrigerator()
        avail = availitems(data)

        print("IN STOCK ", avail[0])
        company = input("Enter preferred brand: ")
        print("IN STOCK ", avail[1])
        characteristics = input("Enter preferred characteristics: ")
        print("IN STOCK ", avail[2])
        capacity = input("Enter preferred capacity (litres): ")
        low = input("Enter minimum budget: ")
        high = input("Enter maximum budget: ")

        return {'company': company,
                'characteristics': characteristics,
                'capacity': capacity,
                'low': low,
                'high': high
                }

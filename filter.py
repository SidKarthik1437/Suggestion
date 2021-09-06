def data_filter(appliance, pref_data, data):
    new_data = []
    print("filtering")
    if appliance == 'laptop':
        for item in data:
            for pref in pref_data:
                if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                    if pref_data['processor'] in item['processor'] or pref_data['processor'] == '':
                        if not pref_data[pref] == '' and not pref_data[pref] == ' ' \
                                and not pref == 'low' and not pref == 'high' and not pref == 'processor':
                            if str(item[pref]) == pref_data[pref]:
                                if item not in new_data:
                                    new_data.append(item)
                        # if item not in new_data:
                         #     new_data.append(item)
        for item in data:
            if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                if item not in new_data:
                    new_data.append(item)
        return new_data

    if appliance == 'smartphone':
        for item in data:
            for pref in pref_data:
                if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                    if pref_data['processor'] in item['processor']:
                        if not pref_data[pref] == '' and not pref_data[pref] == ' ' \
                                and not pref == 'low' and not pref == 'high' and not pref == 'processor':
                            if str(item[pref]) == pref_data[pref]:
                                if item not in new_data:
                                    new_data.append(item)

        for item in data:
            if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                if item not in new_data:
                    new_data.append(item)
        return new_data

    if appliance == 'earphones':
        for item in data:
            for pref in pref_data:
                if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                    if pref_data['model'] in item['model']:
                        if not pref_data[pref] == '' and not pref_data[pref] == ' ' \
                                and not pref == 'low' and not pref == 'high' and not pref == 'model':
                            if str(item[pref]) == pref_data[pref]:
                                if item not in new_data:
                                    new_data.append(item)
        for item in data:
            if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                if item not in new_data:
                    new_data.append(item)

        return new_data

    if appliance == 'television':
        for item in data:
            for pref in pref_data:
                if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                    if pref_data['resolution'] in item['resolution']:
                        if not pref_data[pref] == '' and not pref_data[pref] == ' ' \
                                and not pref == 'low' and not pref == 'high' and not pref == 'resolution':
                            if str(item[pref]) == pref_data[pref]:
                                if item not in new_data:
                                    new_data.append(item)

        for item in data:
            if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                if item not in new_data:
                    new_data.append(item)
        return new_data

    if appliance == 'refrigerator':
        for item in data:
            for pref in pref_data:
                if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                    if pref_data['characteristics'] in item['characteristics']:
                        if not pref_data[pref] == '' and not pref_data[pref] == ' ' \
                                and not pref == 'low' and not pref == 'high' and not pref == 'characteristics':
                            if str(item[pref]) == pref_data[pref]:
                                if item not in new_data:
                                    new_data.append(item)

        for item in data:
            if int(pref_data['low']) < item['price'] < int(pref_data['high']):
                if item not in new_data:
                    new_data.append(item)
        return new_data

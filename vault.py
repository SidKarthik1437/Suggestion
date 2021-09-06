def laptop():
    data = [
        {
            "company": "Fujitsu",
            "ram": 16,
            "ssd": 512,
            "hdd": 0,
            "processor": "Intel Core i7",
            "price": 92990,
            "rating": 4.5,
            "url": "https://www.amazon.in/Fujitsu-33-78cm-Graphics-Fingerprint-4ZR1D67596/dp/B098P34QRL/ref=sr_1_1_sspa?dchild=1&qid=1630856529&refinements=p_36%3A7252032031&rnid=7252027031&s=computers&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExODVVU1RFRzBFSDU0JmVuY3J5cHRlZElkPUEwMjkyODgzMkpLUFo4NDNYWFpNWiZlbmNyeXB0ZWRBZElkPUEwOTc4NTI3MjZLUjdEQUgwNk5OMSZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
        },
        {
            "company": "Apple",
            "ram": 8,
            "ssd": 256,
            "hdd": 0,
            "processor": "Apple M1",
            "price": 88490,
            "rating": 5,
            "url": "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_7?dchild=1&qid=1630861235&refinements=p_36%3A7252032031&rnid=7252027031&s=computers&sr=1-7"
        },
        {
            "company": "Lenovo",
            "ram": 16,
            "ssd": 512,
            "hdd": 0,
            "processor": "Intel Core i5",
            "price": 72824,
            "rating": 5,
            "url": "https://www.amazon.in/Lenovo-IdeaPad-Fingerprint-Graphite-82FG0148IN/dp/B096SKBM59/ref=sr_1_10?dchild=1&qid=1630859298&refinements=p_36%3A7252032031%2Cp_89%3ALenovo&rnid=3837712031&s=computers&sr=1-10"
        },
        {
            "company": "ASUS",
            "ram": 8,
            "ssd": 512,
            "hdd": 0,
            "processor": "AMD Ryzen 7",
            "price": 74990,
            "rating": 4.5,
            "url": "https://www.amazon.in/ASUS-15-6-inch-RTX-3050-Graphics-FA506IC-HN005T/dp/B09CCW5XVM/ref=sr_1_1?dchild=1&qid=1630859350&refinements=p_36%3A7252032031%2Cp_89%3AASUS&rnid=3837712031&s=computers&sr=1-1"
        },
        {
            "company": "HP",
            "ram": 16,
            "ssd": 512,
            "hdd": 0,
            "processor": "Intel Core i5 ",
            "price": 66990,
            "rating": 4,
            "url": "https://www.amazon.in/HP-Pavilion-Graphics-Keyboard-14-dv0054TU/dp/B08WBB369L/ref=sr_1_1?dchild=1&qid=1630859376&refinements=p_36%3A7252032031%2Cp_89%3AASUS%7CHP&rnid=3837712031&s=computers&sr=1-1"
        },
        {
            "company": "ASUS",
            "ram": 8,
            "ssd": 512,
            "hdd": 0,
            "processor": "Intel Core i5",
            "price": 61990,
            "rating": 4.5,
            "url": "https://www.amazon.in/ASUS-i5-10300H-Graphics-Fortress-FX566LH-HN257T/dp/B08CRMTKMK/ref=sr_1_6?dchild=1&qid=1630859376&refinements=p_36%3A7252032031%2Cp_89%3AASUS%7CHP&rnid=3837712031&s=computers&sr=1-6"
        },
        {
            "company": "Lenovo",
            "ram": 8,
            "ssd": 256,
            "hdd": 0,
            "processor": "Intel Core i5",
            "price": 54990,
            "rating": 4.5,
            "url": "https://www.amazon.in/Lenovo-IdeaPad-Keyboard-warranty-82H80156IN/dp/B09BCSPX7X/ref=sr_1_1_sspa?dchild=1&qid=1630858029&refinements=p_36%3A7252032031&rnid=7252027031&s=computers&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQkNJMjhFM1NIUUJEJmVuY3J5cHRlZElkPUEwODQ2OTAzMkRJSUYwMURUOFJWMiZlbmNyeXB0ZWRBZElkPUEwMzk0OTM0Mkg4UFpGUjNMVzdXRCZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
        },
        {
            "company": "HP",
            "ram": 8,
            "ssd": 512,
            "hdd": 0,
            "processor": "Intel Core i5",
            "price": 58490,
            "rating": 4,
            "url": "https://www.amazon.in/HP-Processor-14-inch-Windows-14s-dr2016tu/dp/B092MS22P1/ref=sr_1_3?dchild=1&qid=1630859376&refinements=p_36%3A7252032031%2Cp_89%3AASUS%7CHP&rnid=3837712031&s=computers&sr=1-3"
        },
        {
            "company": "HP",
            "ram": 8,
            "ssd": 256,
            "hdd": 1024,
            "processor": "AMD Ryzen 5",
            "price": 47990,
            "rating": 4,
            "url": "https://www.amazon.in/HP-14-inch-Windows-Natural-14s-dk0501AU/dp/B0991MJLN2/ref=sr_1_9?dchild=1&qid=1630858029&refinements=p_36%3A7252032031&rnid=7252027031&s=computers&sr=1-9"
        },
        {
            "company": "Dell",
            "ram": 8,
            "ssd": 1024,
            "hdd": 0,
            "processor": "Intel Core i5",
            "price": 49990,
            "rating": 4.5,
            "url": "https://www.amazon.in/Dell-i5-1135G7-Integrated-Graphics-D552154WIN9BE/dp/B08RXZCXH6/ref=sr_1_22?dchild=1&qid=1630858029&refinements=p_36%3A7252032031&rnid=7252027031&s=computers&sr=1-22"
        },
        {
            "company": "Lenovo",
            "ram": 8,
            "ssd": 0,
            "hdd": 1024,
            "processor": "Intel Core i3",
            "price": 39490,
            "rating": 4,
            "url": "https://www.amazon.in/Lenovo-Graphics-warranty-Platinum-81WB015GIN/dp/B0999BTTKZ/ref=sr_1_6?dchild=1&qid=1630859811&refinements=p_36%3A7252030031&rnid=7252027031&s=computers&sr=1-6"
        },
        {
            "company": "HP",
            "ram": 8,
            "ssd": 0,
            "hdd": 1024,
            "processor": "AMD Ryzen 3",
            "price": 37990,
            "rating": 4,
            "url": "https://www.amazon.in/HP-3-3250-Laptop-Windows-15s-gr0011AU/dp/B08T6SJ215/ref=sr_1_4?dchild=1&qid=1630859811&refinements=p_36%3A7252030031&rnid=7252027031&s=computers&sr=1-4"
        },
        {
            "company": "Dell",
            "ram": 4,
            "ssd": 256,
            "hdd": 1024,
            "processor": "Intel Core i3",
            "price": 39866,
            "rating": 4,
            "url": "https://www.amazon.in/Dell-i3-1005G1-Integrated-Graphics-D552151WIN9BE/dp/B08R777GBL/ref=sr_1_12?dchild=1&qid=1630859811&refinements=p_36%3A7252030031&rnid=7252027031&s=computers&sr=1-12"
        }
    ]

    return data
    # {
    # 'company': '',
    # 'ram':,
    # 'ssd':,
    # 'hdd':,
    # 'processor': '',
    # 'price':,
    # 'rating':,
    # url: '',
    # },

def smartphone():
    data = [
        {
            "company": "POCO",
            "model": "M3",
            "price": 10499,
            "ram": 4,
            "storage": 64,
            "camera": 48,
            "processor": "Qualcomm Snapdragon 662",
            "link": "https://www.flipkart.com/poco-m3-power-black-64-gb/p/itm39e9e3fb7d8b2?pid=MOBG4CGFRMX2AKFD&lid=LSTMOBG4CGFRMX2AKFDNJETFV&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=clp_banner_2_3.bannerX3.BANNER_smartphone-carnival-7kk9ih-9opl3-store_QX7ZRT2PK9PB&fm=neo%2Fmerchandising&iid=18161b07-4940-47ef-826c-28bcdd599cce.MOBG4CGFRMX2AKFD.SEARCH&ppt=clp&ppn=smartphone-carnival-7kk9ih-9opl3-store&ssid=y6pyr20d9c0000001630851835269"
        },

        {
            "company": "REALME",
            "model": "C20",
            "price": 7499,
            "ram": 2,
            "storage": 32,
            "camera": 8,
            "processor": "MediaTek Helio G35",
            "link": "https://www.flipkart.com/realme-c20-cool-blue-32-gb/p/itmea1903897436b?pid=MOBGF4894MEWZJGV&lid=LSTMOBGF4894MEWZJGVW425N5&marketplace=FLIPKART&q=real+me+c20&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_6_9_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_9_na_na_na&fm=SEARCH&iid=92219285-c954-4370-879e-351f918638c9.MOBGF4894MEWZJGV.SEARCH&ppt=pp&ppn=pp&ssid=z3xl2pzpds0000001630852859426&qH=b3c7adc21902db60"
        },

        {
            "company": "INFINIX",
            "model": "Smart 5",
            "price": 6999,
            "ram": 2,
            "storage": 32,
            "camera": 13,
            "processor": "MediaTek Helio G25",
            "link": "https://www.flipkart.com/infinix-smart-5a-quetzal-cyan-32-gb/p/itma0d1e81b14743?pid=MOBG56UGAS4CFKTK&lid=LSTMOBG56UGAS4CFKTKXZCJLS&marketplace=FLIPKART&q=infinix+smart+5&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_ps&fm=SEARCH&iid=e68a4e55-3711-43aa-9fa1-95d0f156b7d1.MOBG56UGAS4CFKTK.SEARCH&ppt=sp&ppn=sp&ssid=yiszngxxgw0000001630852912520&qH=6318b6631012fe26"
        },

        {
            "company": "POCO",
            "model": "C3 4gb",
            "price": 8499,
            "ram": 4,
            "storage": 64,
            "camera": 13,
            "processor": "Mediatek Helio G35",
            "link": "https://www.flipkart.com/infinix-smart-5a-quetzal-cyan-32-gb/p/itma0d1e81b14743?pid=MOBG56UGAS4CFKTK&lid=LSTMOBG56UGAS4CFKTKXZCJLS&marketplace=FLIPKART&q=infinix+smart+5&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_ps&fm=SEARCH&iid=e68a4e55-3711-43aa-9fa1-95d0f156b7d1.MOBG56UGAS4CFKTK.SEARCH&ppt=sp&ppn=sp&ssid=yiszngxxgw0000001630852912520&qH=6318b6631012fe26"
        },

        {
            "company": "REDMI",
            "model": "9 Prime",
            "price": 10499,
            "ram": 4,
            "storage": 64,
            "camera": 13,
            "processor": "MediaTek Helio G80",
            "link": "https://www.flipkart.com/redmi-9-prime-space-blue-64-gb/p/itme138a7bc1c7f5?pid=MOBFUT9M84NDDYQN&lid=LSTMOBFUT9M84NDDYQN9NHPW2&marketplace=FLIPKART&q=redmi+9+prime&store=tyy%2F4io&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_ps&fm=SEARCH&iid=307c5e7b-55e6-4b64-b5d7-a159980c7e4a.MOBFUT9M84NDDYQN.SEARCH&ppt=sp&ppn=sp&ssid=x45b63wmgw0000001630853068827&qH=8da575e93aad7ab3"
        },

        {
            "company": "REDMI",
            "model": "Note 9 ",
            "price": 11999,
            "ram": 4,
            "storage": 64,
            "camera": 48,
            "processor": "MediaTek Helio G85",
            "link": "https://www.flipkart.com/redmi-note-9-pebble-grey-64-gb/p/itmb9c65ffe0ee74?pid=MOBFU3ZFQ3GAGANG&lid=LSTMOBFU3ZFQ3GAGANG1QDSWB&marketplace=FLIPKART&q=redmi+9note+9&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=f7978a6d-d5cf-4c69-ae4d-db45300f67a0.MOBFU3ZFQ3GAGANG.SEARCH&ppt=sp&ppn=sp&ssid=fy0oa6y7qo0000001630853098271&qH=f7e715ba09dd32e3"
        },

        {
            "company": "REALME",
            "model": "C25s ",
            "price": 10999,
            "ram": 4,
            "storage": 128,
            "camera": 13,
            "processor": "MediaTek Helio G85",
            "link": "https://www.flipkart.com/realme-c25-watery-blue-128-gb/p/itm62d25188ea98a?pid=MOBGFZ7VE45TEDSJ&lid=LSTMOBGFZ7VE45TEDSJIA5ISK&marketplace=FLIPKART&q=realme+c25&store=tyy%2F4io&srno=s_1_3&otracker=AS_Query_OrganicAutoSuggest_4_8_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_4_8_na_na_ps&fm=SEARCH&iid=b9116e3e-d9a7-4c38-af26-f23fc9af5315.MOBGFZ7VE45TEDSJ.SEARCH&ppt=sp&ppn=sp&ssid=fui1n8r05s0000001630853133230&qH=2e301b94bf836845"
        },

        {
            "company": "REALME",
            "model": "Narzo 30 5G",
            "price": 16999,
            "ram": 6,
            "storage": 128,
            "camera": 48,
            "processor": "MediaTek Dimensity 700",
            "link": "https://www.flipkart.com/realme-narzo-30-5g-racing-silver-128-gb/p/itm56837fcb0d6f3?pid=MOBG3W3GWVTBTQZQ&lid=LSTMOBG3W3GWVTBTQZQGONJ0G&marketplace=FLIPKART&q=realme+narzo+30&store=tyy%2F4io&srno=s_1_7&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&fm=SEARCH&iid=42757420-fbfc-4c98-8fa6-6edcda528061.MOBG3W3GWVTBTQZQ.SEARCH&ppt=sp&ppn=sp&ssid=cizqcdykv40000001630853265407&qH=0eaa4b5e3d0b0adb"
        },

        {
            "company": "SAMSUNG",
            "model": "Galaxy F22 ",
            "price": 12999,
            "ram": 4,
            "storage": 64,
            "camera": 48,
            "processor": "MediaTek Helio G80",
            "link": "https://www.flipkart.com/samsung-galaxy-f22-denim-black-64-gb/p/itm6f47a19cb79ae?pid=MOBG43UGC3PYCBZF&lid=LSTMOBG43UGC3PYCBZFPZLL2Q&marketplace=FLIPKART&q=samsung+galaxy+f22&store=tyy%2F4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_ps&fm=SEARCH&iid=e83bdf4b-ecd8-46ad-a7ea-6f663287aeb0.MOBG43UGC3PYCBZF.SEARCH&ppt=sp&ppn=sp&ssid=qb5nzvqips0000001630853328829&qH=78e811620418a5c1 "
        },

        {
            "company": " MOTOROLA",
            "model": "E7 Power ",
            "price": 8799,
            "ram": 4,
            "storage": 64,
            "camera": 13,
            "processor": "MediaTek Helio G25",
            "link": "https://www.flipkart.com/motorola-e7-power-coral-red-64-gb/p/itm3300062c815ba?pid=MOBFVH62GXHPHPFW&lid=LSTMOBFVH62GXHPHPFWMFPQQ0&marketplace=FLIPKART&q=moto+e7+power&store=tyy%2F4io&srno=s_1_2&otracker=AS_Query_OrganicAutoSuggest_2_8_sc_na_ps&otracker1=AS_Query_OrganicAutoSuggest_2_8_sc_na_ps&fm=SEARCH&iid=adfe82e8-d3bc-4ab6-a25e-4eca790a4f38.MOBFVH62GXHPHPFW.SEARCH&ppt=sp&ppn=sp&ssid=0c0wet5xmo0000001630853370252&qH=3451f759bf347aa4"
        },

        {
            "company": "SAMSUNG",
            "model": "M31",
            "price": 16661,
            "ram": 6,
            "storage": 128,
            "camera": 64,
            "processor": "Samsung Exynos 9 Octa 9611",
            "link": "https://www.flipkart.com/samsung-galaxy-m31-space-black-128-gb/p/itmeb29fb2c00580?pid=MOBFPNPS6QGTKBQB&lid=LSTMOBFPNPS6QGTKBQBGM8FDO&marketplace=FLIPKART&q=samsung+m31&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_2_9_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_2_9_na_na_ps&fm=SEARCH&iid=abb76957-5955-4af0-ba25-e08a86b4babb.MOBFPNPS6QGTKBQB.SEARCH&ppt=sp&ppn=sp&ssid=7whfq0m89c0000001630853399660&qH=72c0d4f69be69bf9"
        },

        {
            "company": "MOTOROLA",
            "model": "G40 Fusion",
            "price": 16499,
            "ram": 6,
            "storage": 128,
            "camera": 64,
            "processor": "Qualcomm Snapdragon 732G ",
            "link": "https://www.flipkart.com/motorola-g40-fusion-dynamic-gray-128-gb/p/itm0da1b05fa3a9e?pid=MOBFWSF8XAZVCJHZ&lid=LSTMOBFWSF8XAZVCJHZYTOUM6&marketplace=FLIPKART&q=moto+g40+fusion+mobile&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_ps&fm=SEARCH&iid=05fc69dd-b94c-4cb5-84d6-83c2ead799f3.MOBFWSF8XAZVCJHZ.SEARCH&ppt=sp&ppn=sp&ssid=zcckg13va80000001630853512841&qH=93fbbfc019c334cc"
        },

        {
            "company": "OPPO",
            "model": "A53s 5G",
            "price": 15990,
            "ram": 6,
            "storage": 128,
            "camera": 13,
            "processor": "MediaTek Dimensity 700",
            "link": "https://www.flipkart.com/oppo-a53s-5g-crystal-blue-128-gb/p/itm7dd84770173a5?pid=MOBG25PGC3KZKETA&lid=LSTMOBG25PGC3KZKETA7MPWGP&marketplace=FLIPKART&q=oppo+a53s&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_5_7_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_5_7_na_na_ps&fm=SEARCH&iid=037d086e-0155-474c-9a15-e0bd9a7dfc5b.MOBG25PGC3KZKETA.SEARCH&ppt=sp&ppn=sp&ssid=l54jzsubcw0000001630853546203&qH=5a4c7323be568e72"
        },

        {
            "company": "Infinix",
            "model": "Note 10",
            "price": 12499,
            "ram": 6,
            "storage": 128,
            "camera": 48,
            "processor": "MediaTek Helio G85",
            "link": "https://www.flipkart.com/infinix-note-10-emerald-green-128-gb/p/itmd04ff59c20eee?pid=MOBG3KHEBF7PPT6Z&lid=LSTMOBG3KHEBF7PPT6ZM6OUMM&marketplace=FLIPKART&q=infinix+note+10&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&fm=SEARCH&iid=96c4de92-0272-4ccb-ba66-6f9a27e4b70d.MOBG3KHEBF7PPT6Z.SEARCH&ppt=sp&ppn=sp&ssid=hxrc0v5tow0000001630853568742&qH=4e1cf08277158024"
        },

        {
            "company": "Panasonic",
            "model": "Eluga I8",
            "price": 6999,
            "ram": 3,
            "storage": 32,
            "camera": 13,
            "processor": "Meditek",
            "link": "https://www.flipkart.com/panasonic-eluga-i8-charcoal-black-32-gb/p/itm83187d4b25e5f?pid=MOBFS3KXGFGYUZPE&lid=LSTMOBFS3KXGFGYUZPEAILZOH&marketplace=FLIPKART&q=panasonic+eluga+i8&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_4_15_sc_na_ps&otracker1=AS_Query_OrganicAutoSuggest_4_15_sc_na_ps&fm=SEARCH&iid=bdab8149-089e-4207-b368-1becae0e86ba.MOBFS3KXGFGYUZPE.SEARCH&ppt=sp&ppn=sp&ssid=j04vie60o00000001630853596520&qH=f1d655c2efa171f9"
        },

        {
            "company": "KARBONN ",
            "model": "X21",
            "price": 5099,
            "ram": 2,
            "storage": 32,
            "camera": 8,
            "processor": "Octa Core",
            "link": "https://www.flipkart.com/karbonn-x21-midnight-blue-32-gb/p/itmada259142426d?pid=MOBGFUZTXA64JFSD&lid=LSTMOBGFUZTXA64JFSDJM8CDU&marketplace=FLIPKART&q=karbonn+x21&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_5_7_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_5_7_na_na_ps&fm=SEARCH&iid=a2b20fda-5f21-47e8-badc-01e54e70e2a1.MOBGFUZTXA64JFSD.SEARCH&ppt=sp&ppn=sp&ssid=4u3b78u4s00000001630853626252&qH=c41e917b1f4b311e"
        },

        {
            "company": "vivo",
            "model": "Y20G 2021",
            "price": 13990,
            "ram": 4,
            "storage": 64,
            "camera": 13,
            "processor": "MediaTek Helio P35",
            "link": "https://www.flipkart.com/vivo-y20g-obsidian-black-128-gb/p/itm4f2cd46459e6c?pid=MOBFZX2GGSFM8SJW&lid=LSTMOBFZX2GGSFM8SJWQ6UTZU&marketplace=FLIPKART&q=vivo+y20g&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&fm=SEARCH&iid=544a17ca-5f6c-4c8b-a2da-26fc3e981a12.MOBFZX2GGSFM8SJW.SEARCH&ppt=sp&ppn=sp&ssid=szdwnz79r40000001630853665522&qH=b1dea16c6367d594"
        },

        {
            "company": "SAMSUNG",
            "model": "Galaxy F41",
            "price": 14499,
            "ram": 6,
            "storage": 128,
            "camera": 64,
            "processor": "Exynos 9611",
            "link": "https://www.flipkart.com/samsung-galaxy-f41-fusion-blue-128-gb/p/itm4769d0667cdf9?pid=MOBFV5PWG5MGD4CF&lid=LSTMOBFV5PWG5MGD4CFZ8YQJZ&marketplace=FLIPKART&q=samsung+f41&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&fm=SEARCH&iid=c97d2305-9398-48a4-83ca-1916ed6f7703.MOBFV5PWG5MGD4CF.SEARCH&ppt=sp&ppn=sp&ssid=nkg6yfrh680000001630853693853&qH=a167874541761adf"
        },

        {
            "company": "LG",
            "model": "W11",
            "price": 7665,
            "ram": 3,
            "storage": 32,
            "camera": 13,
            "processor": "MediaTek Helio P22",
            "link": "https://www.flipkart.com/lg-w11-black-32-gb/p/itm5025be1a3b0c1?pid=MOBG25V9GZMVQGZX&lid=LSTMOBG25V9GZMVQGZXUCBS55&marketplace=FLIPKART&q=lg+w11+mobile&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&fm=SEARCH&iid=59c5d4aa-3be7-4a4e-95bf-13bb4f874d55.MOBG25V9GZMVQGZX.SEARCH&ppt=sp&ppn=sp&ssid=bljea0simo0000001630861561540&qH=ee5d10dd1510651a"
        }
    ]
    return data

def earphones():
    data = [
        {
            "company": "boAt",
            "model": "Bassheads 103 Black Wired Headset",
            "color": " black",
            "connectivity": "wired",
            "price": 399,
            "link": "https://www.flipkart.com/boat-bassheads-103-black-wired-headset/p/itmcef2a10b6ea14?pid=ACCFGYHGGDCFYCA3&lid=LSTACCFGYHGGDCFYCA3NCS7JM&marketplace=FLIPKART&q=wired+earphones+&store=0pm%2Ffcn&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=1e2ae3a8-6839-47b9-a0c9-989615f923a5.ACCFGYHGGDCFYCA3.SEARCH&ppt=sp&ppn=sp&qH=51e9e47042cca958 "
        },
        {
            "company": "Sennheiser",
            "model": "CX 300s - Black Wired Headset",
            "color": "black",
            "connectivity": "wired",
            "price": 3490,
            "link": "https://www.flipkart.com/sennheiser-cx-300s-black-wired-headset/p/itmccc055aeb463e?pid=ACCFECFDHTYHCECR&lid=LSTACCFECFDHTYHCECRPMV3KY&marketplace=FLIPKART&q=wired+earphones+&store=0pm%2Ffcn&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=a7a0fd9b-fcd7-479f-bdef-afcdfb119ca3.ACCFECFDHTYHCECR.SEARCH&ppt=sp&ppn=sp&qH=51e9e47042cca958 "
        },
        {
            "company": "JBL",
            "model": "Endurance Run Wired Headset",
            "color": "black",
            "connectivity": "wired",
            "price": 1099,
            "link": "https://www.flipkart.com/jbl-endurance-run-wired-headset/p/itm2f2077e8276de?pid=ACCF8CF7GTNYUWK7&lid=LSTACCF8CF7GTNYUWK7FJBI2R&marketplace=FLIPKART&q=wired+earphones+&store=0pm%2Ffcn&srno=s_1_13&otracker=search&otracker1=search&fm=SEARCH&iid=a7a0fd9b-fcd7-479f-bdef-afcdfb119ca3.ACCF8CF7GTNYUWK7.SEARCH&ppt=sp&ppn=sp&qH=51e9e47042cca958"
        },
        {
            "company": "boAt",
            "model": " BassHeads 220 Wired Headset",
            "color": "black ",
            "connectivity": "wired",
            "price": 669,
            "link": "https://www.flipkart.com/jbl-c150si-wired-headset/p/itm5f6934af69fb7?pid=ACCEHDJBEJSQYYKU&lid=LSTACCEHDJBEJSQYYKUKRH1QM&marketplace=FLIPKART&q=wired+headphones&store=0pm%2Ffcn&srno=s_1_14&otracker=AS_Query_OrganicAutoSuggest_4_11_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_11_na_na_na&fm=SEARCH&iid=1c92c631-39c8-4ea4-a7ed-15c635ab6473.ACCEHDJBEJSQYYKU.SEARCH&ppt=sp&ppn=sp&ssid=hgrj1r3zy80000001630854870262&qH=fae9a029a61f58ad"
        },

        {
            "company": "OnePlus",
            "model": "Bullets Wireless Z Bass Edition Bluetooth Headset",
            "color": "blue",
            "connectivity": "bluetooth",
            "price": 1999,
            "link": "https://www.flipkart.com/oneplus-bullets-wireless-z-bass-bluetooth-headset/p/itm39349fc848c8a?pid=ACCFVA3KZVQWVTWG&lid=LSTACCFVA3KZVQWVTWGZO0TGS&marketplace=FLIPKART&srno=s_1_4&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&fm=SEARCH&iid=aebff04b-3474-4c11-9ff6-2f0614c944f6.ACCFVA3KZ2EYMYX3.SEARCH&ppt=sp&ppn=sp&ssid=h1wx6pp6bk0000001630855147925&qH=418696e663e903e6 "
        },
        {
            "company": "boAt",
            "model": "Rockerz 195 Bluetooth Headset",
            "color": "orange",
            "connectivity": "bluetooth",
            "price": 1049,
            "link": "https://www.flipkart.com/boat-rockerz-195-bluetooth-headset/p/itm6a85fd10addfe?pid=ACCFTV5K8XD2KSFG&lid=LSTACCFTV5K8XD2KSFGVSIV51&marketplace=FLIPKART&q=bluetooth+earphone&store=0pm%2Ffcn&srno=s_1_17&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&fm=SEARCH&iid=aebff04b-3474-4c11-9ff6-2f0614c944f6.ACCFTV5K8XD2KSFG.SEARCH&ppt=sp&ppn=sp&qH=418696e663e903e6"
        },
        {
            "company": "SONY",
            "model": "WI-SP510 Bluetooth Headset",
            "color": " blue",
            "connectivity": "bluetooth",
            "price": 4875,
            "link": "https://www.flipkart.com/sony-wi-sp510-bluetooth-headset/p/itm93bb3922bf1ad?pid=ACCFRKMPEHGYZX7Q&lid=LSTACCFRKMPEHGYZX7QFPYKTZ&marketplace=FLIPKART&q=bluetooth+earphone&store=0pm%2Ffcn&srno=s_1_30&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&fm=SEARCH&iid=f4cba6b2-f7d3-45f6-ba53-c88d9f16e6cd.ACCFRKMPEHGYZX7Q.SEARCH&ppt=sp&ppn=sp&qH=418696e663e903e6"
        },
        {
            "company": "Aroma",
            "model": "NB119C",
            "color": "black",
            "connectivity": "bluetooth",
            "price": 548,
            "link": "https://www.flipkart.com/aroma-nb119c-36-hours-playtime-neckband-bluetooth-headset/p/itm6de51daadac60?pid=ACCG3SMKXAUZTYH2&lid=LSTACCG3SMKXAUZTYH2KD8CLG&marketplace=FLIPKART&q=bluetooth+earphone&store=0pm%2Ffcn&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&fm=SEARCH&iid=en_vnW4aFQ45Rka41TXlJ%2Bx9x9PMQN0N%2BCWWsCUjveWwyRXGNAL%2BdOT2tm8kJ6LZsFlJ2%2FiFv%2FmnfNMrqUf0PBD3g%3D%3D&ppt=sp&ppn=sp&qH=418696e663e903e6"
        },

        {
            "company": "SONY",
            "model": " 310AP Wired Headset",
            "color": " red",
            "connectivity": "wired",
            "price": 849,
            "link": "https://www.flipkart.com/sony-310ap-wired-headset/p/itmc388e2c1ac7ce?pid=ACCDQZAU6GBRWYXD&lid=LSTACCDQZAU6GBRWYXD0TAETK&marketplace=FLIPKART&q=wired+headset&store=0pm%2Ffcn&srno=s_1_15&otracker=search&otracker1=search&fm=SEARCH&iid=3ad6e046-8577-4ce3-9e17-c86827d48ebb.ACCDQZAU6GBRWYXD.SEARCH&ppt=sp&ppn=sp&ssid=frljt1t9uo0000001630855634577&qH=ec8b366ba95c152f"
        },
        {
            "company": "Skullcandy",
            "model": "Riff Mic Wired Headset ",
            "color": "grey",
            "connectivity": "wired",
            "price": 2199,
            "link": "https://www.flipkart.com/skullcandy-riff-mic-wired-headset/p/itm7e3b8926bdd3c?pid=ACCFAJ8AU9E3N6UE&lid=LSTACCFAJ8AU9E3N6UEI0MDHD&marketplace=FLIPKART&q=skullcandy+riff&store=0pm%2Ffcn&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&fm=SEARCH&iid=a4aa7048-056b-4744-b2cb-af61909894dd.ACCFAJ8AU9E3N6UE.SEARCH&ppt=sp&ppn=sp&ssid=4sgh9xzots0000001630862224203&qH=fbee780e4af4657c"
        },
        {
            "company": "Sennheiser",
            "model": "HD 4.30i Wired ",
            "color": "whit",
            "connectivity": "wired ",
            "price": 7990,
            "link": "https://www.flipkart.com/sennheiser-hd-4-30i-wired-without-mic-headset/p/itmc7d73341fda29?pid=ACCES9QARNEJP7DV&lid=LSTACCES9QARNEJP7DV52M2GS&marketplace=FLIPKART&q=wired+headset&store=0pm%2Ffcn&srno=s_1_34&otracker=search&otracker1=search&fm=SEARCH&iid=8ff7b41d-9bd9-4148-b814-07a8904dc826.ACCES9QARNEJP7DV.SEARCH&ppt=sp&ppn=sp&qH=ec8b366ba95c152f"
        },
        {
            "company": "JBL",
            "model": " Quantum 300 Wired Gaming Headset",
            "color": "black",
            "connectivity": "wired",
            "price": 4699,
            "link": "https://www.flipkart.com/jbl-quantum-300-wired-gaming-headset/p/itm8be258f0c4ae6?pid=ACCFSKBYYSHUTJFM&lid=LSTACCFSKBYYSHUTJFM52NXC9&marketplace=FLIPKART&q=wired+headset&store=0pm%2Ffcn&srno=s_1_26&otracker=search&otracker1=search&fm=SEARCH&iid=a98af3c7-d692-4827-9568-0686986d7217.ACCFSKBYYSHUTJFM.SEARCH&ppt=sp&ppn=sp&qH=ec8b366ba95c152f"
        },

        {
            "company": "boAt",
            "model": "Airdopes 131 Bluetooth Headset ",
            "color": " midnight blue",
            "connectivity": "wireless",
            "price": 1283,
            "link": "https://www.flipkart.com/boat-airdopes-131-bluetooth-headset/p/itmf77ad6e8eecf1?pid=ACCFSDGX68PUKJYE&lid=LSTACCFSDGX68PUKJYEHF5WGJ&marketplace=FLIPKART&q=earbuds&store=0pm%2Ffcn&srno=s_1_5&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&fm=SEARCH&iid=dbc8561a-28a4-405d-8818-cf79543cf49f.ACCFSDGX68PUKJYE.SEARCH&ppt=sp&ppn=sp&ssid=p4qfixwrzk0000001630859778898&qH=2951f68ff1fee1e0"
        },
        {
            "company": "OnePlus",
            "model": "Buds Bluetooth Headset",
            "color": "nord blue",
            "connectivity": "wireless",
            "price": 4999,
            "link": "https://www.flipkart.com/oneplus-buds-bluetooth-headset/p/itm4b5b6de677c10?pid=ACCFTRN354PRDUUD&lid=LSTACCFTRN354PRDUUD3LDEGW&marketplace=FLIPKART&q=oneplus+earbuds&store=0pm%2Ffcn&srno=s_1_5&otracker=AS_Query_OrganicAutoSuggest_7_10_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_7_10_na_na_ps&fm=SEARCH&iid=9fdb7a05-1412-4acb-ab41-69f36ada4612.ACCFTRN354PRDUUD.SEARCH&ppt=sp&ppn=sp&ssid=6jtod8sohs0000001630859941044&qH=1236109085756208"
        },
        {
            "company": "CrossBeats",
            "model": "Urban Bluetooth Headset",
            "color": "dark blue",
            "connectivity": "wireless",
            "price": 3299,
            "link": " https://www.flipkart.com/crossbeats-urban-bluetooth-headset/p/itm34bc8706bcd79?pid=ACCFZAX5UJNEKEDY&lid=LSTACCFZAX5UJNEKEDYSHQDYN&marketplace=FLIPKART&q=oneplus+earbuds&store=0pm%2Ffcn&srno=s_1_19&otracker=AS_Query_OrganicAutoSuggest_7_10_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_7_10_na_na_ps&fm=SEARCH&iid=9fdb7a05-1412-4acb-ab41-69f36ada4612.ACCFZAX5UJNEKEDY.SEARCH&ppt=sp&ppn=sp&qH=1236109085756208"
        },
        {
            "company": "Sennheiser",
            "model": "CX 400BT Bluetooth Headset",
            "color": "black ",
            "connectivity": "wireless",
            "price": 13990,
            "link": "https://www.flipkart.com/sennheiser-cx-400bt-bluetooth-headset/p/itmd153293c3f3aa?pid=ACCFVGUUHFGJJHCK&lid=LSTACCFVGUUHFGJJHCKYZCPAO&marketplace=FLIPKART&q=senheiser+earbuds&store=0pm%2Ffcn&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=e33620de-43ff-4cea-95a9-2729be665958.ACCFVGUUHFGJJHCK.SEARCH&ppt=sp&ppn=sp&ssid=m47531cj6o0000001630860111431&qH=40833830a3216565"
        }
    ]
    return data

def television():
    data = [
        {
            'brand':'Redmi',
            'ram':8,
            'resolution':'ultra HD',
            'screensize':50,
            'warranty':1,
            'price':38999,
            'url':'https://www.amazon.in/Redmi-inches-Ultra-Android-L50M6-RA/dp/B08Y55LPBF/ref=sr_1_2_sspa?adgrpid=70930074921&dchild=1&ext_vrnc=hi&gclid=Cj0KCQjw1dGJBhD4ARIsANb6OdnSTBm2P990xdTGBSrP_a_srxKH4UqPXGzBRLeVYJZ82jTHm3ZpJLEaAidFEALw_wcB&hvadid=398133391406&hvdev=c&hvlocphy=9062067&hvnetw=g&hvqmt=b&hvrand=512175049298764710&hvtargid=kwd-296914595420&hydadcr=24571_1971437&keywords=amazon+in+tv&qid=1630856040&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRFRFQkZKMDE4VEFOJmVuY3J5cHRlZElkPUEwNDAxMzk3MVg1MFRVOVZSVEhGSiZlbmNyeXB0ZWRBZElkPUEwMTQ4NTc1MllNVlZWVzExMjlOWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
        },
        {
            'brand':'Philips',
            'ram':8,
            'resolution':'Ultra HD',
            'screensize':58,
            'warranty':2,
            'price':45999,
            'url':'https://www.amazon.in/Redmi-inches-Ultra-Android-L50M6-RA/dp/B08Y55LPBF/ref=sr_1_2_sspa?adgrpid=70930074921&dchild=1&ext_vrnc=hi&gclid=Cj0KCQjw1dGJBhD4ARIsANb6OdnSTBm2P990xdTGBSrP_a_srxKH4UqPXGzBRLeVYJZ82jTHm3ZpJLEaAidFEALw_wcB&hvadid=398133391406&hvdev=c&hvlocphy=9062067&hvnetw=g&hvqmt=b&hvrand=512175049298764710&hvtargid=kwd-296914595420&hydadcr=24571_1971437&keywords=amazon+in+tv&qid=1630856040&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRFRFQkZKMDE4VEFOJmVuY3J5cHRlZElkPUEwNDAxMzk3MVg1MFRVOVZSVEhGSiZlbmNyeXB0ZWRBZElkPUEwMTQ4NTc1MllNVlZWVzExMjlOWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
        },
        {
            'brand':'Samsung',
            'ram':8,
            'resolution':'ultra HD',
            'screensize':50,
            'warranty':1,
            'price':51990,
            'url':'https://www.amazon.in/dp/B08FD2VSD9/ref=syn_sd_onsite_desktop_19?psc=1&uh_it=f947bdd928dc3d01e34fa224f69a68e1_CT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFSNUpDUTZMU1VUNjcmZW5jcnlwdGVkSWQ9QTAwMjQxNjQyRlQ1WUpDSVdEWFRVJmVuY3J5cHRlZEFkSWQ9QTAzNzM2ODcyVk9RQUhTU1FEN1BCJndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
        },
        {
            'brand':'LG',
            'ram':8,
            'resolution':'Smart LED TV',
            'screensize':32,
            'warranty':1,
            'price':23990,
            'url':'https://www.amazon.in/LG-inches-Ready-Smart-32LM636BPTB/dp/B07VL2WB4M/ref=sr_1_3?dchild=1&keywords=lg+tv&qid=1630863008&sr=8-3'
        },
        {
            'brand':'TCL',
            'ram':8,
            'resolution':'Ultra HD',
            'screensize':43,
            'warranty':1,
            'price':31999,
            'url':'https://www.amazon.in/dp/B08FD2VSD9/ref=syn_sd_onsite_desktop_19?psc=1&uh_it=f947bdd928dc3d01e34fa224f69a68e1_CT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFSNUpDUTZMU1VUNjcmZW5jcnlwdGVkSWQ9QTAwMjQxNjQyRlQ1WUpDSVdEWFRVJmVuY3J5cHRlZEFkSWQ9QTAzNzM2ODcyVk9RQUhTU1FEN1BCJndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
        },
    ]
    return data

def refrigerator():
    data = [
        {
            'brand':'Whirlpool',
            'characteristics':'frost free multidoor',
            'capacity': 240,
            'price':28000,
            'url':'https://www.amazon.in/Whirlpool-Refrigerator-263D-PROTTON-ROY/dp/B07V3MHBFQ/ref=asc_df_B07V3MHBFQ/?tag=googleshopdes-21&linkCode=df0&hvadid=396988105878&hvpos=&hvnetw=g&hvrand=14636939683158145135&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062077&hvtargid=pla-818824351428&psc=1&ext_vrnc=hi'
        },
        {
            'brand':'Samsung',
            'characteristics':'direct cool single door',
            'capacity':255,
            'price':20390,
            'url':'https://www.amazon.in/Samsung-Inverter-Refrigerator-RR26T389YUT-HL/dp/B08346C9R4/ref=asc_df_B08346C9R4/?tag=googleshopdes-21&linkCode=df0&hvadid=397081752608&hvpos=&hvnetw=g&hvrand=14636939683158145135&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062077&hvtargid=pla-866037942915&psc=1&ext_vrnc=hi'
        },
        {
            'brand':'LG',
            'characteristics':'frost free side by side',
            'capacity':668,
            'price':105400,
            'url':'https://www.amazon.in/LG-Refrigerator-GC-L247CLAV-APZQEBN-Inverter-Compressor/dp/B079TWHM7F/ref=asc_df_B079TWHM7F/?tag=googleshopdes-21&linkCode=df0&hvadid=397081919471&hvpos=&hvnetw=g&hvrand=14636939683158145135&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062077&hvtargid=pla-489997113532&psc=1&ext_vrnc=hi'
        },
        {
            'brand':'Haier',
            'characteristics':'side by side with twin invertor technology',
            'capacity':565,
            'price':55991,
            'url':'https://www.amazon.in/Haier-Inverter-Frost-Free-Refrigerator-HRF-619SS/dp/B07RWJMQTX/ref=asc_df_B07RWJMQTX/?tag=googleshopdes-21&linkCode=df0&hvadid=396988105878&hvpos=&hvnetw=g&hvrand=14636939683158145135&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062077&hvtargid=pla-786272575918&psc=1&ext_vrnc=hi'
        },
        {
            'brand':'Godrej',
            'characteristics':'frost free double door',
            'capacity':236,
            'price':19990,
            'url':'https://www.flipkart.com/godrej-236-l-frost-free-double-door-2-star-refrigerator/p/itm4e9b9dbde460e?pid=RFRFZCW3W7S3CTZP&lid=LSTRFRFZCW3W7S3CTZP1CDPJY&marketplace=FLIPKART&cmpid=content_refrigerator-new_8965229628_gmc'
        },
    ]
    
    return data
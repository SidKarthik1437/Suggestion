from pprint import pprint

data={
    'tv':[
        {
            'Brand':'Redmi',
            'RAM':8,
            'Resolution':'ultra HD',
            'Screen size inches':50,
            'Warranty':1,
            'Price':38999,
            'Url':'https://www.amazon.in/Redmi-inches-Ultra-Android-L50M6-RA/dp/B08Y55LPBF/ref=sr_1_2_sspa?adgrpid=70930074921&dchild=1&ext_vrnc=hi&gclid=Cj0KCQjw1dGJBhD4ARIsANb6OdnSTBm2P990xdTGBSrP_a_srxKH4UqPXGzBRLeVYJZ82jTHm3ZpJLEaAidFEALw_wcB&hvadid=398133391406&hvdev=c&hvlocphy=9062067&hvnetw=g&hvqmt=b&hvrand=512175049298764710&hvtargid=kwd-296914595420&hydadcr=24571_1971437&keywords=amazon+in+tv&qid=1630856040&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRFRFQkZKMDE4VEFOJmVuY3J5cHRlZElkPUEwNDAxMzk3MVg1MFRVOVZSVEhGSiZlbmNyeXB0ZWRBZElkPUEwMTQ4NTc1MllNVlZWVzExMjlOWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
        },
        {
            'Brand':'Philips',
            'RAM':8,
            'Resolution':'Ultra HD',
            'Screen size inches':58,
            'Warranty':2,
            'Price':45999,
            'Url':'https://www.amazon.in/Redmi-inches-Ultra-Android-L50M6-RA/dp/B08Y55LPBF/ref=sr_1_2_sspa?adgrpid=70930074921&dchild=1&ext_vrnc=hi&gclid=Cj0KCQjw1dGJBhD4ARIsANb6OdnSTBm2P990xdTGBSrP_a_srxKH4UqPXGzBRLeVYJZ82jTHm3ZpJLEaAidFEALw_wcB&hvadid=398133391406&hvdev=c&hvlocphy=9062067&hvnetw=g&hvqmt=b&hvrand=512175049298764710&hvtargid=kwd-296914595420&hydadcr=24571_1971437&keywords=amazon+in+tv&qid=1630856040&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRFRFQkZKMDE4VEFOJmVuY3J5cHRlZElkPUEwNDAxMzk3MVg1MFRVOVZSVEhGSiZlbmNyeXB0ZWRBZElkPUEwMTQ4NTc1MllNVlZWVzExMjlOWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
        },
        {
            'Brand':'Samsung',
            'RAM':8,
            'Resolution':'ultra HD',
            'Screen size inches':50,
            'Warranty':1,
            'Price':51990,
            'Url':'https://www.amazon.in/dp/B08FD2VSD9/ref=syn_sd_onsite_desktop_19?psc=1&uh_it=f947bdd928dc3d01e34fa224f69a68e1_CT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFSNUpDUTZMU1VUNjcmZW5jcnlwdGVkSWQ9QTAwMjQxNjQyRlQ1WUpDSVdEWFRVJmVuY3J5cHRlZEFkSWQ9QTAzNzM2ODcyVk9RQUhTU1FEN1BCJndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
        },
        {
            'Brand':'LG',
            'RAM':8,
            'Resolution':'Smart LED TV',
            'Screen size inches':32,
            'Warranty':1,
            'Price':23990,
            'Url':'https://www.amazon.in/LG-inches-Ready-Smart-32LM636BPTB/dp/B07VL2WB4M/ref=sr_1_3?dchild=1&keywords=lg+tv&qid=1630863008&sr=8-3'
        },
        {   
            'Brand':'TCL',
            'RAM':8,
            'Resolution':'Ultra HD',
            'Screen size inches':43,
            'Warranty':1,
            'Price':31999,
            'Url':'https://www.amazon.in/dp/B08FD2VSD9/ref=syn_sd_onsite_desktop_19?psc=1&uh_it=f947bdd928dc3d01e34fa224f69a68e1_CT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFSNUpDUTZMU1VUNjcmZW5jcnlwdGVkSWQ9QTAwMjQxNjQyRlQ1WUpDSVdEWFRVJmVuY3J5cHRlZEFkSWQ9QTAzNzM2ODcyVk9RQUhTU1FEN1BCJndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
        },
    ],
    "Refrigerator":[
        {
            'Brand':'Whirlpool',
            'Characteristics':'frost free multidoor',
            'Capacity': 240,
            'Price':28000,
            'Url':'https://www.amazon.in/Whirlpool-Refrigerator-263D-PROTTON-ROY/dp/B07V3MHBFQ/ref=asc_df_B07V3MHBFQ/?tag=googleshopdes-21&linkCode=df0&hvadid=396988105878&hvpos=&hvnetw=g&hvrand=14636939683158145135&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062077&hvtargid=pla-818824351428&psc=1&ext_vrnc=hi'
        },
        {
            'Brand':'Samsung',
            'Characteristics':'direct cool single door',
            'Capacity':255,
            'Price':20390,
            'Url':'https://www.amazon.in/Samsung-Inverter-Refrigerator-RR26T389YUT-HL/dp/B08346C9R4/ref=asc_df_B08346C9R4/?tag=googleshopdes-21&linkCode=df0&hvadid=397081752608&hvpos=&hvnetw=g&hvrand=14636939683158145135&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062077&hvtargid=pla-866037942915&psc=1&ext_vrnc=hi'
        },
        {
            'Brand':'LG',
            'Characteristics':'frost free side by side',
            'Capacity':668,
            'Price':105400,
            'Url':'https://www.amazon.in/LG-Refrigerator-GC-L247CLAV-APZQEBN-Inverter-Compressor/dp/B079TWHM7F/ref=asc_df_B079TWHM7F/?tag=googleshopdes-21&linkCode=df0&hvadid=397081919471&hvpos=&hvnetw=g&hvrand=14636939683158145135&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062077&hvtargid=pla-489997113532&psc=1&ext_vrnc=hi'
        },
        {
            'Brand':'Haier',
            'Characteristics':'side by side with twin invertor technology',
            'Capacity':565,
            'Price':55991,
            'Url':'https://www.amazon.in/Haier-Inverter-Frost-Free-Refrigerator-HRF-619SS/dp/B07RWJMQTX/ref=asc_df_B07RWJMQTX/?tag=googleshopdes-21&linkCode=df0&hvadid=396988105878&hvpos=&hvnetw=g&hvrand=14636939683158145135&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062077&hvtargid=pla-786272575918&psc=1&ext_vrnc=hi'
        },
        {
            'Brand':'Godrej',
            'Characteristics':'frost free double door',
            'Capacity':236,
            'Price':19990,
            'Url':'https://www.flipkart.com/godrej-236-l-frost-free-double-door-2-star-refrigerator/p/itm4e9b9dbde460e?pid=RFRFZCW3W7S3CTZP&lid=LSTRFRFZCW3W7S3CTZP1CDPJY&marketplace=FLIPKART&cmpid=content_refrigerator-new_8965229628_gmc'
        },
    ]
}   
print("Hello User!! please mention what you need from our catalouge:")
for item in data.keys():
    print(item)
user_product = input("enter the product:")
product_characteristics = data[user_product] 

print("Here's the list of available items")
for item in product_chracteristics: 
    print("Brand:",item['brand'] + '\t','\t', "Characteristics:",
    item['characteristics'] + '\t', "Capacity:", str(item['capacity']) ,
    'liters' + '\t', "Price:", str(item['price']) + 
    'rupees' + '\t' + "Url:" + item(['url']) 

user_characteristics = input("Enter" + user_product + "characteristics: ")
user_brand = input("Enter " + user_product + " brand: ")

for item in product_characteristics: 
    if item['characteristics'] == user_characteristics and item['brand'] == user_brand:
        pprint(item)
     



        



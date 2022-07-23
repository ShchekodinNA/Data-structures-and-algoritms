def scream():
    print("ahh!")

user = {
    "age": 54,
    'name':'Kylie',
    'magic': True,
    'scream': scream
}

user["scream"]()        # O(1)
user['spell'] = 'abra kadabra'  # access = O(1)
print(user['spell'])
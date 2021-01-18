name = ('Arbaaz khan', 'Naveed', 'Rohit')
company = ('Apple', 'Dell', 'Lenovo')
zipped = zip(name, company)
print(zipped)   # <zip object at 0x000002130CF75CC0>
# print(list(zipped))     # [('Arbaaz khan', 'Apple'), ('Naveed', 'Dell'), ('Rohit', 'Lenovo')]
# print(dict(zipped))     # {'Arbaaz khan': 'Apple', 'Naveed': 'Dell', 'Rohit': 'Lenovo'}

for a,b in zipped:
    print(f'{a}: {b}')

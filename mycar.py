mycar = {
    "brand":"Renault",
    "model":"Triber",
    "year":2022,
    "color":"Monlight Silver",
    "seatcount":7
}

print(f'I have {mycar["brand"]} {mycar["model"]} {mycar["year"]} with {mycar["color"]} color {mycar["seatcount"]} seater car')

cars = {
    "brand":"Renault",
    "model":"Triber",
    "year":2022,
    "color":"Monlight Silver",
    "seatcount":7
}

for car in cars:
    print(f"{cars[car]}")
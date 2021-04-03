d1 = {
    "dish": "Mixed Salad",
    "price": 2.11
}

d2 = {
    "dish": "French Fries",
    "price": 2.89
}

d3 = {
    "dish": "Side Salad",
    "price": 3.49
}

d4 = {
    "dish": "Hot Wings",
    "price": 3.70
}

d5 = {
    "dish": "Mozzarella Sticks",
    "price": 4.59
}

d6 = {
    "dish": "Sampler Plate",
    "price": 5.99
}

counter = 0

while counter < 16.28:

    if counter < 16.28 - d6["price"]:
        counter = counter + d6["price"]
        print(counter)
    elif counter < 16.28 -d5["price"]:
        counter = counter + d5["price"]
        print(counter)
    elif counter < 16.28 -d4["price"]:
        counter = counter + d4["price"]
        print(counter)
    elif counter < 16.28 -d3["price"]:
        counter = counter + d3["price"]
        print(counter)
    elif counter < 16.28 -d2["price"]:
        counter = counter + d2["price"]
        print(counter)
    elif counter < 16.28 -d1["price"]:
        counter = counter + d1["price"]
        print(counter)
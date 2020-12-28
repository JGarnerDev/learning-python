def get_drink_by_profession(param):
    drinks = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politican": "Your tax dollars",
        "rapper": "Cristal"
    }
    param = param.lower()
    return drinks.get(param, "Beer")


print(get_drink_by_profession("JABRONI"))
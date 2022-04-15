STOCK = [
            {
                "id":0,
                "name":"healing potion",
                "qty": 5,
                "price": 200
            },
            {
                "id":1,
                "name":"speed potion",
                "qty": 2,
                "price": 500
            },
            {
                "id":2,
                "name":"polymorph potion",
                "qty": 1,
                "price": 5000
            }
]

def getAllPotions():
    return STOCK

def getPotionById(id):
    for potion in STOCK:
        if potion['id'] == id:
            return potion
    return None



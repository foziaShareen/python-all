class Inventory:
    def __init__(self, name, stock, p_price, s_price, expiry, category):
        self.name = name
        self.stock = stock
        self.p_price = p_price
        self.s_price = s_price
        self.expiry = expiry
        self.category = category


def input_fun():
    name = ""
    with open("record.txt", "a") as f:
        while name != "m":
            name = input("enter product name or m for main menu:  ")
            if name != "m":
                stock = input("enter " + name + " stock: ")
                p_price = input("enter " + name + " purchasing price: ")
                s_price = input("enter " + name + " sale price: ")
                expiry = input("enter " + name + " expiry date: ")
                category = input("enter " + name + "  category: ")
                object = Inventory(name, stock, p_price, s_price, expiry, category)
                f.write(object)
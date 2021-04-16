class Product:
    productID = 0
    product_catalog = {}

    def __init__(self, name, count):
        self.id = Product.productID
        Product.productID += 1
        self.name = name
        self.count = count
        self.items = []
        for _ in range(count):
            self.items.append(Item(self.id).id)

    def getInfo(self):
        itemsString = str(self.items)
        return "name : {name}, count: {count}, items: {items}".format(name = str(self.name), count= str(self.count), items=itemsString)

    @classmethod
    def add_product(cls, pName, pCount):
        newProduct = Product(pName, pCount)
        cls.product_catalog[newProduct.id] = newProduct

    @classmethod
    def send_out(cls, products):
        counter = {}
        for p in products:
            if p not in counter:
                counter[p] = 1
            else:
                counter[p] += 1
        enough = True
        for p, count in counter.items():
            if p not in cls.product_catalog or cls.product_catalog[p].count < count:
                enough = False
                print("Not enough "+ cls.product_catalog[p].name + " in the warehouse")
        if enough:
            for p, count in counter.items():
                for _ in range(count):
                    cls.product_catalog[p].items.pop(0)
                    cls.product_catalog[p].count -= 1
            print("Requested products sent out successfully! ")

class Item:
    itemId = 100

    def __init__(self, pId):
        self.id = Item.itemId
        Item.itemId += 1
        self.productID = pId



Product.add_product("table", 3)
Product.add_product("chair", 2)
Product.add_product("bed", 5)
for k,v in Product.product_catalog.items():
    print(k,v.getInfo())
outList = [0,1,2,0,2]
Product.send_out(outList)
for k,v in Product.product_catalog.items():
    print(k,v.getInfo())

class Product:
    product_catalog ={}
    product_id = 0

    def __init__(self, name, count):
        self.id = Product.product_id
        Product.product_id += 1
        self.name = name
        self.count = count
        self.items = []
        for _ in range(count):
            self.items.append(Item(self.id).id)

    @classmethod
    def add_product(cls,name, count):
        newProduct = Product(name,count)
        Product.product_catalog[newProduct.id] = newProduct

    def toString(self):
        itemsString = str(self.items)
        return "id: {id}, name: {name}, count: {count}, items:{items}".format(id=self.id, name=self.name, count=self.count, items = itemsString)

    @classmethod
    def sentOut(cls, outlist):
        counter = {}
        for p in outlist:
            if p in counter:
                counter[p] += 1
            else:
                counter[p] = 1
        enough = True
        for p, count in counter.items():
            if p not in Product.product_catalog or count>Product.product_catalog[p].count:
                enough = False
                print(Product.product_catalog[p].name, " is not enough. Sent out fail!")
        if enough:
            for p, count in counter.items():
                for _ in range(count):
                    Product.product_catalog[p].items.pop(0)
                Product.product_catalog[p].count -= count
            print("sent out success!")
class Item:
    item_id = 100

    def __init__(self, product_id):
        self.id = Item.item_id
        Item.item_id += 1
        self.productId = product_id



Product.add_product("table",2)
Product.add_product("chair",3)
for k,v in Product.product_catalog.items():
    print(k, v.toString())

outlist = [0,0,1,1,]
Product.sentOut(outlist)
for k,v in Product.product_catalog.items():
    print(k, v.toString())


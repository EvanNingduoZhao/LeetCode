# 这题实际上就是business logic，注意要把discount这个2d array先转化成一个dict
def findLowestPrice(products,discounts):
    n = len(products)
    m = len(products[0])
    minTotal = 0
    discountDict = {}
    for d in discounts:
        discountDict[d[0]]=[d[1],d[2]]
    for p in products:
        labelPrice = float(p[0])
        minPrice = float("inf")
        for i in range(1,m):
            if p[i]!= "EMPTY":
                discountType = discountDict[p[i]][0]
                discountDetail = discountDict[p[i]][1]
                if discountType == '0':
                    minPrice = min(minPrice, round(float(discountDetail)))
                elif discountType == '1':
                    minPrice = min(minPrice, round((1-float(discountDetail)/100)*labelPrice))
                else:
                    minPrice = min(minPrice,round(labelPrice-discountDetail))
        minTotal+=minPrice
    return minTotal

products = [['10', 'sale', 'january-sale'], ['200', 'sale', 'EMPTY']]
discounts = [['sale','0','10'],['january-sale','1','10']]
print(findLowestPrice(products,discounts))
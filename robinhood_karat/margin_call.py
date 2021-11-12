def margin_call(trades):
    cash = 1000
    stocks={}
    for trade in trades:
        timestamp,symbol,type,quantity,price = trade
        if type=="B":
            cash-=int(quantity)*int(price)
            if symbol in stocks:
                stocks[symbol]+=int(quantity)
            else:
                stocks[symbol]=int(quantity)
        else:
            cash += int(quantity) * int(price)
            stocks[symbol] -= int(quantity)
    res = []
    for stock, count in stocks.items():
        record = [stock,str(count)]
        res.append(record)
    sorted(res, key=lambda x: x[0])
    res.insert(0,["CASH",str(cash)])
    return res


def margin_call2(trades):
    cash = 1000
    stocks={}
    for trade in trades:
        timestamp,symbol,type,quantity,price = trade
        if type=="B":
            if cash>=int(quantity)*int(price):
                cash-=int(quantity)*int(price)
            else:
                shareCanBuy = cash//int(price)
                cash = cash%int(price)
                deficit = (int(quantity)-shareCanBuy)*int(price)
                stocks,cash = sell_to_fill_deficit(stocks,cash,deficit)
            if symbol in stocks:
                stocks[symbol][0] += int(quantity)
                stocks[symbol][1] = int(price)
            else:
                stocks[symbol] = [int(quantity), price]

        else:
            cash += int(quantity) * int(price)
            stocks[symbol][0] -= int(quantity)
            stocks[symbol][1] = int(price)
    res = []
    for stock, count in stocks.items():
        record = [stock,str(count)]
        res.append(record)
    sorted(res, key=lambda x: x[0])
    res.insert(0,["CASH",str(cash)])
    return res



def sell_to_fill_deficit(stocks,cash,deficit):
    stockList=[]
    for key,value in stocks.items():
        record = [key,value[0],value[1]]
        stockList.append(record)
    stockList.sort(key=lambda x:(x[2],x[0]))
    while deficit>0:
        # print(stockList)
        _, quantity, price = stockList[0]
        if quantity*price <= deficit:
            stockList.pop(0)
            deficit-=quantity*price
        else:
            demandQuantity = deficit//price+1
            cash += demandQuantity*price-deficit
            stockList[0][1]-=demandQuantity
            deficit = 0
    newStocksDict = {}
    for symbol, quantity, price in stockList:
        newStocksDict[symbol]=[quantity,price]
    return newStocksDict, cash

def sell_to_fill_deficit3(stocks,cash,deficit):
    stockList=[]
    collateral = {}
    for key,value in stocks.items():
        if key[-1]!="O":
            if key+"O" in stocks:
                if value[0]>stocks[key+"O"]:
                    record = [key, value[0]-stocks[key+"O"],value[1]]
                    stockList.append(record)
                    continue
                else:
                    continue
        record = [key,value[0],value[1]]
        stockList.append(record)
    stockList.sort(key=lambda x:(x[2],x[0]))
    while deficit>0:
        # print(stockList)
        _, quantity, price = stockList[0]
        if quantity*price <= deficit:
            stockList.pop(0)
            deficit-=quantity*price
        else:
            demandQuantity = deficit//price+1
            cash += demandQuantity*price-deficit
            stockList[0][1]-=demandQuantity
            deficit = 0
    newStocksDict = {}
    for symbol, quantity, price in stockList:
        newStocksDict[symbol]=[quantity,price]
    return newStocksDict, cash


trades= [["1", "AAPL", "B", "10", "10"], ["3", "GOOG", "B", "20", "5"], ["10", "AAPL", "S", "5", "15"]]
print(margin_call(trades))

trades2=[["1", "AAPL", "B", "10", "100"],["2", "AAPL", "S", "2", "80"],["3", "GOOG", "B", "15", "20"]]
print(margin_call2(trades2))
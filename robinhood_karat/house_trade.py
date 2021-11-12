def getUnmatchedOrders(houseTrades,streetTrades):
    hTradesDict = {}
    sTradesDict = {}
    # transform houseTrades and streetTrades into maps
    # key is symbol,quantity value is the origianl string
    for trade in houseTrades:
        symbol,side,quantity,id = trade.split(",")
        key = symbol+","+quantity
        if key not in hTradesDict:
            hTradesDict[key]=[trade]
        else:
            hTradesDict[key].append(trade)
    for trade in streetTrades:
        symbol, side, quantity, id = trade.split(",")
        key = symbol + "," + quantity
        if key not in sTradesDict:
            sTradesDict[key] = [trade]
        else:
            sTradesDict[key].append(trade)

    removeMatches(hTradesDict, sTradesDict, "Exact")
    removeMatches(hTradesDict, sTradesDict, "Attribute")
    removeMatches(hTradesDict, sTradesDict, "Offset")
    print(hTradesDict)
    print(sTradesDict)
    unmatchedOrders = []
    for key, value in hTradesDict.items():
        for v in value:
            unmatchedOrders.append(v)
    for key, value in sTradesDict.items():
        for v in value:
            unmatchedOrders.append(v)
    unmatchedOrders.sort()
    return unmatchedOrders

def removeMatches(hTradesDict,sTradesDict,type):
    # since remove offset is within homeTrades or within streetTrades
    # so we treat offset seperately
    if type=="Offset":
        removeOffset(hTradesDict)
        removeOffset(sTradesDict)
    else:
        for key in hTradesDict.keys():
            if key in sTradesDict:
                hPotentialMatches = hTradesDict[key]
                sPotentialMatches = sTradesDict[key]
                hPotentialMatches.sort()
                sPotentialMatches.sort()
                sRemoveIndex=set()
                hRemoveIndex=set()
                for h in range(len(hPotentialMatches)):
                    for s in range(len(sPotentialMatches)):
                        if s not in sRemoveIndex:
                            if type=="Exact":
                                if hPotentialMatches[h]==sPotentialMatches[s]:
                                    hRemoveIndex.add(h)
                                    sRemoveIndex.add(s)
                                    break
                            elif type == "Attribute":
                                hSide = hPotentialMatches[h].split(",")[1]
                                sSide = sPotentialMatches[h].split(",")[1]
                                if hSide == sSide:
                                    hRemoveIndex.add(h)
                                    sRemoveIndex.add(s)
                                    break
                hTradesDict[key] = removeElements(hTradesDict[key], hRemoveIndex)
                sTradesDict[key] = removeElements(sTradesDict[key], sRemoveIndex)

def removeOffset(TradesDict):
    for key, value in TradesDict.items():
        if len(value) >= 2:
            RemoveIndex = set()
            value.sort()
            for i in range(len(value)):
                for j in range(i + 1, len(value)):
                    if i not in RemoveIndex and j not in RemoveIndex:
                        if value[i].split(",")[1] != value[j].split(",")[1]:
                            RemoveIndex.add(i)
                            RemoveIndex.add(j)
            TradesDict[key] = removeElements(TradesDict[key],RemoveIndex)

def removeElements(list,removeIndex):
    newList = []
    for i in range(len(list)):
        if i not in removeIndex:
            newList.append(list[i])
    return newList

houseTrades1=["AAPL,B,0100,ABC123", "AAPL,B,0100,ABC123", "GOOG,S,0050,CDC333"]
streetTrades1= [" FB,B,0100,GBGGGG", "AAPL,B,0100,ABC123"]
print("Test case 0: ",getUnmatchedOrders(houseTrades1,streetTrades1))
houseTrades2=["AAPL,B,0100,ABC123","GOOG,S,0050,CDC333"]
streetTrades2 = ["  FB,B,0100,GBGGGG", "AAPL,B,0100,ABC123"]
print("Test case 1: ",getUnmatchedOrders(houseTrades2,streetTrades2))
houseTrades3=["AAPL,S,0010,ZYX444",
            "AAPL,S,0010,ZYX444",
            "AAPL,B,0010,ABC123",
            "GOOG,S,0050,GHG545"]
streetTrades3=["GOOG,S,0050,GHG545",
            "AAPL,S,0010,ZYX444",
            "AAPL,B,0010,TTT222"]
print("Test case 2: ",getUnmatchedOrders(houseTrades3,streetTrades3))
houseTrades4=["AAPL,B,0010,ABC123",
            "AAPL,S,0015,ZYX444",
            "AAPL,S,0015,ZYX444",
            "GOOG,S,0050,GHG545"]
streetTrades4=["GOOG,S,0050,GHG545",
            "AAPL,S,0015,ZYX444",
            "AAPL,B,0500,TTT222"]
print("Test case 3: ", getUnmatchedOrders(houseTrades4,streetTrades4))
houseTrades5=["AAPL,B,0100,ABC123",
            "AAPL,B,0100,ABC123",
            "AAPL,B,0100,ABC123",
            "GOOG,S,0050,CDC333"]
streetTrades5=["  FB,B,0100,GBGGGG",
            "AAPL,B,0100,ABC123",
            "AAPL,B,0100,ABC123",
            "GOOG,S,0050,CDC333"]
print("Test case 4: ",getUnmatchedOrders(houseTrades5, streetTrades5))
houseTrades6=["AAPL,S,0100,ABC123",
            "AAPL,B,0100,ABC123",
            "AAPL,B,0100,ABC123",
            "GOOG,S,0050,CDC333"]
streetTrades6=[ "FB,B,0100,GBGGGG",
            "AAPL,B,0100,ABC123",
            "AAPL,B,0100,ABC123",
            "GOOG,S,0050,CDC333",
            "AAPL,S,0100,ABC124",
            "AAPL,B,0100,ABC125"]
print("Test case 5:", getUnmatchedOrders(houseTrades6,streetTrades6))
houseTrades7=["AAPL,B,0010,ABC123",
            "AAPL,S,0015,ZYX444",
            "AAPL,S,0015,ZYX444",
            "AAPL,S,0015,ZYX444",
            "AAPL,S,0015,ZYX444",
            "AAPL,S,0015,ZYX444",
            "GOOG,S,0050,GHG545"]
streetTrades7=["GOOG,S,0050,GHG545",
            "AAPL,S,0015,ZYX444",
            "AAPL,S,0015,ZYX444",
            "AAPL,S,0015,ZYX444",
            "AAPL,S,0015,ZYX444",
            "AAPL,B,0500,TTT222"]
print("Test case 6:", getUnmatchedOrders(houseTrades7,streetTrades7))


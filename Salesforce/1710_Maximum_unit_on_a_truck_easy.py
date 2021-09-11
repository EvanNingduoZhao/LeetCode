# Question:
# You are assigned to put some amount of boxes onto one truck.
# You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that
# can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes
# does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.

# 这题很简单，因为我们要最大化卡车里装下的unit的数量，那就就要优先装一个box里units数量最多的box的type
# 所以首先给boxType根据一个box里可以装的unit数量sort
# 直到最后卡车装不下当前type的所有box，那么就卡车还能装几个box就把当前type的box放上去几个
def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(reverse=True, key=lambda x: x[1])
    boxes = 0
    units = 0
    lastTypeToFill = None
    for type in boxTypes:
        if boxes + type[0] <= truckSize:
            boxes += type[0]
            units += type[1] * type[0]
        else:
            lastTypeToFill = type
            break
    if lastTypeToFill:
        units += (truckSize - boxes) * lastTypeToFill[1]
    return units

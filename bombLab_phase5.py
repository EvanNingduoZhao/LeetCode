import random
import itertools
bigList=[2,10,6,1,12,0,9,3,4,7,14,5,11,8,15,13]
count=0
permutes=list(itertools.permutations(bigList,6))
print(len(permutes))
for smallList in permutes:
    count+=1
    print(smallList)
    print("we have seen: ",count)
    base = 0
    for i in smallList:
        base*=16
        base+=i
    print(base)
    if base == 11590595:
        print("The ultimate Answer is: ", smallList)
        break
# while True:
#     smallList=random.sample(bigList, 6)
#     if str(smallList) not in seen:
#         seen.add(str(smallList))
#         count+=1
#         print(smallList)
#         print("we have seen: ",count)
#         base = 0
#         for i in smallList:
#             base*=16
#             base+=i
#         print(base)
#         if base == 11590595:
#             print("The ultimate Answer is: ", smallList)
#             break
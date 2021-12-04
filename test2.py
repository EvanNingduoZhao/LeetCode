# def fibonacci(n):
#     res =0
#     if n == 0:
#         res = 0
#     elif n == 1 or n == 2:
#         res = 1
#     else:
#         prev1 = 1
#         prev2 = 1
#         num = 0
#         for _ in range(3, n + 1):
#             num = prev1 + prev2
#             prev2 = prev1
#             prev1 = num
#         res = num
#     return res
#
# print(fibonacci(1))

# import ipaddress
# print("hello")
# cidrSig = '172.10.242.81/12'
# rangeAddr = ipaddress.IPv4Network(cidrSig,False)
# leadindBits = int(cidrSig.split("/")[1])
# addressCount = pow(2,32-leadindBits)
# print(addressCount)
# print(str(rangeAddr[0]))
# print(rangeAddr[-1])
# # for addr in rangeAddr:
#     print(rangeAddr)
# rangeAddr = [str(ip) for ip in ipaddress.IPv4Network('192.0.2.0/28',False)]
# print(len(rangeAddr))
# print(rangeAddr[0])
# print(rangeAddr[-1])
#

# n=4
# m=3
# dp =[[[0,0,0,0] for j in range(n)] for i in range(m)]
# print(dp)
# count = 0
# for i in range(m):
#     # print(dp[i])
#     for j in range(n):
#         # print(dp[i][j])
#         for k in range(4):
#             count+=1
#             dp[i][j][k]+=1
#             print("i",i)
#             print("j",j)
#             print("k",k)
#             print(dp)
#             print(count)
# print([0]*4)
# dp2 = [[0,]]
# for i in range(n):
#     for j in range(4):
#         dp2[i][j]+=1
#         print(dp2)

for j in xrange(10):
    print(j)
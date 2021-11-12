def split_integer(num):
    stringNum = str(num)
    n = len(stringNum)
    if n%2 == 0:
        first = stringNum[:int(n/2)]
        second = stringNum[int(n/2):]
        first, second = trim_zeros(first,second)
        print("first is:",first)
        print("second is:",second)
        return abs(first-second)
    else:
        first_1 = stringNum[:int(n // 2)]
        second_1 = stringNum[int(n // 2):]
        first_1, second_1 = trim_zeros(first_1,second_1)
        first_2 = stringNum[:int(n // 2+1)]
        second_2 = stringNum[int(n // 2+1):]
        first_2, second_2 = trim_zeros(first_2, second_2)
        print("first_1 is:", first_1)
        print("second_1 is:", second_1)
        print("first_2 is:", first_2)
        print("second_2 is:", second_2)
        return min(abs(first_1-second_1),abs(first_2-second_2))


def trim_zeros(first,second):
    while len(first)>1 and first[-1] == '0':
        first = first[:-1]
    while len(second)>1 and second[0] == '0':
        second = second[1:]
    return int(first),int(second)

print(split_integer(7007))
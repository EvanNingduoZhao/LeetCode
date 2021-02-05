# 这道题的精髓就是要用一个stack
def bobAlice(arr):
    winner='Bob'
    stack=[arr[0]]
    print(arr)
    for i in range(1,len(arr)):
        if stack and arr[i] == stack[-1]:
            winner=switchWinner(winner)
            # print('winner',winner)
            stack.pop()
        else:
            stack.append(arr[i])

    return winner

def switchWinner(winner):
    if winner == 'Bob':
        return 'Alice'
    else:
        return 'Bob'

arr=[1,2,2,3,3,1,1]
print(bobAlice(arr))
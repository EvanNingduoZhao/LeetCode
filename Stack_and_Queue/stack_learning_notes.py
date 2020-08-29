class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("stack is empty")

    def get_stack(self):
        return self.items

s = Stack()
s.push("A")
s.push("B")
print(s.get_stack())
s.push("C")
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.is_empty())
print(s.peek())


# an easy stack project to check is a parenthesis string is balanced
def paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    i = 0
    while i<len(paren_string) and is_balanced == True:
        if paren_string[i] in '([{':
            s.push(paren_string[i])
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if match(top,paren_string[i]) == False:
                    is_balanced = False
        i+=1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

def match(p1,p2):
    if p1 =='{' and p2 == '}':
        return True
    elif p1 =='[' and p2 == ']':
        return True
    elif p1 =='(' and p2 == ')':
        return True
    else:
        return False

print(paren_balanced('{{{{{{{}}}}}}]'))
print((10-5)^2)
#Author: Wyatt Avilla
#Date: 11/12/22
#File: Uses tree and stack ADTs to calculate arithmetic expressions based on user input


from stack import Stack
from tree import BinaryTree
from tree import ExpTree

def balanced(inp):    # checks if given expression is balanced
    parstack = Stack()
    for char in inp:
        if char == "(":
            parstack.push(char)
        if char == ")":
            if parstack.isEmpty():
                return False
            parstack.pop()
    if parstack.isEmpty():
        return True
    else:
        return False

def seperate(inp):
    output = []
    operators = ["*", "/", "+", "-", "(", ")", "^"]
    count = 0
    for x in inp:
        if count >= len(inp):
            output.append(float(inp))
            count = 0
            break
        if inp[count] in operators:
            if count > 0:
                output.append(float(inp[0:count]))
                inp = inp[count:]
                count = 0
            output.append(inp[0])
            inp = inp[1:]
        if len(inp) == 0:
            break
        if inp[count].isnumeric() or inp[count] == ".":
            count += 1
    return output

def format_okay(expression):
    ok_chars = ["*", "/", "+", "-", "(", ")", "^"]
    true_opers = ["*", "/", "+", "-", "^"]

    if ".." in expression:  #checks if decimals are used properly
        return False
    if expression[0] in true_opers:
        return False
    if expression[-1] in true_opers:
        return False
    if balanced(expression) == False:  #checks for parenthesis balance
        return False

    for char in expression:
        if (char.isnumeric()) or (char in ok_chars) or (char == "."): #checks input only contains numbers and operators
            continue
        else: 
            return False
    
    expression = seperate(expression) #checks for correct ammont of operators/numbers
    floatcount = 0
    strcount = 0
    for x in expression:
        if type(x) == float:
            floatcount += 1
        if x in true_opers:
            strcount += 1
    if floatcount != strcount+1:
        return False

    return True

def infix_to_postfix(expression):  #based off pseudocode given by Michael Coe and https://runestone.academy/ns/books/published/pythonds/index.html
    expression = seperate(expression)
    opstack = Stack()
    outlist = []
    operators = ["*", "/", "+", "-"]
    nums = [str(x) for x in range(1,10)]
    precedence = {"(":1, "+":2, "-":2, "*":3, "/":3, "^":4,}
    for char in expression:
        if type(char) == float:
            if char.is_integer():
                outlist.append(str(int(char)))
            else:
                outlist.append(str(char))
        elif char == "(":
            opstack.push(char)
        elif char == ")":
            popped = opstack.pop()
            while popped != "(":
                outlist.append(popped)
                popped = opstack.pop()
        else:
            while not (opstack.isEmpty()) and (precedence[opstack.peek()] >= precedence[char]):
                outlist.append(opstack.pop())
            opstack.push(char)
    while not opstack.isEmpty():
        outlist.append(opstack.pop())
    return " ".join(outlist)

def calculate(expression):
    expression = infix_to_postfix(expression)
    expression = expression.split()
    tree = ExpTree.make_tree(expression)
    return ExpTree.evaluate(tree)

if __name__ == '__main__':
    print("Welcome to Calculator Program!")
    while True:
        user_input = (input("Please enter your expression here. To quit enter 'quit' or 'q':\n").replace(" ", ""))
        if (user_input.lower() == "q") or (user_input.lower() == "quit"):
            print("Goodbye!")
            break
        if format_okay(user_input) == False:
            continue
        print(calculate((user_input))) 

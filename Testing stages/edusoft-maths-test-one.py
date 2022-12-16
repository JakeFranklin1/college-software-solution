import operator
import random

# a = random.randrange(0, 10, 1)
# b = random.randrange(0, 10, 1)
operatorDict = {"+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.floordiv}

def levelOne():
    a = random.randrange(0, 10, 1)
    b = random.randrange(0, 10, 1)
    if b != 0:
        operator = random.choice(["+", "-", "*","/"])
        print(a, operator, b)
        return operatorDict[operator](a, b)
    else:
        operatorNoDiv = random.choice(["+", "-", "*"])
        result = operatorDict[operatorNoDiv](a, b)
        print(a, operatorNoDiv, b, 'testing else')
        print(result, "no division", operatorNoDiv)
        return operatorDict[operatorNoDiv](a, b)

print(levelOne())
# operator, a, b, operatorDict = levelOne()
    

# result = operatorDict[operator](a, b)
# operators = [operator.add, operator.sub, operator.mul]
# random_operator = random.choice(operators)
import operator
import random
operatorDict = {"+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.floordiv}

def levelOne():
    operatorNoDiv = random.choice(["+", "-", "*","/"])
    question = 0
    while question != 10:
        a = random.randrange(0, 10, 1)
        # b = random.randrange(0, 10, 1)
        b = 0
        if b != 0:
            question += 1
            print("Question number: %d" % question)
            print(a, operator, b)
            result = operatorDict[operator](a, b)
            print("Answer =",result)
        elif b == 0 and operator == "/":
            operatorNoDiv = random.choice(["+", "-", "*"])
            question += 1
            print(a, operatorNoDiv, b, "\nElse Called")
            result = operatorDict[operatorNoDiv](a, b)
            print("Answer =",result)

levelOne()
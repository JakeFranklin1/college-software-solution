import random
import operator

question = 0
level = 1
wrongAnswer =

operatorDict = {"+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.floordiv}

while question != 10:
    question += 1

    print("Question: ", question)

    num1 = random.randrange(0, 10)
    num2 = random.randrange(0, 10)
    operator = random.choice(["/", "+", "-", "*"])
    result = operatorDict[operator](num1, num2)

    while result < 0 and level != 3:
        num1 = random.randrange(0, 10)
        operator = random.choice(["/", "+", "-", "*"])
        num2 = random.randrange(0, 10)
        result = operatorDict[operator](num1, num2)

    if num2 == 0 and operator == "/":
        operatorNoDiv = random.choice(["+", "-", "*"])
        result = operatorDict[operatorNoDiv](num1, num2)

    print(str(num1) + " " + str(operator) + " " + str(num2))
    print("The answer is:", result)

    answer = int(input("Enter answer: "))
    if answer == result:
        print("Well done!")
    else:
        print("Wrong answer")

    if question == 10:
        print("Game over!")

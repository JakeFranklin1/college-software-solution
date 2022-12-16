import operator
import random
operatorDict = {"+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.floordiv}

def levelOne():
    question = 0
    correctAnswer = 0
    wrongAnswer = 0
    while question != 10:
        question += 1
        operator = random.choice(["-", "+", "*", "/"])
        a = random.randrange(0, 10, 1)
        b = random.randrange(0, 10, 1)
        if b == 0 and operator == "/":
            operatorNoDiv = random.choice(["+", "-", "*"])
            result = operatorDict[operatorNoDiv](a, b)
            while result < 0:
                a = random.randrange(0, 10, 1)
                b = random.randrange(0, 10, 1)
                print("Generating new numbers:", a, operatorNoDiv, b) # Testing
                result = operatorDict[operatorNoDiv](a, b)
            print(" Question number: %d" % question + "\n", a, operatorNoDiv, b)
            print("Answer =",result) # testing
            answer = int(input("Please Answer the Question: "))
        else:
            result = operatorDict[operator](a, b)
            while result < 0:
                a = random.randrange(0, 10, 1)
                b = random.randrange(0, 10, 1)
                print("Generating new numbers:", a, operator, b) # Testing
                result = operatorDict[operator](a, b)
            print("Question number: %d" % question,"\n", a, operator, b)
            print("Answer =",result) # Testing
            answer = int(input("Please Answer the Question: "))
        if answer == result:
            print("\nCorrect! The answer was", result,"\n")
            correctAnswer += 1
        elif answer != result:
            print("\nWrong! The answer was", result,"\n")
            wrongAnswer += 1
    if question == 10:
        print("Your correct answers were:",correctAnswer, "And you got",wrongAnswer,"Incorrect")

levelOne()
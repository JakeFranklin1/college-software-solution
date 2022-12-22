import random
import operator
operatorDict = {"+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.floordiv}

question = 0
wrongAnswer = 0
prevQuestions = []
while question != 10:
    
    question += 1
    operator = random.choice(["-", "+", "*", "/"])
    a = 1
    b = 1
    # a = random.randrange(0, 5,1)
    # b = random.randrange(0, 5,1)
    
    currentQuestion = (str(a) + ' ' + str(operator) + ' ' + str(b))
    print(currentQuestion)
    for c in prevQuestions:
        if currentQuestion in prevQuestions:
            a = random.randrange(0, 5,1)
            b = random.randrange(0, 5,1)
            print(prevQuestions, currentQuestion)
            print("recalculated")
    
    if b == 0 and operator == "/":
        operatorNoDiv = random.choice(["+", "-", "*"])
        result = operatorDict[operatorNoDiv](a, b)
        print("tried to divide by 0")
        while result < 0:
            a = random.randrange(0,5,1)
            b = random.randrange(0,5,1)
            print("Generating new numbers:", a, operator, b) # Testing
            result = operatorDict[operator](a, b)
        print("Question number: %d" % question)
        print(a, operator, b)
        print("Answer =",result) # Testing
    else:
        result = operatorDict[operator](a, b)
        while result < 0:
            a = random.randrange(0, 5,1)
            b = random.randrange(0, 5,1)
            print("Generating new numbers:", a, operator, b) # Testing
            result = operatorDict[operator](a, b)
        print("Question number: %d" % question)
        print(a, operator, b)
        print("Answer =",result) # Testing
    answer = int(input("\nPlease Answer the Question: "))
    
    
    if answer == result:
        print("\nCorrect! The answer was", result,"\n")
        # correctAnswer += 1
    elif answer != result:
        print("\nWrong! The answer was", result,"\n")
        wrongAnswer += 1
    store = (str(a) + ' ' + str(operator) + ' ' + str(b))
    prevQuestions.append(store)
    print(prevQuestions)
        
if question == 10:
    print("Your correct answers were:", (10 - wrongAnswer), "and you got",wrongAnswer,"incorrect")


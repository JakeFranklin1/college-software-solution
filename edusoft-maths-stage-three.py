import operator
import random
import csv
operatorDict = {"+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.floordiv}

def main():
    studentList = []
    filepath = 'student.csv'
    File = open(filepath)
    Reader = csv.reader(File)
    Data = list(Reader)
    login = input("Enter your login: ")
    for x in list(range(0, len(Data))):
        if login == Data[x][0]:
            print("User Found:",Data[x][1], Data[x][2])
            studentList.append(Data[x])
            level = int(Data[x][3])
            num1 = 0
            if level == 1:
                num2 = 1
            elif level == 2:
                num2 = 100
            elif level == 3:
                num1 = -100
                num2 = 100
            File.close()
            mathsTest(level,num1,num2)

def mathsTest(level,num1,num2):
    print("Level of test:",level)
    question = 0
    correctAnswer = 0
    wrongAnswer = 0
    while question != 10:
        question += 1
        operator = random.choice(["-", "+", "*", "/"])
        a = random.randrange(num1,num2,1)
        b = random.randrange(num1,num2,1)
        if b == 0 and operator == "/":
            operatorNoDiv = random.choice(["+", "-", "*"])
            result = operatorDict[operatorNoDiv](a, b)
            while result < 0 and level != 3:
                a = random.randrange(num1, num2, 1)
                b = random.randrange(num1, num2, 1)
                print("Generating new numbers:", a, operatorNoDiv, b) # Testing
                result = operatorDict[operatorNoDiv](a, b)
            print(" Question number: %d" % question + "\n", a, operatorNoDiv, b)
            print("Answer =",result) # testing
            answer = int(input("Please Answer the Question: "))
        else:
            result = operatorDict[operator](a, b)
            while result < 0 and level != 3:
                a = random.randrange(num1, num2, 1)
                b = random.randrange(num1, num2, 1)
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
        return updateScore(correctAnswer, wrongAnswer)
    
def updateScore(correctAnswer, wrongAnswer):
    
    

main()
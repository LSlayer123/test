import math
import os
Valid = False

def RomanToArab(Number):
  #Function for converting numbers from Roman numerals into traditional Arabic numbers
  
  Total = 0
  
  for i in range(0,len(Number)):
    if Number[i] == "I":
      Total = Total + 1
    elif Number [i] == "V":
      Total = Total + 5
    elif Number [i] == "X":
      Total = Total + 10
    elif Number [i] == "L":
      Total = Total + 50
    elif Number [i] == "C":
      Total = Total + 100
    elif Number [i] == "D":
      Total = Total + 500
    elif Number [i] == "M":
      Total = Total + 1000
  
  return Total

def ArabToRoman(Number):
  #Function for converting traditional Arabic numbers into Roman numerals
  
  Total = ""
  Numbers = (1000,500,100,50,10,5,1)
  Letters = ("MDCLXVI")
  
  for i in range (0,7):
    Amount = math.floor(int(Number) / (int(Numbers[i])))
    for j in range (0,int(Amount)):
      Total = Total + Letters[i]
    if Amount > 0:
      Number = int(Number) - (int(Numbers[i]) * int(Amount))
  
  return Total
    
def Validation(FirstPart, Procedure, LastPart):
  Letters = ("MDCLXVI") 
  Suitable = True
  for i in range(0,len(FirstPart)):
    if FirstPart[i] != ".":
      print("hi")
      
def Splitting(InitialProblem):
  #Function for splitting up the input from the user into the two numbers and the operation that needs to be processed
  
  length = 0
  FinalValues = []
  
  for i in range (0,len(InitialProblem)):
    if InitialProblem[i] == "+" or InitialProblem[i] == "-":
      length = i
  
  FirstNumber = InitialProblem[0:int(length)]
  Operation = InitialProblem[int(length)]
  LastNumber = InitialProblem[(int(length) + 1):]
  FinalValues.append(FirstNumber)
  FinalValues.append(Operation)
  FinalValues.append(LastNumber)
  
  return FinalValues

while not Valid:
  os.system("clear")
  Question = input("Please enter the calculation that you would like to be processed: \n")

  Values = Splitting(Question)
  
  Number1 = Values[0]
  Operation = Values[1]
  Number2 = Values[2]

  if Operation == "+":
    print("Arabic: \n" + (str((RomanToArab(Number1)) + (RomanToArab(Number2)))))
    print("Roman: \n" + (ArabToRoman(((RomanToArab(Number1)) + (RomanToArab(Number2))))))
    Valid = True
  elif Operation == "-":
    print("Arabic: \n" + (str((RomanToArab(Number1)) - (RomanToArab(Number2)))))
    print("Roman: \n" + (ArabToRoman(((RomanToArab(Number1)) - (RomanToArab(Number2))))))
    Valid = True

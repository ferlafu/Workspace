import re

def arithmetic_arranger(problems, solve = False):
  # arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    if(len(problems) > 5):
      return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for problem in problems:
      if(re.search("[^\s0-9.+-]", problem)):
        if(re.search("[*]", problem) or re.search("[/]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."

      firstNumber = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      secondNumber = problem.split(" ")[2]

      if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
        return "Error: Numbers cannot be more than four digits."

      sum = ""
      if(operator == "+"):
        sum = str(int(firstNumber) + int(secondNumber))
      elif(operator == "-"):
        sum = str(int(firstNumber) - int(secondNumber))  

      lenght = max(len(firstNumber), len(secondNumber)) + 2
      top = str(firstNumber).rjust(lenght)
      bottom = operator + str(secondNumber).rjust(lenght - 1)
      line = ""
      res = str(sum).rjust(lenght)
      for s in range(lenght):
        line += "-"
      
      if problem != problems[-1]:
        first += top + '    '
        second += bottom + '    '
        lines += line + '    '
        sumx += res + '    '
      else:
        first += top
        second += bottom
        lines += line
        sumx += res

    if solve:
      string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
      string = first + "\n" + second + "\n" + lines
    return string
      
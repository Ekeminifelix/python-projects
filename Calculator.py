operand = input('Number 1: ')
operand2 = input('Number 2: ')
sign= input("sign:")

#print (operand, sign, operand2)

if sign == '+':
    result = float(operand)+ float(operand2)

elif sign == '-':
    result = float(operand)- float(operand2)
elif sign == '/':
    result = float(operand)/ float(operand2)
elif sign == '*':
    result = float(operand)* float(operand2)
elif sign == '%':
    result = float(operand) % float(operand2)

print (result)

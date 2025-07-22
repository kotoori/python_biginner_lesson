def calculate(a, b, sign):
  if sign == '+':
    return a + b
  elif sign == '-':
    return a - b
  elif sign == '*':
    return a * b
  elif sign == '/':
    if b == 0:
      print('0で割ることはできません')
      return None
    else:
      return a / b
  else:
    return '+,-,*,/のいずれかを入力してください'

a = int(input('a: '))
b = int(input('b: '))
sign = input('+, -, *, /: ')  # +, -, *, /のいずれかを入力
print(calculate(a, b, sign))
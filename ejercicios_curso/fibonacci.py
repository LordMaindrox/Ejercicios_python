fibonacci=[]
x = 0
y = 1
num = 10
print(x,y)
for n in range(num):
  fibonacci.append(x+y)
  aux = x +y
  x = y
  y = aux
print(fibonacci)
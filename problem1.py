#O(n)
x=3
sum=0
limit = 1000
while x<limit:
  if x%3==0 or x%5==0:
    sum = sum + x
  x=x+1
print(sum)

#O(1)
three = int((limit-1)/3)
five = int((limit-1)/5)
fifteen = int((limit-1)/15)

def p(i):
  return i*(i+1)/2

print (3*p(three)+5*p(five)-15*p(fifteen))

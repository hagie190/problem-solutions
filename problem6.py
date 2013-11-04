ceiling  = 10
sosq= 0
while i in range (0, 10):
  sosq = sosq + (2*i+1)*(ceiling-i)
sqos = (ceiling*ceiling*(ceiling+1)*(ceiling+1))/4
print(sqos-sosq)

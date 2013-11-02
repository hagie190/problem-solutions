num =600851475143
prime = 2
while prime<num:
  if num%prime==0:
    num = num/prime
    continue
  prime = prime + 1
print(prime)

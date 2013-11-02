#O(n)
fo = 1
so = 1
et = 2
sum = 0

while et<4000000:
  sum = sum + et
  fo = et + so
  so = et + fo
  et = fo + so
print(sum)

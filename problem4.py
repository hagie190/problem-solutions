#for every 6 digit palidrome
stop= False
for x in range (-999, -99):
  #contruct
  if stop: break
  s = str(-x)
  num = int(s+s[2]+s[1]+s[0])
  #find factors
  for i in range (1, 901):
    if ((num%(1000-i)==0)and num/(1000-i)>100) and num/(1000-i)<1000:
      print(str(num) +" = "+str(1000-i)+" * "+str(num/(1000-i)))
      stop = True
      

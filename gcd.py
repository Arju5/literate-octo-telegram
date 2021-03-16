def gcd(x,y):
  if(x<y):
    smallest = x
  else:
    smallest = x
  for i in range(1, smallest + 1):
    if((x%i == 0) and (y%i == 0)):
      gcd = i
  
  return gcd
print("The gcd of the given two numbers is : ", gcd(50,20))

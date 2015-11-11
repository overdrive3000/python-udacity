# Find Biggest and/or Median number of given 3 numbers

def bigger(a,b):
  if a > b:
    return a
  return b

def biggest(a,b,c):
  return bigger(bigger(a,b),c)

def median(a,b,c):
  big = biggest(a,b,c)
  if a == big:
    return bigger(b,c)
  elif b == big:
    return bigger(a,c)
  else:
    return bigger(a,b)

print median(4,2,7)
print median(2,2,7)
print median(8,2,7)

print biggest(8,2,7)
print biggest(0,0,0)
print biggest(9,2,0)

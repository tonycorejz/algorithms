def gcd(a,b):
  p = 1
  q = 0
  r = 0
  s = 1
  m = a
  n = b
  while not(m==0 or n==0):
    if m>=n:
      m = m - n
      p = p - r
      q = q - s
    else:
      n = n - m
      r = r - p
      s = s - q
  if m == 0:
    k = n
    x = r
    y = s
  else:
    k = m
    x = p
    y = q
  print(k,x,y)
        
x = int(input())
y = int(input())
gcd(x,y)
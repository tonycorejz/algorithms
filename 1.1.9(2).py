def fibo(n):
  a, b = 0, 1
  for i in range(int(n / 2)):
      a = a + b
      b = a + b
  return a

n = int(input())
print(fibo(n))
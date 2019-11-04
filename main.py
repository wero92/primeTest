import math

def isPrime(number):
  if (number < 2):
    return False
  else:
    for i in range(2, int(math.sqrt(number)) + 1):
      if number % i == 0:
        return False
  return True

cases = int(input(''))
while cases:
  number = int(input(''))
  cases -= 1
  print("Liczba jest pierwsza") if isPrime(number) else print("Liczba NIE JEST pierwsza")

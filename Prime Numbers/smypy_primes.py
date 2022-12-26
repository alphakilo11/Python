import sympy
count = 0
candidate = 1
while count < 999999:
  candidate += 2
  if sympy.isprime(candidate) == True:
    count += 1
print(candidate)

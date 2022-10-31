# saves permutation variants to endergebnis variable

from timeit import default_timer as timer

def permutation(folge):
    global ergebnis, level, endergebnis
    if len(folge) > 1:
        original = folge.copy()
        for i in range(len(folge)):
            ergebnis[level] = folge[i]
            del folge[i]
            level = level + 1
            permutation(folge)
            folge = original.copy()
            if i == len(original) - 1:
                level = level - 1
    else:
        ergebnis[level] = folge[0]
        level = level - 1
        output = ""
        for element in ergebnis:
          output += element
        endergebnis.append(output)
        
def sub_string_divisibility(number):
  divisors = (2, 3, 5, 7, 11, 13, 17)
  divisor = len(divisors) - 1 #iterating backwards is probably 28.5% faster
  for i in range(7, 0, -1):
    if int(number[i: i+3]) % divisors[divisor] != 0:
      return False
    divisor -= 1
  return True

folge = "0123456789"
folge = [i for i in folge]
ergebnis = [""] * len(folge)
endergebnis = []
level = 0
startzeit = timer()
permutation(folge)
sum = 0
for candidate in endergebnis:
  if sub_string_divisibility(candidate):
    sum += int(candidate)

print("Dauer:", timer() - startzeit)
sum

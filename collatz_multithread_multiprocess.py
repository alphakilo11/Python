import multiprocess as mp  
import time  

def collatz(params):
  #threadnumber = params[0]
  start = params[0]
  end = params[1]
  for i in range(start, end):
      while i != 1:
          if i % 2 == 0:
              i = i / 2
          else:
              i = 3 * i + 1
 # print("Thread number", threadnumber, "done.") 

def distribute(number_to_distribute, divisor):
  step1 = []
  share = number_to_distribute / divisor
  for i in range(divisor):
    step1.append(int(share * i) + 1)
  result = []
  for i in step1:
    result.append([i, i + 1])
  result[len(result) - 1][1] = number_to_distribute
  return result



start = time.time()

if __name__ == '__main__':
    parameter1 = (distribute(52500, 1))
    pool = mp.Pool(mp.cpu_count())  
    pool.map(collatz, parameter1)
    pool.close()  
    pool.join()  

print("Duration: ", time.time() - start)
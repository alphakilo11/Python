import multiprocessing as mp  
import time  

def test_function(i):   
    print("function starts" + str(i))  
    time.sleep(1)  
    print("function ends" + str(i))  

if __name__ == '__main__':  
    pool = mp.Pool(mp.cpu_count())  
    pool.map(test_function, [i for i in range(4)])  
    pool.close()  
    pool.join()  
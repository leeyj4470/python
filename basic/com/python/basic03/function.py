'''
Created on 2018. 6. 12.

@author: big2-00
'''
import math

def abc():    
    pass

def stddev(*args):
    def mean():
        return sum(args)/len(args)
    
    def variance(m):
        total=0;
        for arg in args:
            total+=(arg-m)**2
        return total/(len(args)-1)
    
    v=variance(mean())       
    return math.sqrt(v)

if __name__ == '__main__':
    
    stddev=stddev(2.3,1.7,1.4,0.7,1.9)
    print(stddev)
    
    
    
    
    
    
    
    
    
    
'''
Created on 2018. 6. 11.

@author: big2-00
'''

import math

if __name__ == '__main__':
    
    a=input()
    a=float(a)
    
    a=math.trunc((a+0.005)*100)/100
    
    print(a)
    
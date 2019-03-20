'''
Created on 2018. 6. 12.

@author: big2-00
'''

class Car:    
      
    
    def __init__(self):
       self.color=0xFF0000
       self.wheel_size=16
       self.displacement=2000
       self.maker=["HYNDAI"] 
             
    
    def forward(self):
        pass
    
    def backward(self):
        pass
    
    def turn_left(self):
        pass
    def turn_right(self):
        pass
        

if __name__=='__main__':
    
   myCar1=Car()   
   myCar2=Car()   
   
   print(myCar1.maker)
   
   myCar1.maker[0]="DAEWOO"
   
   print(myCar1.maker)
   print(myCar2.maker)
   
    









    
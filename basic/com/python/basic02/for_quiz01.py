'''
Created on 2018. 6. 12.

@author: big2-00
'''

if __name__ == '__main__':
        
    for dan in range(2,10):
        print(str(dan)+"단 입니다.")
        
        for gop in range(1,10):
            print("{0} * {1} = {2}".format(dan,gop,dan*gop))
        
        print()
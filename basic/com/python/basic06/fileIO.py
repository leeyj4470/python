'''
Created on 2018. 6. 12.

@author: big2-00
'''
from test.test_decimal import file

if __name__ == '__main__':
    
    '''
    file=open('test.txt','w')
    file.write("hello")
    file.close()
    '''
    
    '''
    file=open('test.txt','r')
    str=file.read()
    print(str)
    file.close()
    '''
    
    '''
    lines = ['안녕하세요\n','김형민입니다\n',
            '여기까지 파이썬 기초\n',
            '수업을 마치겠습니다.']
    
    with open('finish_utf8.txt','w',encoding='utf-8') as file:
        for line in lines:
            file.write(line)
    
    '''
    
    with open('finish_utf8.txt','r',encoding='utf-8') as file:
        lines=file.readlines()
        line=''
        for line in lines:
            print(line,end='')
    
    
    
    
    
    
    
    
    
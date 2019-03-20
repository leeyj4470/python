'''
Created on 2018. 6. 12.

@author: big2-00
'''

if __name__ == '__main__':
    print('숫자를 입력하세요.')
    a=int(input())
    
    if a==0:
        print('0은 나눗셈을 이용할 수 없습니다.')
    else:
        print('3 / {0} = {1}'.format(a,3/a))
        
    print('1~7 의 숫자 하나를 입력하세요.')
    a=int(input())
    
    day=''
    if a==1:
        day="월"
    elif a==2:
        day="화"
    elif a==3:
        day="수"
    elif a==4:
        day="목"
    elif a==5:
        day="금"
    elif a==6:
        day="토"
    elif a==7:
        day="일"
    else:
        day="숫자 입력이 잘못되었습니다."
    
    print(day)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
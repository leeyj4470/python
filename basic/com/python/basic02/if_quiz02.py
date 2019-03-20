'''
Created on 2018. 6. 12.

@author: big2-00
'''

if __name__ == '__main__':
    print('국어점수:')
    kor=int(input())
    print('수학점수:')
    math=int(input())
    print('영어점수:')
    eng=int(input())
    
    total=kor+math+eng
    avg=total/3
    
    grade='F'
    if(avg>=90):
        grade='A'
    elif(avg>=80):
        grade='B'
    elif(avg>=70):
        grade='C'
    else:
        grade='F'
        
    print('총점 : '+str(total))
    print('평균 : '+str(avg))
    print('학점 : '+grade)
        
        
        
        
        
        
    
'''
Created on 2018. 6. 12.

@author: big2-00
'''

if __name__ == '__main__':
    
    a=""
    
    while True:
        print("초기메뉴")
        print("[1] 사용자 등룍")
        print("[2] 로그인")
        print("[3] 아이디/패스워드 찾기")
        print("메뉴를 선택하세요.(종료:q/Q)",end="")                
        
        a=input().upper();
        if(a=='1'):
            print("사용자등록 페이지로 이동합니다.")
        elif(a=='2'):
            print("로그인 페이지로 이동합니다.")
        elif(a=='3'):
            print("아이디/패스워드 찾기 페이지로 이동합니다.")
        elif(a=='Q'):
            print("프로그램을 종료합니다.")
            break # sys.exit(0) 
        else:
            print("입력이 올바르지 않습니다.")
        
        
        
        
        
        
        
        
        
        
        
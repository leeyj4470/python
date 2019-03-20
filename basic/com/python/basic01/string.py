

if __name__ == '__main__':    
    a=""
    b=""
    print("a 변수 값을 입력하시오\n")    
    a=input()
    
    print("b 변수 값을 입력하시오\n")
    b=input()
    
    print("a변수 타입 : "+str(type(a))+"\n")
    print("b변수 타입 : "+str(type(b))+"\n")
    
    c=int(a)+int(b)

    print("{0} + {1} = {2}".format(a,b,c))


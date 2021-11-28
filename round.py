import math
def solution():
    global n
    mmin_dec=0
    mmax_dec=0
    mmiddle = 0
    #n=4.2
    clear_n=math.trunc(n)
    clear_n= (n%clear_n)
    print(clear_n)
    
    if clear_n < 0.5:
        mmin_dec=0
        mmax_dec=0.5
        mmiddle = 0.25
        
    
    if clear_n > 0.5:
        mmin_dec=0.5
        mmax_dec=1
        mmiddle = 0.75
    
    if clear_n >= mmin_dec and clear_n <= mmax_dec: #0 to 0.5
        if clear_n < mmiddle:
            before = int(n)+mmin_dec
            print(before)
            answer=(round(before,1))
            print(answer)
            return answer
             
        if clear_n >= mmiddle:
            before=int(n)+mmax_dec
            print(before)
            answer=(round(before,1))
            print(answer)
            return answer
    if clear_n == 0.5:
        return (int(n)+0.5)


n=input("Enter n: ")
n=float(n)
print(type(n),n)
solution()
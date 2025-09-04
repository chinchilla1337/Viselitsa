import math
n,k = int(input()),int(input())
p=int(math.log(n, k))
steps = n-k**p
print(steps)


li = list(range(1, n+1))

def delete_num(l, k, steps):
    cnt=0
    a=1
    for i in range(1,steps+1):
        li.remove(a+k-1)
        if i+cnt not in l:
            cnt+=1
        li.append(i+cnt)
        a=a+k
        

def deletenum(n,k,steps):
    a=0
    l = (list(range(1,n+1)))
    for i in range(1,steps+1):
        t=l[a+k-1]
        del l[a+k-1]
        if t>=n//k:
            l.extend(l)
        a=a+k
    print(t)    
    


deletenum(n, k, steps)

    
         
              
        





    


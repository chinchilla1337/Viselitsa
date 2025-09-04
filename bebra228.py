s= input()
li = s.split()
a= s.split()
cnt = 0
for i in range(len(li)):
    a[i]=""
    for j in a:
        if j == li[i]:
            cnt+=0.5
    a = s.split()   
print(int(cnt))
        

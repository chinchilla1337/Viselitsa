import time
start_time = time.time()
a = [5, 1, 4,2,8]
cnt = 0
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1], a[j]
            
        
print(a)
print(f"Elapsed time: {time.time() - start_time:.4f} seconds")

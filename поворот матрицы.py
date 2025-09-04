
def povorot90(matrix):
    n=len(matrix)
    for j in range(n):
        li=[]
        for i in range(n):
            li.append(matrix[i][j])
        li.reverse()
        matrix.append(li)
    del matrix[:n]
    return matrix
                              
            
def sum_triangle(matrix):
    n=len(matrix)
    sum=0
    for i in range(n):
        for j in range(n):
            if i<j and j<n-i-1:
                sum+=matrix[i][j]
    return sum


                
n = int(input())
matrix = [[int(m) for m in input().split()] for _ in range(n)]
sum1= sum_triangle(matrix)
a = povorot90(matrix)
print(a)
b = povorot90(a)
print(b)
c = povorot90(b) 
print(c)
sum2 = sum_triangle(a)
sum3 = sum_triangle(b)
sum4 = sum_triangle(c)

print(f"Верхняя четверть: {sum1}")
print(f"Правая четверть : {sum4}")
print(f"Нижняя четверть: {sum3}")
print(f"Левая четверть: {sum2}")

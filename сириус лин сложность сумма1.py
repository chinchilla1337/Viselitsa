st=[]
def push(inputt):
    n=int(inputt[-1])
    st.append(n)
    print('ok')
def pop():
    if st:
        print(st.pop())
    else:
        print('error')
        
def back():
    if st:
        print(st[-1])
    else:
        print('error')
def size():
    print(len(st))
def clear():
    st.clear()
    print('ok')
def exit():
    print('bye')
di = dict(zip(['push', 'pop', 'back', 'size', 'clear', 'exit'][push(),pop(),back(),size(),clear(),exit()]))

while input!='exit':
    di[input()]()

exit()

     

list_a = [1,2,"문자열",True,False]
print(list_a[2][2])
print(list_a[ : ]) # start_index : end_index-1 # 원본을 복사
print(list_a[:3])
print(list_a[3:])
print(list_a[-2:])
# start_index : end_index-1 : 1
print(list_a[::2])
print(list_a[::-1]) #역순으로 접근

list_a = [1,2,3]
list_b = [4,5,6]

print(list_a + list_b)
print(list_a*3)

set_a = {'a':1,'b':2,'c':3}
print(set_a['a'])
# remove

list_a = [1,1,1,2]

# solution
index = 0
for i in range(len(list_a)-1,-1,-1): #역순으로 조회
   if list_a[i] == 1:
      del list_a[i]
    
print(list_a)

# remove
list_a = [1,2,1,1,2,3]

print(type(list_a))


for i in range(len(list_a)):
    print(f'index {i} list_a --{list_a}')
    if 1 in list_a:
        list_a.remove(1)
    else:
        break

print(list_a)
print(list_a.count(1))
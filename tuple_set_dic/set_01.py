# 저금통
list_a = [100,500,10,500,100,50,500,10]
# 저금통에 있는 동전의 종류 10,50,100,500

# 셋

set_a = {1,2,3,1,2,3,1}
print(f'set_a = {set_a}')   # 중복 제거

# 중복을 제거(허용하지 않는다)한다
# 순서가 랜덤이다

print(set(list_a))

set_2 = {1,2}
# print(set_2[0])
set_2.add(3)
print(set_2)
set_2.remove(2)
print(f'remove -- {set_2}')
set_2.update([5])
print(f'update -- {set_2}')
set_2.pop()
print(f'pop -- {set_2}')
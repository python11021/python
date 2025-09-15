# 중첩 for문

list_1 = [10,20,30]
list_2 = [11,21,31]

list_2th = [list_1, list_2]
print(list_2th)

for i in range(len(list_2th)):
    for j in range(len(list_2th[i])):
        print(list_2th[i][j])


list_of_list = [[1,2,3],[4,5,6,7],[8,9],]

for i in range(len(list_of_list)):
    for j in range(len(list_of_list[i])):
        print("list_of_list", list_of_list[i][j])
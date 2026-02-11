# import array as arr

# arrName=arr.array('i', [12, 6, 8, 9, 5])
# print(arrName)

# #operation
# #1.add
# #a)append()
# # arrName.append(10)
# # print(arrName)
# # #b)insert()
# # arrName.insert(0,-9)
# # print(arrName)  
# # # 2.delete
# # # remove
# arrName.remove(12)
# print(arrName)
# arrName.pop(1)
# print(arrName)
# arrName[0] = 40
# print(arrName)





import array as uday
arrayName = uday.array('i', [12, 35, 56, 67])
for i in range(0, len(arrayName),2):
    print(arrayName[i],end=" ")

#write a program to get the sum and product
sum = 0
product = 1
for val in arrayName:
    sum+=val
    product*=val
print(sum)
print(product)
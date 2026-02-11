import array as uday
arrayName = uday.array('i', [12, 35, 56, 67])
count=0
target=int(input("Enter the target element: "))
for val in arrayName:
    if val == target:
        count+=1

#t/c = 0(N)
#s/c = 0(1)
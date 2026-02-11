import array as uday
arrayName = uday.array('i', [8, 7, 5, 4, 3])

inc=True
dec=True
for i in range(0, len(arrayName)-1):
    if(arrayName[i]>arrayName[i+1]):
        inc=False
    if(arrayName[i]<arrayName[i+1]):
        dec=False
if (inc == True):
    print("in increasing order")
elif (dec == True):
    print("in decreasing order")
else:
    print("not sorted")
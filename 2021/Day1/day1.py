arr = [int(num) for num in open('input.txt','r')]
count = count2 = 0

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        count += 1
    if i > 2 and arr[i-1] + arr[i-2] + arr[i-3] < arr[i] + arr[i-1] + arr[i-2]:
        count2 += 1
print(count, count2)
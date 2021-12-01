arr = [int(num) for num in open('inp1')]
count = count2 = 0

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        count += 1
    if i > 2 and arr[i-1] + arr[i-2] + arr[i-3] < arr[i] + arr[i-1] + arr[i-2]:
        count2 += 1
print(f'{count}\n{count2}')
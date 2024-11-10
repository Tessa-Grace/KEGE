with open('input.txt') as file:
    st = file.readline()

count = 3
ans = 0

for i in range(len(arr) - 3):
    s1, s2, s3, s4 = arr[i:i+4]
    t = s1 + s2 + s3 + s4
    if t == ban:
        count = 3
    else:
        count += 1
    ans = max(ans, count)
    
print(ans)

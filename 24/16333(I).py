with open('input.txt') as file:
    st = file.readline()

count = 1
ans = 0
for i in range(len(st) - 1):
    s1, s2 = st[i], st[i+1]
    if s1 in 'QRW' and s2 in 'QRW' or \
       s1 in '124' and s2 in '124':
        count = 1
    else:
        count += 1
    ans = max(ans, count)

print(ans)

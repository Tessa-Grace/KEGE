with open('24_11813.txt') as file:
    st = file.readline()

gl = 'AEIOUY'

count = 1
ans = 0
for i in range(len(st) - 1):
    s1, s2 = st[i], st[i + 1]
    if s1 in gl and s2 in gl or \
       s1 not in gl and s2 not in gl:
        count = 1
    else:
        count += 1
    ans = max(ans, count)

print(ans)

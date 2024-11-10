with open('input.txt') as file:
   data = file.readline()

ans = 0

for i in range(len(data)):
   count = 0
   count_y = 0
   for j in range(i, len(data)):
      if data[j] == 'Y':
         count_y += 1
      else:
         count += 1
      if count_y == 151:
         break
   ans = max(ans, count + 150)

print(ans)

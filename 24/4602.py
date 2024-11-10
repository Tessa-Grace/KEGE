with open('24_4602') as file:
    data = file.readline()

data = data.replace('A', 'O')
data = data.replace('C', 'B').replace('D', 'B')
data = data.replace('BO', '*')
data = data.replace('O', ' ').replace('B', ' ')

data = data.split()
print(len(max(data, key=len)))

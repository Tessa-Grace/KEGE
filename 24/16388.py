with open('24_16388.txt') as file:
    data = file.readline()

data = data.replace('KLMN', '&&&&').replace('&KLM', '&&&& ').replace('&KL', '&&& ').replace('&K', '&& ')
data = data.replace('LMN&', ' &&&&').replace('MN&', ' &&&').replace('N&', ' &&')

for i in 'KLMN':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))

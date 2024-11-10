with open('input.txt') as file:
    st = file.readline()

gl = 'eyuioa'.upper()
sg = 'qwrtpsdfghjklzxcvbnm'.upper()

for i in gl:
    st = st.replace(i, 'E')
for i in sg:
    st = st.replace(i, 'G')

while 'GG' in st or 'EE' in st:
    st = st.replace('GG', 'G G').replace('EE', 'E E')
    
st = st.split()
print(len(max(st, key=len)))

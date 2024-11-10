with open('24_16333.txt') as file:
    st = file.readline()

st = st.replace('2', '1').replace('4', '1')
st = st.replace('W', 'Q').replace('R', 'Q')
while 'QQ' in st or '11' in st:
    st = st.replace('QQ', 'Q Q').replace('11', '1 1')

st = st.split()

print(len(max(st, key=len)))

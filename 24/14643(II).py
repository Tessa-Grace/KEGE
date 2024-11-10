with open('24_14643.txt') as file:
    st = file.readline()

arr = arr.replace('AXMM', 'AXM XMM')
print(len(max(arr.split(), key=len)))

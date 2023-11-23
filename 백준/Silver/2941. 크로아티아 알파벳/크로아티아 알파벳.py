string = input()
lis = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in lis:
    string = string.replace(i, '1')
print(len(string))
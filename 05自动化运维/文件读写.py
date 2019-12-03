import sys

# f = open('app.log')
# print(f.read())
# f.close()

# f = open('data.txt', 'w')
# f.write('Beautiful is better than ugly.')
# f.writelines(['Explicit is better than implicit.','Simple is better than complex.'])

# with open('data.txt', 'w') as f:
#     print(1, 2, 'hello,world', sep=",", file=f)

with open('data.txt') as inf,open('out.txt','w') as outf:
    for line in inf:
        outf.write("".join([word.ca]))

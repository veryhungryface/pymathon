g=open("new2.txt",'r')
read=g.readlines()
read="".join(read)
print(read)

print(type(read))
g.close()

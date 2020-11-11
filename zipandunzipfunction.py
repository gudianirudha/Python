x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))
#zipped
x2, y2 = zip(*zip(x, y))
# * is used to unzip
print(x2,y2)
#unzipped

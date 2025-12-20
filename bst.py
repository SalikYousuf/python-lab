a = [1,2,3,4,5,6]
for elem in a:
    print(elem)

b = [1,3,5,2,0]
b.sort()
print(b)

b.append(9)
print(b)
b.reverse()
print(b)

a.copy()
a.extend(b)
a.index(3)
a.insert(2,10)
#a.remove()
a.count(10)
print(a)

print(len(a))
print(max(a))
print(min(a))

name = "hello world"
print(name[::-1])
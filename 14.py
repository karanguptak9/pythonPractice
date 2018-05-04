a = ["1", 1, "1", 2]
#set function doesnt contain duplicate
a = list(set(a))
print(a)


#Or use if statement
b = []
for i in a:
    if i not in b:
        b.append(i)
print (b)

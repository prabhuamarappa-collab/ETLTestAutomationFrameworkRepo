#create list 1 to 100
l = list(range(1,101))
print(l)

#create 2 lists(even_records & odd_records) from existing list
e = []
o = []
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e)
print(o)

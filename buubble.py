a=[12,56,43,1]

for j in range(0,len(a)):
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            k=a[i]
            a[i]=a[i+1]
            a[i+1]=k
print(a)

#UPDATE table 'studet' set name='mohammed azzan' WHERE name='azzan';
#DELETE from student where name='mohammed azzan';
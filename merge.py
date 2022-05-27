def mergeArrays(a, b, n1, n2):
    c = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
 
    while i < n1 and j < n2:
     
    
        if a[i] < b[j]:
            c[k] = a[i]
            k = k + 1
            i = i + 1
        else:
            c[k] = b[j]
            k = k + 1
            j = j + 1
     
 
  
    while i < n1:
        c[k] = a[i]
        k = k + 1
        i = i + 1
 
  
    while j < n2:
        c[k] = b[j]
        k = k + 1
        j = j + 1
    print("Array after merging")
    for i in range(n1 + n2):
        print(str(c[i]), end = " ")
 

a = [1,2,3]
n1 = len(a)
 
b = [2,5,5]
n2 = len(b)
mergeArrays(a, b, n1, n2)
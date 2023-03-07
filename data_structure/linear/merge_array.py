def merge(a1,a2):
    result = []
    i,j = 0,0
    while i < len(a1) and j < len(a2):
        if a1[i] > a2[j]:
            result.append(a2[j])
            j += 1
        else:
            result.append(a1[i])
            i += 1
    result += a1[i::]
    result += a2[j::]
    return result 

a = [1,7,8]
b = [1,2,4,5,6,7,10,12]
c=merge(a,b)
print(c)
def mergeSort(alist):
    if len(alist)<=1:
        return alist
    m=len(alist)//2
    left=alist[:m]
    right=alist[m:]
    left=mergeSort(left)
    right=mergeSort(right)
    print 'splitting:',left,right
    return list(merge(left,right))

def merge(left,right):
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    print 'merging:',result
    return result

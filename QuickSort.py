def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        split=partition(alist,first,last)
        quickSortHelper(alist,first,split-1)
        quickSortHelper(alist,split+1,last)

def partition(alist,start,end):
    pivot=alist[start]
    left=start+1
    right=end
    Done=False
    while not Done:
        while left<=right and alist[left]<pivot:
            left+=1
        while left<=right and alist[right]>pivot:
            right-=1
        if left>right:
            Done=True
        else:
            alist[left],alist[right]=alist[right],alist[left]
            left+=1
            right-=1
    alist[start],alist[right]=alist[right],alist[start]
    return right

"""Example of recursion, following sorting algorithm is selection sort
written using recursion"""
def select_sort(alist, n):
    if n <= 1:
        return
    position = 0
    maximum = alist[position]
    i = 1
    while i < n:
        if alist[i] > maximum:
            position = i
            maximum = alist[position]
        i += 1

    alist[n - 1], alist[position] = alist[position], alist[n - 1]
    select_sort(alist, n - 1)


mylist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(mylist)

select_sort(mylist, n)
print(mylist)

def mergeSort(S):
    """Sort the elements of Python list S using the merge sort algorithm"""
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    mergeSort(S1)
    mergeSort(S2)

    merge(S1, S2, S)


def merge(S1, S2, S):
    """Merge two sorted Python Lists S1 and S2 into properly sized list S"""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i = i + 1
        else:
            S[i + j] = S2[j]
            j = j + 1


data1 = [5, 4, 3, 2, 1]
mergeSort(data1)
print("Sorted Data 1 ", data1)

data2 = [1, 2, 3, 4, 5]

mergeSort(data2)
print("Sorted Data 2 ", data2)

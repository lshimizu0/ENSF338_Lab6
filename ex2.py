import random
import timeit


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent



def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)

    return root



def bst_search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None



def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def main():
    n = 10000

   
    vec = list(range(n))

    random.shuffle(vec)


    root = None
    for value in vec:
        root = insert(value, root)


    bst_times = []
    for value in vec:
        t = timeit.timeit(lambda v=value: bst_search(v, root), number=10)
        bst_times.append(t / 10)

    bst_avg_time = sum(bst_times) / len(bst_times)
    bst_total_time = sum(bst_times)


    sorted_vec = sorted(vec)


    binary_times = []
    for value in vec:
        t = timeit.timeit(lambda v=value: binary_search(sorted_vec, v), number=10)
        binary_times.append(t / 10)

    binary_avg_time = sum(binary_times) / len(binary_times)
    binary_total_time = sum(binary_times)

    print("BST Search Results")
    print(f"Average time per search: {bst_avg_time:.12f} seconds")
    print(f"Total time for all searches: {bst_total_time:.12f} seconds")

    print("\nBinary Search Results")
    print(f"Average time per search: {binary_avg_time:.12f} seconds")
    print(f"Total time for all searches: {binary_total_time:.12f} seconds")


if __name__ == "__main__":
    main()


# The results consistently show that the BST search is faster than binary search.
# Since they have the same time complexity of O(log(n)) it is likely due to the python
# implementation of the theory. In lower level languages it is likely that searching though
# the array will have a faster time since it does not have to do as much work with memory.
import random
import timeit
# Question 1:
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False
    

def measure_search(tree, values):
    times = []

    for x in values:
        t = timeit.timeit(lambda: tree.search(x), number=10)
        times.append(t / 10)

    avg_time = sum(times) / len(times)
    total_time = sum(times)
    return avg_time, total_time


# Question 2:
sorted_vector = list(range(10000))

sorted_tree = BST()
for value in sorted_vector:
    sorted_tree.insert(value)

avg_sorted, total_sorted = measure_search(sorted_tree, sorted_vector)

print("Sorted insertion tree:")
print("Average search time:", avg_sorted)
print("Total search time:", total_sorted)


# Question 3:
shuffled_vector = sorted_vector[:]
random.shuffle(shuffled_vector)

shuffled_tree = BST()
for value in shuffled_vector:
    shuffled_tree.insert(value)

avg_shuffled, total_shuffled = measure_search(shuffled_tree, sorted_vector)

print("\nShuffled insertion tree:")
print("Average search time:", avg_shuffled)
print("Total search time:", total_shuffled)

# When the sorted values are inserted onto the tree it becomes unbalanced, basically a linked list.
# The search algorithim will have to go throgh values linearly with time complexity O(n). Whereas with the shuffled insertion
# the search time is optimized since less nodes need to be iterated through with time complexity O(log(n)).


from heap_operations import MaxHeap





heap = MaxHeap()

print("is Heap empty: " + str(heap.is_empty()))
for val in [15, 10, 20, 17, 8]:
    heap.insert(val)
    print(f"Inserted {val}, heap: {heap.heap}")
heap.printHeap()

print("\nExtracting max values:")
print("Max:", heap.extract_max(), "Heap:", heap.heap)
print("Max:", heap.extract_max(), "Heap:", heap.heap)


print("\nGetting max values, without extraction:")
print("Max:", heap.get_max(), "Heap:", heap.heap)
print("Max:", heap.get_max(), "Heap:", heap.heap)



# Reinserting for remove test
for val in [30, 25, 40, 10]:
    heap.insert(val)
heap.printHeap()
print("\nCurrent size of heap: ", heap.size())

print("\nGetting max values, without extraction:")
print("Max:", heap.get_max(), "Heap:", heap.heap)


print("\nHeap before removing index 1:", heap.heap)
removed = heap.remove(1)
print(f"Removed value at index 1: {removed}")
print("Heap after removal:", heap.heap)


underOrderedList = MaxHeap()
underOrderedList.heap = [15, 10, 20, 17, 8, 31, 124, 5, 12, 5]
underOrderedList.printHeap()

print("\nHeapifying an Unordered List")
underOrderedList.heapify()
underOrderedList.printHeap()


heap1 = MaxHeap()
heap1.heap = [15, 10, 20, 17, 8, 31, 124, 5, 12]

print("Original Heap:")
heap1.printHeap()

sorted_list = heap1.heapsort()
print("Heapsorted List (ascending):", sorted_list)

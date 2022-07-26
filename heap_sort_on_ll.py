class Heap:
	
	@staticmethod
	def heapify(arr,size,root):
		largest = root
		left = 2 * root + 1
		right = 2 * root + 2

		if(left < size and arr[largest] < arr[left]):
			largest = left

		if(right < size and arr[largest] < arr[right]):
			largest = right

		if(largest != root):
			arr[largest],arr[root] = arr[root],arr[largest]
			Heap.heapify(arr, size, largest)


	@staticmethod
	def sort(arr):
		size=len(arr)

		for i in range(size//2-1, -1, -1):
			Heap.heapify(arr, size, i)

		for i in range(size-1,0,-1):
			arr[i],arr[0] = arr[0],arr[i]
			Heap.heapify(arr,i-1,0)


	def printHeap(arr):
		print(" ".join([str(i) for i in arr]))
		


arr=[4,5,7,2,3,4,7]

Heap.sort(arr)

Heap.printHeap(arr)








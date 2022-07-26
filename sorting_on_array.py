
class Solution:
	def QuickSort(self,arr,low,high):
		if(high < low):
			return

		p = self.partition(arr,low,high)

		self.QuickSort(arr,low,p-1)
		self.QuickSort(arr,p+1,high)

	def partition(self,arr,low,high):
		pi=arr[high]

		i=low-1

		for j in range(low, high):
			if(arr[j] < pi):
				i+=1
				arr[i],arr[j] = arr[j],arr[i]

		arr[i+1],arr[high] = arr[high],arr[i+1]

		return i+1

	def selectionSort(self,arr):
		pos=0
		min_index=0
		l=len(arr)

		while(pos < l):
			min_index=pos
			for i in range(pos,l):
				if(arr[i] < arr[min_index]):
					min_index=i
			arr[min_index],arr[pos] = arr[pos],arr[min_index]
			pos+=1


	def insertionSort(self,arr):

		for i in range(1,len(arr)):
			j=i
			while(j>0 and arr[j] < arr[j-1]):
				arr[j],arr[j-1]=arr[j-1],arr[j]
				j-=1

	def bubbleSort(self,arr):

		l=len(arr)

		for i in range(l):
			for j in range(0,l-i-1):
				if(arr[j] > arr[j+1]):
					arr[j],arr[j+1] = arr[j+1],arr[j]




a=[10,80,30,90,40,50,70]

# Solution().QuickSort(a,0,len(a)-1)

# print("Selection sort")
# Solution().selectionSort(a)


print("Insertion sort")
Solution().insertionSort(a)

# print("Bubble sort")
# Solution().bubbleSort(a)

for i in range(len(a)):
	print(a[i],end=" ")



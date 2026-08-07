class LinearSearch:
    
    def search(self, arr, key):
        for i in range(len(arr)):
            if arr[i] == key:
                return i
        return -1


# Main Program
obj = LinearSearch()

arr = list(map(int, input("Enter the elements: ").split()))
key = int(input("Enter the element to search: "))

result = obj.search(arr, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
  ## time complexity :o(n)
## space complexity:o(1)


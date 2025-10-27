def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive sort
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge two sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        arr.append(val)

    print("\nUnsorted List:", arr)
    merge_sort(arr)
    print("Sorted List (Ascending Order):", arr)

if __name__ == "__main__":
    main()

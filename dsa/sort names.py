def sort_number(names):
    n = len(names)
    # Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if names[j] > names[j + 1]:
                # Swap the elements
                names[j], names[j + 1] = names[j + 1], names[j]     
    return names
if __name__ == "__main__":
    num = ["John", "Alice", "Bob", "Diana", "Charlie"]
    sorted_names =sort_number(names=num)
    print("Sorted Names:", sorted_names)
    
# linear search
def linear_search(data:list, element):
    for index, num in enumerate(data):
        if num == element:
            return index
    return "Element is not found in parsed array !"

# Binary search
# works only on sorted array


def binary_search(data:list, element, start, stop):
    middle_element = (start + stop) // 2
    if stop >= start and len(data) != middle_element:
            if element == data[middle_element]:
                return middle_element
            elif element > data[middle_element]:
                return binary_search(data, element, start=middle_element+1, stop=len(data))
            else:
                return binary_search(data[:middle_element], element, start=0, stop=middle_element)
    else:
        return "Element is not found in parsed array !"


if __name__ == "__main__":
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    find = binary_search(dataset, 10, 0, len(dataset))
    print(find)

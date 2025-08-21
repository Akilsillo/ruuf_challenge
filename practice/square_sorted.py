def square_array(array: list[int])->list[int]:
    left = 0
    right = len(array) - 1
    squares_array = []
    while left <= right:
        if abs(array[left]) < abs(array[right]):
            num = array[right] ** 2
            squares_array.append(num)
            right -= 1
        else:
            num = array[left] ** 2
            squares_array.append(num)
            left += 1

    squares_array.reverse()
    return squares_array

print(square_array([-4, -2, 0, 1, 3]))

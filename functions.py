# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3):
    return max(num1, num2, num3)
    
print(max_num(100, 289, 4))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for i in numbers:
        result = result * i
    return result

print(mult_list([1, 2, 3, 4]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]

print(rev_string('hello world'))

# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(target, start, end):
    return target in range(start, end+1)

print(num_within(3,2,4))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1]], [1, 1]
def pascal(n):
    if n  < 1:
        print('NO')
    elif n == 1:
        print(triangle[0])
    else: 
        row_number = 2
        while len(triangle) < n:
            row = []
            prev_row = triangle[row_number - 1]

            length = len(prev_row) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    value = triangle[row_number - 1][i - 1] + triangle[row_number - 1][i]
                    row.append(value)
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(row)

pascal(2)
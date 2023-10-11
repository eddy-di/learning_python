# l = []
# 
# l.append(1)
# print(l)
# 
# l.append([2])
# print(l)
# 
# l[1].append([3])
# print(l)
# 
# l[1][1].append([4])
# print(l)
# 
# l[1][1][1].append([5])
# print(l)

# def generate_nested_lists(n):
    # result = [n]
    # for i in range(n-1, 0, -1):
        # result = [i, result]
    # return result
# 
# Generate the nested lists with different levels
# for i in range(1, 10):
    # result = generate_nested_lists(i)
    # print(result)


def generate_nested_lists(values):
    if not values:
        return None
    result = values[:-1]
    for val in values[:-1][::-1]:
        result = [val, result]
    return result

# Generate nested lists with different values
values_list = [1, "two", [3, 4], "five", (6, 7)]

for values in values_list:
    result = generate_nested_lists(values)
    print(result)

def multiply_by2(li):
    new_list = []
    print('this is the list stuff: ', li)
    for item in li:
        new_list.append(item*2)
    return new_list


nums = [1, 2, 3, 4]
print(multiply_by2(nums))
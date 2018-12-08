file = open("input.txt")
input = file.read()
file.close()

nums = []
prev = ''
for index in range(len(input)):
    if input[index] == '\n':
        if prev != '':
            nums.append(int(prev))
        continue
    elif input[index] == ' ':
        prev = ''
        continue
    if input[index+1] != ' ':
        prev += input[index]
    elif input[index-1] != ' ':
        nums.append(int(prev + input[index]))
        prev = ''
    else:
        nums.append(int(input[index]))
        prev = ''


def get_childs_metadata(root_index, number_list):

    meta_sum = 0
    if number_list[root_index] == 0:
        meta_n = number_list[root_index + 1]
        total_meta = 0
        for i in range(meta_n):
            total_meta += number_list[root_index + 1 + (i + 1)]
        next_index = root_index + 1 + meta_n + 1
        return total_meta, next_index

    else:
        child_n = number_list[root_index]
        meta_n = number_list[root_index + 1]
        total_meta = 0
        next_child_index = root_index + 2
        for i in range(child_n):
            meta, next_child_index = get_childs_metadata(next_child_index, number_list)
            total_meta += meta
        for i in range(meta_n):
            total_meta += number_list[next_child_index + i]
        next_index = next_child_index + meta_n
        return total_meta, next_index


meta_total, end_index = get_childs_metadata(0, nums)
print(meta_total)
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
        childs_indexes = []
        for i in range(child_n):
            childs_indexes.append((i, next_child_index))
            meta, next_child_index = get_childs_metadata(next_child_index, number_list)
        for i in range(meta_n):
            child_meta_relative_index = number_list[next_child_index + i] - 1
            if child_meta_relative_index >= child_n:
                continue
            child_meta_real_index = child_meta_relative_index
            for entry in childs_indexes:
                if entry[0] == child_meta_relative_index:
                    child_meta_real_index = entry[1]
                    break
            child_meta, ignore_index = get_childs_metadata(child_meta_real_index, number_list)
            total_meta += child_meta
        next_index = next_child_index + meta_n
        return total_meta, next_index


meta_total, end_index = get_childs_metadata(0, nums)
print(meta_total)
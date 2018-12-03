import re
matrix = []
m_side = 1500
for i in range(m_side):
    for j in range(m_side):
        matrix.append('.')

file = open("input.txt")

overlapping = 0
for line in file:
    id = re.search("(#)([0-9]*)(\s@) ", line).group(2)
    left_offset = int(re.search("(@\s)(.*)(,)", line).group(2))
    top_offset = int(re.search("(,)(.*)(:)", line).group(2))
    width = int(re.search("(:\s)(.*)(x)", line).group(2))
    height = int(re.search("(x)(.*)", line).group(2))

    for i in range(height):
        for j in range(width):
            ele = matrix[(top_offset + i)*m_side + left_offset + j]
            if ele == '.':
                matrix[(top_offset + i) * m_side + left_offset + j] = id
            elif ele == 'X':
                continue
            else:
                matrix[(top_offset + i) * m_side + left_offset + j] = 'X'
                overlapping += 1

print overlapping

# 24479 not the answer
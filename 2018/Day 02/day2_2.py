boxes = []

f = open("input.txt")
for line in f:
    boxes.append(line[:len(line)-1:])
f.close()

finish = False
for id1 in boxes:
    for id2 in boxes:
        if id1 == id2:
            continue
        common_letters = ''
        diff_letters = 0
        wrongID = False

        for i in range(len(id1)):
            if id1[i] != id2[i]:
                diff_letters += 1
            else:
                common_letters += id1[i]

            if diff_letters > 1:
                print "Wrong match: ", id1, id2
                wrongID = True
                break

        if wrongID:
            continue

        print common_letters
        finish = True
        break
    if finish:
        break






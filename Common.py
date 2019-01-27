import csv

left_wing = open("left_wing.csv", "r")
right_wing = open("right_wing.csv", "r")

left_reader = csv.reader(left_wing, delimiter=',')
right_reader = csv.reader(right_wing, delimiter=',')

overlap = []
left_line_count = 0
right_line_count = 0
#left_compare
for left_row in left_reader:
    if left_line_count == 0:
        left_line_count+=1
        continue
    if left_row == []:
        continue
    for right_row in right_reader:
        if right_line_count == 0:
            right_line_count += 1
            continue
        if right_wing == []:
            continue
        if left_row[1] == right_row[1]:
            overlap += left_row[1]
            right_line_count += 1
            left_line_count += 1


left_line_count = 0
right_line_count = 0
#right compare
for right_row in right_reader:
    if right_line_count == 0:
        right_line_count += 1
        continue
    for left_row in left_reader:
        if left_line_count == 0:
            left_line_count+=1
            continue

        if left_row[1] == right_row[1]:
            if left_row[1] not in overlap:
                overlap += left_row[1]
            right_line_count += 1
            left_line_count += 1
print(overlap)
file_name_1 = 'test_file_1.txt'
file_name_2 = 'test_file_2.txt'

set_1 = set()
repeats_1 = {}
count_1 = 0
with open(file_name_1) as file:
    for line in file:
        line = line.strip()
        count_1 = count_1 + 1
        if line in set_1:
            repeat_count = 1
            if line in repeats_1:
               repeat_count = repeats_1[line] + 1
            repeats_1[line] = repeat_count
        set_1.add(line)

set_2 = set()
repeats_2 = {}
count_2 = 0
with open(file_name_2) as file:
    for line in file:
        line = line.strip()
        count_2 = count_2 + 1
        if line in set_2:
            repeat_count = 2
            if line in repeats_2:
               repeat_count = repeats_2[line] + 1
            repeats_2[line] = repeat_count
        set_2.add(line)

# Items from File 1 not in File 2
diff = [item for item in set_1 if item not in set_2]
print('*********** File: %s *************' % file_name_1);
print('Total: %d, Unique: %d,  Repeats: %d, Diff: %d' % (count_1, len(set_1), len(repeats_1), len(diff)))
print('ITEMS NOT IN %s >>>>>>' % file_name_2)
print('\n'.join(diff))
print('REPEAT FREQUENCIES >>>>>>')
print(repeats_1)

# Items from File 2 not in File 1
diff = [item for item in set_2 if item not in set_1]
print('*********** File: %s *************' % file_name_2)
print('Total: %d, Unique: %d,  Repeats: %d, Diff: %d' % (count_2, len(set_2), len(repeats_2), len(diff)))
print('ITEMS NOT IN %s >>>>>>' % file_name_1)
print('\n'.join(diff))
print('REPEAT FREQUENCIES >>>>>>')
print(repeats_2)

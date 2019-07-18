items_1 = []

file1 = open("test_file_1.txt", "w")
n = 100
for x in range(350000):
    n = n + 1
    if x > 0 :
        file1.write('\n')
    file1.write(str(n))

file2 = open("test_file_2.txt", "w")
n = 120
for x in range(350000):
    n = n + 1
    if x > 0:
        file2.write('\n')
    file2.write(str(n))
file2.write('\n')
file2.write('11')
file2.write('\n')
file2.write('10\n')
file2.write('11\n')
file2.write('10\n')
file2.write('10\n')
file2.write('10\n')
file2.write('13')


import sys
import csv

#Get the name of the export file from the command line
filename = sys.argv[1]
#Get the number of rows per chunk from the command line
row_lim = int(sys.argv[2])

with open (filename, 'rU') as csv_to_split:
    reader = csv.reader(csv_to_split)
    header = next(reader)
    chunk = [header]
    file_chunks = []
    row_num = 1
    file_num = 1
    for row in reader:
        if row_num < row_lim:
            chunk.append(row)
            row_num = row_num + 1
        else:
            chunk.append(row)
            file_chunks.append(chunk)
            row_num = 1
            chunk = [header]
    if len(chunk) > 0:
        file_chunks.append(chunk)

for i, chunk in enumerate(file_chunks):
    cur_filename = filename[:-4]+'_part_' + str(i+1)+'.csv'
    cur_file = open(cur_filename, 'wb')
    writer = csv.writer(cur_file)
    writer.writerows(chunk)
    cur_file.close

print "Complete; " + str(i+1) + " files created."

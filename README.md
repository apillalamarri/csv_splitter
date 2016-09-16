# csv_splitter

This script splits a csv into chunks of a given number of rows each,
each with the header from the original csv

To run it, type:
python csv_splitter.py <csv filename> <number of rows per chunk>

For example:
Suppose big_file.csv has 100000 rows. To run this script and split big_file.csv into <=30000 row chunks,
put csv_splitter.py big_file.csv into a directory.

Then type:
python csv_splitter.py big_file.csv 30000

on the command line.

This will create four files called:

big_file_part_1.csv, big_file_part_2.csv, big_file_part_3.csv, and big_file_part_4.csv

in the same directory as csv_splitter.py and big_file.csv

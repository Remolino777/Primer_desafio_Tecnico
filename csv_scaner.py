import csv

path = 'data\Housing_clean.csv'

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
            
def find_error(file_path, target_value):
    target_str = str(target_value)
    for index, line in enumerate(read_large_file(file_path)):
        if target_str in line:
            yield index
            
for error_line in find_error(path, 8.787220328629298):
    print(f'the value is in: {error_line}')
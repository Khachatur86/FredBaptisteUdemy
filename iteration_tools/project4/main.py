import constants
import parse_utils
import itertools
from datetime import datetime
# for fname in constants.fnames:
#   print(fname)
#   with open(fname) as f:
#     print(next(f))
#     print(next(f))
#     print(next(f))
#   print

# for fname in constants.fnames:
#   print(fname)
#   with open(fname) as f:
#     reader = csv.reader(f, delimiter=",", quotechar='|')
#     print(next(reader))
#     print(next(reader))
#   print()

# header row (fields name)

# for fname in constants.fnames:
#   print(fname)
#   reader = parse_utils.csv_parser(fname, include_header=True)
#   print(next(reader), end="\n")
#   # print(next(reader))

# # just the data

# for fname in constants.fnames:
#   print(fname)
#   reader = parse_utils.csv_parser(fname)
#   print(next(reader))
#   print(next(reader), end="\n")
#   # print(next(reader))

# reader = parse_utils.csv_parser(constants.fname_update_status)
# for _ in range(3):
#   record = next(reader)
#   record = [str(record[0]), parse_utils.parse_date(record[1]), parse_utils.parse_date(record[2])]
#   print(record)

# for fname, class_name, parser in zip(constants.fnames, constants.class_names, constants.parsers):
#   file_iter = parse_utils.iter_file(fname, class_name, parser)
#   print(fname)
#   for _ in range(3):
#     print(next(file_iter))

# gen = parse_utils.iter_combined_plain_tuple(constants.fnames, constants.class_names, 
#                                         constants.parsers, constants.compress_fields)
                                      

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# print(parse_utils.create_combo_named_tuple_class(constants.fnames, constants.compress_fields)._fields)

data_iter = parse_utils.iter_combined(constants.fnames, constants.class_names, \
                                      constants.parsers, constants.compress_fields)

# print(next(data_iter))
# print(next(data_iter))

for row in itertools.islice(data_iter, 5):
  print(row, "\n")

print('--------------------------')

cutoff_date = datetime(2018,2, 1)
def group_key(item):
  return item.gender, item.vehicle_make

data = parse_utils.filtered_iter_combined(constants.fnames, constants.class_names, \
                                      constants.parsers, constants.compress_fields, key=lambda row: row.last_updated >= cutoff_date)

sorted_data = sorted(data, key=group_key)
print(sorted_data)
# groups = itertools.groupby(sorted_data,)
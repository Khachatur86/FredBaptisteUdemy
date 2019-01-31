import constants
import csv
# for fname in constants.fnames:
#   print(fname)
#   with open(fname) as f:
#     print(next(f))
#     print(next(f))
#     print(next(f))
#   print

for fname in constants.fnames:
  print(fname)
  with open(fname) as f:
    reader = csv.reader(f, delimiter=",", quotechar='|')
    print(next(reader))
    print(next(reader))
  print()
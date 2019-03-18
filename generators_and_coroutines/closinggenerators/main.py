
from inspect import getgeneratorstate

import csv
## 1 Example

# def parse_file(f_name):
#   print('opening file...')
#   f = open(f_name, 'r')
#   try:
#     print(11)
#     dialect = csv.Sniffer().sniff(f.read(2000))
#     f.seek(0)
#     reader = csv.reader(f, dialect=dialect)
#     for row in reader:
#       yield row
        
#   finally:
#     print('closing file...')
#     f.close()

import itertools

# parser = parse_file('cars.csv')
# for row in itertools.islice(parser, 10):
  # print(row)
# 
# parser.close()


## 2 Example 

# def parse_file(f_name):
#   print('opening file...')
#   f = open(f_name, 'r')
#   try:
#     print(11)
#     dialect = csv.Sniffer().sniff(f.read(2000))
#     f.seek(0)
#     reader = csv.reader(f, dialect=dialect)
#     for row in reader:
#       yield row
#   except Exception as ex:
#     print('some exception occured', str(ex))
#   except GeneratorExit:
#     print('Generator was closed')
#   finally:
#     print('closing file...')
#     f.close()

# parser = parse_file('cars.csv')
# for row in itertools.islice(parser, 10):
#   print(row)

# parser.close()

## 3 Example

# def parse_file(f_name):
#   print('opening file...')
#   f = open(f_name, 'r')
#   try:
#     print(11)
#     dialect = csv.Sniffer().sniff(f.read(2000))
#     f.seek(0)
#     next(f) # skip header row
#     reader = csv.reader(f, dialect=dialect)
#     for row in reader:
#       try:
#         yield row
#       except GeneratorExit:
#         print('ignoring call to close generator...')
#   finally:
#     print('closing file...')
#     f.close()

# parser = parse_file('cars.csv')
# for row in itertools.islice(parser, 10):
#   print(row)

# parser.close()

## 4 Example

# def parse_file(f_name):
#   print('opening file...')
#   f = open(f_name, 'r')
#   try:
#     print(11)
#     dialect = csv.Sniffer().sniff(f.read(2000))
#     f.seek(0)
#     next(f) # skip header row
#     reader = csv.reader(f, dialect=dialect)
#     for row in reader:
#       try:
#         yield row
#       except GeneratorExit:
#         print('got all to close generator...')
#         raise ValueError
        
#   finally:
#     print('closing file...')
#     f.close()

# parser = parse_file('cars.csv')
# for row in itertools.islice(parser, 10):
#   print(row)

# parser.close()

def save_to_db():
  print('starting new transaction')
  try:
    while True:
      try:
        data = yield
        print(1)
        print('sending data to database:', eval(data))
      # except Exception:
      #   print('aborting transaction')

      except GeneratorExit:
        print('committing transaction')
        # raise
  except:
    raise
  else:
    pass
  finally:
    print('aborting transaction')
      
trans = save_to_db()

next(trans)
trans.send('1+10')
trans.send('1 / 0')
#trans.send('1+8')
## # trans.close()

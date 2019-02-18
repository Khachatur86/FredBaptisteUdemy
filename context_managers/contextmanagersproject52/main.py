f_names = 'cars.csv', 'personal_info.csv'

for f_name in f_names:
  with open(f_name) as f:
    print(next(f), end='')
    print(next(f), end='')
  print('\n--------------------')

import csv
from itertools import islice

with open(f_names[0]) as f:
  dialect = csv.Sniffer().sniff(f.read(1000))


def get_dialect(f_name):
  with open(f_name) as f:
    return csv.Sniffer().sniff(f.read(1000))

from collections import namedtuple

class FileParser:
  def __init__(self, f_name):
    self.f_name = f_name
  
  def __enter__(self):
    self._f = open(self.f_name, 'r')
    self._reader = csv.reader(self._f, get_dialect(self.f_name))
    headers = map(lambda s: s.lower(),next(self._reader))
    self._nt = namedtuple('Data', headers)
    return self

  def __exit__(self, exc_type, exc_value, exc_tb):
    self._f.close()
    return False

  def __iter__(self):
    return self
  
  def __next__(self):
    if self._f.closed:
      raise StopIteration
    else:
      return self._nt(*next(self._reader))

def parsed_data_iter(data_iter, nt):
  for row in data_iter:
    yield nt(*row)

from contextlib import contextmanager
@contextmanager
def parsed_data(f_name):
  def get_dialect(f_name):
    with open(f_name) as f:
      return csv.Sniffer().sniff(f.read(1000))

  def parsed_data_iter(data_iter, nt):
    for row in data_iter:
      yield nt(*row)

  f = open(f_name, 'r')

  try:
    reader = csv.reader(f, get_dialect(f_name))
    headers = map(lambda s: s.lower(), next(reader))
    nt = namedtuple('Data', headers)
    yield (nt(*row) for row in reader)
  finally:
    f.close()


with parsed_data('personal_info.csv') as data:
  for row in islice(data, 5):
    print(row)
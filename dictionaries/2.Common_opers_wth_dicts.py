d = dict(zip('abc', range(1, 4)))
print(d)
print(d.get('python'))

print(d.get('python', 'N/A'))

text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium'
counts = dict()

for c in text:
  counts[c] = counts.get(c, 0) + 1

print(counts)

counts = dict()

for c in text:
  key = c.lower().strip()
  if key:
    counts[key] = counts.get(key, 0) + 1
  
print(counts)


d = dict(a=1, b=2, c=3)

print('a' in d)
print('z' in d)

d = dict.fromkeys('abcd', 0)
print(d)

del d['a']

print(d)

result = d.pop('b', 99)
print(result)
print(d)

d = dict({i: i**2 for i in range(1, 5)})

print(d)

print(d.popitem())

print(d)

d = {'a':1, 
    'b': 2,
    'c': 1 }

if 'z' not in d:
  d['z'] = 0

print(d)

if 'z' not in d:
  d['z'] = 110

print(d)

def insert_if_not_present(d, key, value):
  if key not in d:
    d[key] = value
    return value
  else:
    return d[key]


### Setdefault

d = dict(zip('abc', range(1, 4)))
print(d)

print(d.setdefault('a', 100))
print(d.setdefault('x', 100))
print(d)


text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?'
counts = dict()
for c in text:
    counts[c] = counts.get(c, 0) + 1
print(counts)
import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)


categories = {}

for c in text:
  if c != ' ':
    if c in string.ascii_lowercase:
      key = 'lower'
    elif c in string.ascii_uppercase:
      key='upper'
    else:
      key = 'other'
    if key not in categories:
      categories[key] = set()
    
    categories[key].add(c)


from pprint import pprint
pprint(categories)
for cat in categories:
  print(f'{cat}: ', ''.join(categories[cat]))

categories = {}

for c in text:
  if c != ' ':
    if c in string.ascii_lowercase:
      key = 'lower'
    elif c in string.ascii_uppercase:
      key = 'upper'
    else:
      key = 'other'

    categories.setdefault(key, set()).add(c)

for cat in categories:
  print(f'{cat}: ', ''.join(categories[cat]))



def cat_key(c):
  if c == ' ':
    return None
  elif c in string.ascii_lowercase:
    return 'lower'
  elif c in string.ascii_uppercase:
    return 'upper'
  else:
    return 'other'
  

categories = {}

for c in text:
  key = cat_key(c)
  if key:
    categories.setdefault(key, set()).add(c)

for cat in categories:
  print(f'{cat}: ', ''.join(categories[cat]))

def cat_key(c):
  categories = {
    ' ': None,
    string.ascii_lowercase: 'lower',
    string.ascii_uppercase: 'upper'
  }
  for key in categories:
    if c in key:
      return categories[key]
  else:
    return 'other'


print(cat_key('D'))
print(cat_key('4'))
print(cat_key('d'))
print(cat_key('df'))


from itertools import chain

def cat_key(c):
  cat_1 = {' ': None}
  cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower')
  cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')
  categories = dict(chain(cat_1.items(), cat_2.items(), cat_3.items()))
  return categories.get(c, 'other')
  
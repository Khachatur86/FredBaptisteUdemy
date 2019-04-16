# creating sets

s = {'a', 100, (1, 2)}

print(type(s))

s = set(range(10))
print(s)

# every element in sets have to be hashable

d = {
  'a': 1,
  'b': 2
}

print('set(d) - ', set(d))

print({c for c in 'python'})

s1 = {'a', 'b', 'c'}
s2 = {10, 20, 30}

s = {*s1, *s2}
print(s)

s1 = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}

s = {*s1, *s2}
print(s)

def my_func(a, b, c):
  print(a, b, c)

args = {20, 10, 30}

my_func(*args)
my_func(*args)
my_func(*args)

def averager(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)

print(averager(*args))

s = set('baabaa')
print(s)



s = {c for c in 'moomoo'}
print(s)

s = 'abcdefghijklmnopqrstuvwxyz'
distinct = set(s)
print(distinct)
score = len(s) / 26
print(score)


def scorer(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    distinct = set(s)
    # we want to only count characters that are in our alphabet
    effective = distinct & alphabet
    print('effective',effective)
    return len(effective) / len(alphabet)

print(scorer(s))
print(scorer('baa baa'))
print(scorer('baa ba56, sdfa'))
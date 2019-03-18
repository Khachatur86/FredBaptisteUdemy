# def squares(n):
#   for i in range(n):
#     yield i ** 2

# def delegator(n):
#   for value in squares(n):
#     yield value


# gen = delegator(5)
# for _ in range(5):
#   print(next(gen))

# def delegator(n):
#   yield from squares(n)

# gen = delegator(5)
# for _ in range(5):
#   print(next(gen))


from inspect import getgeneratorstate, getgeneratorlocals

def song():
  yield "I am a lumberjack and I am OK"
  yield "I sleep all night and I work all day"

def play_song():
  count = 0
  s = song()
  yield from s
  yield "song finished"
  print('player is exiting...')

player = play_song()
print(getgeneratorstate(player))
print(getgeneratorlocals(player))
print(next(player))
print('After first next')
print(getgeneratorstate(player))
print(getgeneratorlocals(player))
s = getgeneratorlocals(player)['s']
print(getgeneratorstate(s))
print(next(player))
print(getgeneratorstate(player))
print(getgeneratorstate(s))
print(next(player))
print(getgeneratorstate(player))
print(getgeneratorstate(s))
# print(next(player))

def player():
  print('asdf')
  count = 1
  while True:
    print('Run count:', count)
    yield from song()
    count += 1

p = player()

print(next(p),'\n',next(p))
print(next(p),'\n',next(p))
print(next(p),'\n',next(p))
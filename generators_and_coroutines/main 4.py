# print('Ex1')
# # Ex1
# def gen():
#   try:
#     while True:
#       received = yield
#       print(received)
#   finally:
#     print('exception must have happened')

# g = gen()
# next(g)

# g.send('hello')
# # g.throw(ValueError, 'custom message')

# print('\nEx2')
# # Ex2
# def gen():
#   try:
#     while True:
#       recieved = yield
#       print(recieved)
#   except ValueError:
#     print('recieved a value error...')
#   finally:
#     print('exception must have happened')

# g = gen()
# next(g)
# g.send('hello')
# g.throw(ValueError, 'custom message')

# # Ex3

# print('\nEx3')
from inspect import getgeneratorstate

# def gen():
#   while True:
#     try:
#       received = yield
#       print(received)
#     except ValueError as ex:
#       print('Value error received: ', str(ex))


# g = gen()
# next(g)
# g.send('hello')
# g.throw(ValueError, 'custom message')
# print(getgeneratorstate(g))
# g.send('python')
# g.send('Khachatur')

# def gen():
#   while True:
#     received = yield
#     print(received)

# g = gen()
# next(g)
# g.send('hello')
# g.throw(ValueError, 'custom message')
# print(getgeneratorstate(g))

# def gen():
#   try:
#     while True:
#       received = yield
#       print(received)
#   except ValueError as ex:
#     print('ValueError received', str(ex))
#     return None

# g = gen()
# next(g)
# g.send('hello')
# g.throw(ValueError, 'custom message')

# def gen():
#   try:
#     while True:
#       received = yield
#       print(received)
#   except ValueError as ex:
#     print('ValueError received...', str(ex))
#     raise ZeroDivisionError('not really!')

# g = gen()
# next(g)
# g.send('hello')
# g.throw(ValueError, 'custom message')

class CommitException(Exception):
  pass

class RollbackException(Exception):
  pass

def write_to_db():
  print('opening database connection...')
  print('start transaction...')
  try:
    while True:
      try:
            
        data = yield
        print('writing data to database...', data)
      except CommitException:
        print('comitting transaction')
        print('opening next transaction...')
      except RollbackException:
        print('aborting transaction...')
        print('opening next transaction...')

  finally:
    print('generator closing...')
    print('abort transaction...')
    print('closing database connection...')

sql = write_to_db()
next(sql)
next(sql)
next(sql)
next(sql)
sql.send(100)
sql.throw(CommitException)
sql.send(200)
sql.throw(RollbackException)
sql.send(200)
sql.close()

# def gen():
#   try:
#     while True:
#       received = yield
#       print(received)
#   finally:
#     print('closing down')
# print('\n___________________________\n')
# g = gen()
# next(g)
# g.close()

# g = gen()
# next(g)
# g.throw(GeneratorExit)

print('\n-----------------------\n')

def gen():
  try:
    while True:
      recieved = yield
      print(recieved)
  except GeneratorExit:
    print('received generator exit...')
  finally:
    print('closing down')

g = gen()
next(g)
# g.close()

g.throw(GeneratorExit)
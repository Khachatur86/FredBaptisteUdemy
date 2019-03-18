from collections import deque

dq = deque([1, 2, 3, 4, 5])

print(dq)

dq.append(100)
print(dq)

dq.appendleft(-10)
print(dq)

print(dq.pop())
print(dq)

print(dq.popleft())
print(dq)

print(len(dq))

dq = deque([1, 2, 3, 4, 5], maxlen=5)

dq.append(100)
print(dq)

dq.appendleft(0)
print(dq)

# def produce_elements(dq):
#   for i in range(1, 36):
#     dq.appendleft(i)

# def consume_elements(dq):
#   while len(dq) > 0:
#     item = dq.pop()
#     print('processing item', item)

# def coordinator():
#   dq = deque()
#   produce_elements(dq)
#   consume_elements(dq)

# coordinator()

def produce_elements(dq, n):
  for i in range(1, n):
    dq.append(i)
    if len(dq) == dq.maxlen:
      print('queue full - yielding control')
      yield

def consume_elements(dq):
  while True:
    while len(dq) > 0:
      print('processing', dq.pop())
    print('queue empty - yielding control')
    yield

def coordinator():
  dq = deque(maxlen=10)
  producer = produce_elements(dq, 36)
  consumer = consume_elements(dq)
  while True:
    try:
      print('producing ...')
      next(producer)
    except StopIteration:
      # producer finished
      break
    finally:
      print('consuming...')
      next(consumer)
       

coordinator()
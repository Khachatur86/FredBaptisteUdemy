# with open("test.txt", "w") as file:
#   print("inside with: file closed?", file.closed)

# print("after with: file closed?", file.closed)


# def test():
#   with open ('test.txt', "w") as file:
#     print("inside with: file closed?", file.closed)
#     return file
#     print("here - will never run")

# file = test()
# print(file.closed)

# # with open("test.txt", "w") as file:
# #   print("inside with: file closed?", file.closed)
# #   raise ValueError()

# print(file.closed) # Выведете True

# with open("test.txt", "w") as f:
#   f.writelines("this is a test")

# with open('test.txt') as f:
#   row = next(f)

# print(row)

class MyContext:
    def __init__(self):
        print("init running...")
        self.obj = None

    def __enter__(self):
        print("entering context...")
        self.obj = "the Return object"
        return self.obj

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("exiting context...")
        if exc_type:
            print(f"*** Error occurred: {exc_type}, {exc_value} {exc_tb}")
        return True  # False


ctx = MyContext()
print("created context...")
with ctx as obj:
    print("inside with block", obj)
    raise ValueError("custom message")


class Resource:
    def __init__(self, name):
        self.name = name
        self.state = None


class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None

    def __enter__(self):
        print('entering context')
        self.resource = Resource(self.name)
        self.resource.state = "created"
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exiting context')
        self.resource.state = 'destroyed'
        if exc_type:
            print('error occurred')
        return False


with ResourceManager('spam') as res:
    print(f'{res.name} = {res.state}')

print(f'{res.name} = {res.state}')


class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file...')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('closing file...')
        self.file.close()
        return False


# with File('test1.txt', 'w') as f:
#   f.write('This is a late parrot!')


# with File('test1.txt', 'r') as f
#   print(f.readlines())

def test():
    with File('test2.txt', 'w') as f:
        f.write('This is a Arsen')
        return f


f = test()
print(f.closed)

# import common.validators.boolean
# import common.validators.date
# import common.validators.json
# # import common.validators.numeric
# from common.validators.numeric import is_integer, is_numeric
# import common.validators as validators

import common.validators

from common.validators import *
# import common.models.posts.post
# import common.models.posts.posts
# Вместо двух импортов выше запишем ниже
# import common.models.posts

# import common.models.users.user
# import common.models.users
import common.models
# print(globals())
common.validators.is_boolean("daf")
common.validators.json.is_json("{}")
common.validators.date.is_date("2018-01-01")
is_numeric(10)
is_integer("100")
# john_post = common.models.posts.post.Post()
john_post = common.models.Post()
# john_posts = common.models.posts.posts.Posts()
john_posts = common.models.Posts()
john = common.models.users.user.User()

# common.validators.is_numeric(10)
# common.validators.is_integer("100")
print("\n\n***** self *****")
# for k in globals().keys(): # выдает ошибку, так как каждый раз значение переменной k в globals() переопределяется в каждой итерации
#   print(k)

for k in dict(globals()).keys(): 
  print(k)

#   ***** self *****
# __name__
# __doc__
# __package__
# __loader__
# __spec__
# __annotations__
# __builtins__
# signal
# __file__
# __cached__
# common

print("\n\n ***** common *****")
for k in common.__dict__.keys():
  print(k)


#  ***** common *****
# __name__
# __doc__
# __package__
# __loader__
# __spec__
# __path__
# __file__
# __cached__
# __builtins__
# validators

print("\n\n ***** validators *****")
for k in common.validators.__dict__.keys():
  print(k)


#  ***** common *****
# __name__
# __doc__
# __package__
# __loader__
# __spec__
# __path__
# __file__
# __cached__
# __builtins__
# validators

print("\n\n ***** numeric *****")
for k in common.validators.numeric.__dict__.keys():
  print(k)

#  ***** numeric *****
# __name__
# __doc__
# __package__
# __loader__
# __spec__
# __file__
# __cached__
# __builtins__
# is_integer
# is_numeric
# numeric_helper_1
# numeric_helper_2

print("\n\n ***** models *****")
for k in common.models.__dict__.keys():
  print(k)

print("\n\n ***** posts (package) *****")
for k in common.models.posts.__dict__.keys():
  print(k)
# import common.validators.boolean
# import common.validators.date
# import common.validators.json
# import common.validators.numeric
# from common.validators.numeric import is_integer, is_numeric
# import common.validators as validators


# print(list(validators.numeric.__dict__))
import common.validators
import sys
print(list(sys.modules))
# from common.validators import *
# import common.models.posts.post
# import common.models.posts.posts
# Вместо двух импортов выше запишем ниже
# import common.models.posts

# import common.models.users.user
# import common.models.users
# import common.models
# print(globals())
# common.validators.is_boolean("daf")
# common.validators.json.is_json("{}")
# common.validators.date.is_date("2018-01-01")
# validators.numeric.numeric_helper_1()# is_integer("100")
# john_post = common.models.posts.post.Post()
# john_post = common.models.Post()
# # john_posts = common.models.posts.posts.Posts()
# john_posts = common.models.Posts()
# john = common.models.users.user.User()

common.validators.is_numeric(10)
# common.validators.is_integer("100")
print("\n\n***** self *****")
# for k in globals().keys(): # выдает ошибку, так как каждый раз значение переменной k в globals() переопределяется в каждой итерации
#   print(k)

for k in dict(globals()).keys(): 
  print(k)


# print("\n\n ***** common *****")
# for k in common.__dict__.keys():
#   print(k)

#
#
# print("\n\n ***** validators *****")
# for k in validators.__dict__.keys():
#   print(k)
# # #
#
# print("\n\n ***** numeric *****")
# for k in common.validators.numeric.__dict__.keys():
#   print(k)
#
# print("\n\n ***** models *****")
# for k in common.models.__dict__.keys():
#   print(k)
#
# print("\n\n ***** posts (package) *****")
# for k in common.models.posts.__dict__.keys():
#   print(k)
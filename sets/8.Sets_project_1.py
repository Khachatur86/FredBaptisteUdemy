def match_keys(data, valid, path):
  data_keys = data.keys()
  valid_keys = valid.keys()

  extra_keys = data_keys - valid_keys
  missing_keys = valid_keys - data_keys

  if missing_keys or extra_keys:
    missing_msg = ('missing keys: ' + 
                   ','.join({path + '.' + str(key) 
                               for key in missing_keys})) if missing_keys else  ''
    print(missing_msg)
    extras_msg = ('extra keys: ' + 
                  ','.join({path + '.' + str(key)
                             for key in extra_keys})
                  ) if extra_keys else ''
    return False, ' '.join((missing_msg, extras_msg))
  else:
    return True, None


t = {'a': int, 'b': int, 'c': int, 'd': {}, 't': int}

# d = {'a': 'wrong type', 'b': 100, 'c':200, 'd': {'wrong', 'type'}}
d = {'a': None, 'b': None, 'c': None}

ex_k = d.keys() - t.keys()
mi_k = t.keys() - d.keys()
print(ex_k or mi_k)
is_ok, err_msg = match_keys(d, t, 'some.path')
# print(is_ok, err_msg)

def match_types(data, template, path):
  for key, value in template.items():
    if isinstance(value, dict):
      template_type = dict
    else:
      template_type = value
    data_value = data.get(key, object())
    # print(f"data_value - {data_value}, template_type - {template_type}")
    if not isinstance(data_value, template_type):
      err_msg = ('incorrect type: ' + path + '.' + key + 
                                ' -> expected ' + template_type.__name__ + 
                                 ', found ' + type(data_value).__name__)
      return False, err_msg
  return True, None

print('====================================')
t = {'a': int, 'b': str, 'c': {'d': int}}
d = { 'b': 'test', 'a': 100,'c':{'some': 'value'}}
print(match_types(d, t, 'some.path'))


# print(isinstance(bool, type))
# # print(type(object()))
d = { 'b': 'test', 'a': 100,'c': 'unexpected'}
print(match_types(d, t, 'some.path'))

def recurse_validate(data, template, path):
  is_ok, err_msg = match_keys(data, template, path)
  if not is_ok:
    return False, err_msg

  is_ok, err_msg = match_types(data, template, path)
  if not is_ok:
    return False, err_msg

  dictionary_type_keys = {key for key, value in template.items() if isinstance(value, dict)}
  
  for key in dictinary_type_keys:
    sub_path = path + '.' + str(key)
    sub_template = template[key]
    sub_data = data[key]
    is_ok, err_msg = recurse_validate(sub_data, sub_template, sub_path)
    if not is_ok:
      return False, err_msg
  
  return True, None


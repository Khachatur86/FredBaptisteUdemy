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
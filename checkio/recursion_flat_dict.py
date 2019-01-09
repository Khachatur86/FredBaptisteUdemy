def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        print("path - ", path)
        print("current - ",current)
        for k, v in current.items():
            if isinstance(v, dict) and v:
                stack.append((path + (k,), v))
                print("Stack3 - ",stack)
            else:
                result["/".join((path + (k,)))] = v or ""
                print("result - ", result)
    return result

test1 = {"key": {"deeper": {"more": {"enough": "value"}},
                 "deeper2": 2,
                  "deeper3": {"deeper4": 1}}}

flatten(test1)
# stack = [((), dictionary)]
# print(stack)
# print(stack.pop())
# print(stack)


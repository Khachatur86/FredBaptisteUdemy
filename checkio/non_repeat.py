
def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    results = []
    result = []
    for i in range(len(line)):
        for c in line[i:]:
            if c not in result:
                result.append(c)
            else:
                results.append(''.join(result))
                result = [c]
        results.append(''.join(result))
        result.clear()
    if(len(results)):
        return max(results, key=len)
    return ""
def safe_pawns(pawns: set) -> int:
    safe_coords = [(chr(ord(x[0])-1) + str(int(x[1])-1),\
            chr(ord(x[0])+1) + str(int(x[1])-1)) for x in pawns]
    count = 0
    for pos in safe_coords:
      if pos[0] in pawns or pos[1] in pawns:
        count += 1

    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"b7", "c5", "d4", "e4", "f4", "g8", "e5"}) == 2
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
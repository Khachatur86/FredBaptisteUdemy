def sun_angle(time):
    b = {720 : 180}
    int_time = time.split(':')
    minute = int(int_time[0]) * 60 + int(int_time[1]) - 360
    if 0 <= minute <= 720:
      need_angle = 180 * minute / 720
      return need_angle
    return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
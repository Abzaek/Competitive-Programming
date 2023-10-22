def swap_case(s):
    swaped_s = ''
    for i in s:
        if i.isalnum():
            if i.isupper():
                swaped_s = swaped_s + i.lower()
            else: 
                swaped_s = swaped_s + i.upper()
        else:
            swaped_s = swaped_s + i
    return swaped_s

f __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

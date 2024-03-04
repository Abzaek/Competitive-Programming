for i in range(int(input())):
    a, b = input().split()

    if a[-1] == b[-1]:
        if a[-1] == 'L':
            if len(a) > len(b):
                print('>')
            elif len(a) < len(b):
                print('<')
            else:
                print('=')
        elif a[-1] == 'S':
            if len(a) < len(b):
                print('>')
            elif len(a) > len(b):
                print('<')
            else:
                print('=')
        else:
            print('=')
    else:
        if a[-1] == 'M':
            if b[-1] == 'L':
                print('<')
            else:
                print('>')
        elif a[-1] == 'S':
            print('<')
        else:
            print('>')


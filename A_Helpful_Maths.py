s = input().split('+')

s.sort(key=lambda x: int(x))

print('+'.join(s))
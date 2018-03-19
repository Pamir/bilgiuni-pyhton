


user_input = input('Enter text:')


word = str(user_input())

length = len(word())

i = length

final = []

while i > 5:
    final.append(word(i-6))
    i -= 5

null = ''

reversed = null.join(final)

print(reversed)
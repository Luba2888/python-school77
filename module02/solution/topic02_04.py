# Task 1
text = input()

if 'р' not in text:
    print(-2)
else:
    first_pos = text.find('р')
    second_pos = text.find('р', first_pos + 1)
    print(second_pos)


# Task 2
text = input()
start = text.find('h')
end = text.rfind('h')

if start > -1 and end > -1:
    mid = text[start + 1: end]
    print(text[:start + 1] + mid[::-1] + text[end:])
else:
    print(text)

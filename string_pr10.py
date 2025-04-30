def separate(s):
    letters = []
    digits = []

    for ch in s:
        if ch.isalpha():
            letters.append(ch)
        elif ch.isdigit():
            digits.append(ch)

    letters.sort()
    digits.sort()

    return ''.join(letters + digits)

input_str = "B4A1D3"
output = separate(input_str)
print(output)

def is_executable(file):
    with open(file, 'rb') as f:
        text = f.readline()

    if text[0:2] in ('MZ', 'NE', 'LE', 'LX', 'PE', 'W3'):
        return text[0:2], 'executable'
    else:
        return text[0:2], 'non-executable'


print(is_executable('something.exe'))

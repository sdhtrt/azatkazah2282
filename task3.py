def a(file):
    with open(file) as f:
        text = f.read()

    names = []
    name = ''
    lists = []
    for i in range(text.index('(') + 1, text.index(')')):

        if text[i] == ',':
            names.append(name)
            name = ''
        elif text[i] != ' ':
            name += text[i]

    if name:
        names.append(name)
        name = ''

    words = [i.split() for i in text[text.index(')') + 1:].split('=')]
    for word in range(1, len(words)):
        if words[word] and words[word - 1]:
            if words[word][0][0] in '{([':
                lists.append(words[word - 1][-1])
            elif words[word - 1][-1] in '+-*/%':
                pass
            else:
                names.append(words[word - 1][-1])

    print(names, lists)
    for i in range(len(names)):
        text = text.replace(names[i], 'a' + str(i + 1))
    for i in range(len(lists)):
        text = text.replace(lists[i], 'R' + str(i + 1))
    print(text)

a('function.txt')

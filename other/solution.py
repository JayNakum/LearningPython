PARAGRAPH = '''Welcome Mr. Jay, to my project. A Scene Based OpenGL Renderer(sort of) written in C++. It implements every concept that I have been learning. It's primarily a playground for me to try to implement different graphics programming techniques. I will keep adding new features to this framework as I will learn new topics in future. Eventually, the plan is to create a scene-based engine, where you can load up some model(s), add some fancy lights, and virtually explore it.'''

def splitLines() -> list: 
    lines = []
    line = ''
    for chr in PARAGRAPH:
        line += chr
        if (chr in ['.', '?', '!']):
            if (' ' not in line): continue
            lines.append(line)
            line = ''
    return lines

def splitWords(line:str) -> list:
    words = []
    word = ''
    for chr in line:
        word += chr
        if (chr == ' '):
            words.append(word)
            word = ''
    
    return words


def main():
    lines = splitLines()
    print('-------------------LINES-------------------')
    print(lines)
    print('\n')
    print('-------------------WORDS-------------------')
    for line in lines:
        print(splitWords(line))


if __name__ == '__main__':
    main()

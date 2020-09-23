import re
def checkio(line):
    return " ".join(re.split(' *', line))


if __name__ == '__main__':
    assert checkio('I  like   python') == "I like python", 'Example'

import string
def checkio(data):
    if len(data) < 10:
        return False

    contUpper = contLower = contDigit = False
    for letter in data:
        if letter in string.ascii_uppercase:
            contUpper = True
        elif letter in string.ascii_lowercase:
            contLower = True
        elif letter in string.digits:
            contDigit = True
        if contDigit == contUpper == contLower == True:
            break

    return contDigit and contUpper and contLower


import re
def checkio(data):
    if len(data) >= 10 and re.search(r"[A-Z]", data) and re.search(r"[a-z]", data) and re.search(r"\d", data):
        return True
    return False

def checkio(data):
    return bool(re.search(r"""(?=.*[A-Z])   # After a negative lookahead, the searching resets, so
                              (?=.*[a-z])   # searches the next lookahead
                              (?=.*[\d])    # digits
                              .{10}         # at least 10 character long
    """, data, re.VERBOSE))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('asasasasasasasaaS1') == True, "7th example"

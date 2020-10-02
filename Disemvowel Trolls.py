def disemvowel(string):
    for ch in ['a','o','u','i','e','A','O','U','I','E']:
        if ch in string:
            string = string.replace(ch,'')
    return string
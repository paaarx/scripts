import unicodedata


def remove_accent(text):
    return ''.join(map(chr, unicodedata.normalize('NFKD', text)
                       .encode('ASCII', 'ignore')))

import unicodedata


def normalize_unicode(value):
    return unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')

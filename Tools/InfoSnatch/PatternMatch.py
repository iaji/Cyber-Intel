import re


def IndicatorType(indicator):
    ip_regex = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    md5_regex = r'(?=(\b[A-Fa-f0-9]{32}\b))'
    SHA1_regex = r'\b([a-f0-9]{40})\b'
    SHA256_regex = r'\b[A-Fa-f0-9]{64}\b'
    URL_regex = r'((?:http(?:s)?:\/\/)?)((?:www\.)?[a-zA-Z0-9@:%._\+~#=\-]{2,256}\.[a-z0-9]{2,6}\b)((?:\:\d+)?)((?:[-\w@:%\+.~#&/=]*)?)((?:\?[-\w%\+.~#&=]*)?)'

    if re.match(SHA1_regex, indicator):
        return 'SHA1'
    if re.match(md5_regex, indicator):
        return 'MD5'
    if re.match(SHA256_regex, indicator):
        return 'SHA256'
    if re.match(ip_regex, indicator):
        return 'IPV4'
    if re.match(URL_regex, indicator):
        return 'Domain'

def md5Parse(indicators):

    '''Takes in a text dump and extracts MD5's then stores them in an Array of tuples.  Formatted (TYPE, CONTENT, SOURCE)'''

    md5_regex = r'(?=(\b[A-Fa-f0-9]{32}\b))'
    md5s = re.findall(md5_regex, indicators, re.IGNORECASE | re.MULTILINE)

    if len(md5s) == 0:
        return 'No MD5 hashes'

    elif len(md5s) == 1:
        md5s[0] = ('MD5', md5s[0], 'SOURCE?')
        return md5s

    else:
        for md5 in len(md5s):
            md5 = ('MD5', md5, 'SOURCE')
    return md5s

def sha1Parse(indicators):

    '''Takes in a text dump and extracts SHA1's then stores them in an Array of tuples.  Formatted (TYPE, CONTENT, SOURCE)'''

    SHA1_regex = r'\b([a-f0-9]{40})\b'
    SHA1s = re.findall(SHA1_regex, indicators, re.IGNORECASE | re.MULTILINE)

    if len(SHA1s) == 0:
        return 'No SHA1 hashes'
    elif len(SHA1s) == 1:
        SHA1s[0] = ('SHA1', SHA1s[0], 'SOURCE?')
        return SHA1s
    else:
        for SHA1 in len(SHA1s):
            SHA1 = ('SHA1', SHA1, 'SOURCE?')
    return SHA1s

def sha256Parse(indicators):

    '''Takes in a text dump and extracts SHA256's then stores them in an Array of tuples.  Formatted (TYPE, CONTENT, SOURCE)'''

    SHA256_regex = r'\b[A-Fa-f0-9]{64}\b'
    SHA256s = re.findall(SHA256_regex, indicators, re.IGNORECASE | re.MULTILINE)

    if len(SHA256s) == 0:
        return 'No SHA256 hashes'
    elif len(SHA256s) == 1:
        SHA256s[0] = ('SHA256', SHA256s[0], 'SOURCE?')
        return SHA256s
    else:
        for SHA256 in len(SHA256s):
            SHA256 = ('SHA256', SHA256, 'SOURCE?')
    return SHA256s

def ipParse(indicators):

    '''Takes in a text dump and extracts IP's then stores them in an Array of tuples.  Formatted (TYPE, CONTENT, SOURCE)'''

    ip_regex = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    IPs = re.findall(ip_regex, indicators, re.IGNORECASE | re.MULTILINE)

    if len(IPs) == 0:
        return ['No IPs']
    elif len(IPs) == 1:
        IPs[0] = ('IP', IPs[0], 'SOURCE?')
        return IPs
    else:
        for IP in len(IPs):
            IP = ('IP', IP, 'SOURCE?')
    return IPs

def urlParse(indicators):
    URL_regex = r'((?:http(?:s)?:\/\/)?)((?:www\.)?[a-zA-Z0-9@:%._\+~#=\-]{2,256}\.[a-z0-9]{2,6}\b)((?:\:\d+)?)((?:[-\w@:%\+.~#&/=]*)?)((?:\?[-\w%\+.~#&=]*)?)'
    URLs = re.findall(URL_regex, indicators, re.IGNORECASE | re.MULTILINE)
    print URLs

    if len(URLs) == 0:
        return ['No URLs']

    elif len(URLs) == 1:
        URLs[0] = ('URL', URLs[0], 'SOURCE')
        return URLs
    else:
        for URL in len(URLs):
            URL = ('URL', URL,'SOURCE')
    return URLs

def main():
    indicators = ('hello\n7d7aaa8c9a36324a2c5e9b0a3440344502f28b90776baa6b8dac7ac88a83aef0\n13cdbd8c31155610b628423dc2720419\n2cb8230281b86fa944d3043ae906016c8b5984d9\nwww.google.com/help\nuc.edu')

    ans = md5Parse(indicators) + sha1Parse(indicators) + sha256Parse(indicators) + ipParse(indicators)
    print ans
main()

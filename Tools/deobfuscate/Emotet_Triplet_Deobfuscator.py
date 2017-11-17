import re
import collections

URL_regex = r'((?:http(?:s)?:\/\/)?)((?:www\.)?[a-zA-Z0-9@:%._\+~#=\-]{2,256}\.(?!doc)[a-z]{2,6}\b)((?:\:\d+)?)((?:[-\w@:%\+~#&/=]*)?)((?:\?[-\w%\+.~#&=]*)?)'


def readIn():
    ps = input("Please enter the WHOLE command line:  \n")
    #with open('emoV2ps.txt', 'r' ) as f:
    #    ps = str(f.readlines())
    return ps

def concatstr(s):
    """Makes the command line readable"""
    s = s.replace("\\", "").replace("+", '').replace("''", '')
    totals = freq_count(s)
    while totals[0][1] >= 8:
        s = s.replace(str(totals[0][0]), '')
        totals = freq_count(s)

    return s

def detect_urls(deob_ps):
    URLs = re.findall(URL_regex, deob_ps, re.IGNORECASE | re.MULTILINE)
    '''Domain format: [(protocol, domain, port, extension, paramteres)]'''
    urlstring = ''
    for URL in URLs:
        if URL[0] != '':
            loopnum = 0
            for part in URL:
                loopnum += 1
                urlstring += str(part)
                if loopnum == (len(URL)):
                    urlstring += '\n'
    print(urlstring)


def freq_count(thestring):
    index = 0
    trips = []
    totals = []
    while index <= len(thestring):
        trips.append(thestring[index:index+3])
        index+=1
    d = collections.defaultdict(int)
    for c in trips:
        d[c] += 1
    for c in sorted(d, key=d.get, reverse=True):
        totals.append((c, d[c]))
    return totals

ps = readIn()
out = concatstr(ps)
detect_urls(out)

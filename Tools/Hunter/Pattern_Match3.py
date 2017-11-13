import re
import urllib2
from bs4 import BeautifulSoup
import csv


def Indicator_Type(indicator):
    ip_regex = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    md5_regex = r'(?=(\b[A-Fa-f0-9]{32}\b))'
    SHA1_regex = r'\b([a-f0-9]{40})\b'
    SHA256_regex = r'\b[A-Fa-f0-9]{64}\b'
    URL_regex = r'((?:http(?:s)?:\/\/)?)((?:www\.)?[a-zA-Z0-9@:%._\+~#=\-]{2,256}\.(?!doc)[a-z]{2,6}\b)((?:\:\d+)?)((?:[-\w@:%\+.~#&/=]*)?)((?:\?[-\w%\+.~#&=]*)?)'

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


def md5_parse(indicators, Source):
    '''Takes in a text dump and extracts MD5's then stores them in an Array of
       tuples.  Formatted (TYPE, CONTENT, SOURCE)'''

    md5_regex = r'(?=(\b[A-Fa-f0-9]{32}\b))'
    md5s = re.findall(md5_regex, indicators, re.IGNORECASE | re.MULTILINE)
    md5cnt = 0
    md5Hashes = []
    if len(md5s) == (0 or None):
        return md5Hashes.append(('No MD5s', 'NULL', 'NULL'))

    elif len(md5s) == 1:
        md5s[0] = ('HASH', md5s[0], Source)
        return md5s

    else:
        for md5Cnt in xrange(len(md5s)):
            md5Hashes.append(('HASH', md5s[md5Cnt], Source))
        return md5Hashes


def sha1_parse(indicators, Source):
    '''Takes in a text dump and extracts SHA1's then stores them in an Array of
       tuples.  Formatted (TYPE, CONTENT, SOURCE)'''

    SHA1_regex = r'\b([a-f0-9]{40})\b'
    SHA1s = re.findall(SHA1_regex, indicators, re.IGNORECASE | re.MULTILINE)
    SHA1Hashes = []
    SHA1Cnt = 0
    if (len(SHA1s) or SHA1s) == (0 or None):
        return SHA1Hashes.append(('No SHA1s', 'NULL', 'NULL'))

    elif len(SHA1s) == 1:
        SHA1s[0] = ('HASH', SHA1s[0], Source)
        return SHA1s
    else:
        for SHA1Cnt in xrange(len(SHA1s)):
            SHA1Hashes.append(('HASH', SHA1s[SHA1Cnt], Source))
        return SHA1Hashes


def sha256_parse(indicators, Source):
    '''Takes in a text dump and extracts SHA256's then stores them in an Array
       of tuples.  Formatted (TYPE, CONTENT, SOURCE)'''

    SHA256_regex = r'\b[A-Fa-f0-9]{64}\b'
    SHA256s = re.findall(SHA256_regex, indicators, re.IGNORECASE | re.MULTILINE)
    SHA256Hashes = []
    SHA256Cnt = 0
    if (len(SHA256s) or SHA256s) == (0 or None):
        return SHA256Hashes.append(('No SHA256s', 'NULL', 'NULL'))

    elif len(SHA256s) == 1:
        SHA256s[0] = ('HASH', SHA256s[0], Source)
        return SHA256s
    else:
        for SHA256Cnt in xrange(len(SHA256s)):
            SHA256Hashes.append(('HASH', SHA256s[SHA256Cnt]), Source)
        return SHA256Hashes


def ip_parse(indicators, Source):
    '''Takes in a text dump and extracts IP's then stores them in an Array of
       tuples.  Formatted (TYPE, CONTENT, SOURCE)'''

    ip_regex = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    IPs = re.findall(ip_regex, indicators, re.IGNORECASE | re.MULTILINE)
    IPCnt = 0
    IPTotal = []
    if len(IPs) == (0 or None):
        return IPTotal.append(('No IPs', 'NULL', 'NULL'))

    elif len(IPs) == 1:
        IPs[0] = ('IP', IPs[0], Source)
        return IPs
    else:
        for IPCnt in xrange(len(IPs)):
            IPsplit = IPs[IPCnt]
            IPsplit = '.'.join(map(str, IPsplit))
            IPTotal.append(('IP', IPsplit, Source))
        return IPTotal


def url_parse(indicators, Source):
    '''This function will take in a list of complete urls and remove the domain
       from them automatically'''

    URL_regex = r'((?:http(?:s)?:\/\/)?)((?:www\.)?[a-zA-Z0-9@:%._\+~#=\-]{2,256}\.(?!doc)[a-z]{2,6}\b)((?:\:\d+)?)((?:[-\w@:%\+.~#&/=]*)?)((?:\?[-\w%\+.~#&=]*)?)'
    URLs = re.findall(URL_regex, indicators, re.IGNORECASE | re.MULTILINE)

    urlCnt = 0
    domains = []
    '''Domain format: [(protocol, domain, port, extension, paramteres)]'''
    if len(URLs) == 0:
        return domains.append(('No  URLs', 'NULL', 'NULL'))

    elif len(URLs) == 1:
        URLs[0] = ('FQDN', URLs[0][1], Source)
        return URLs
    else:
        for urlCnt in xrange(len(URLs)):
            domains.append(('FQDN', URLs[urlCnt][1], Source))
        return domains


def collect_all_indicators(data, Source):
    md5s = md5_parse(data, Source)
    sha1s = sha1_parse(data, Source)
    sha256s = sha256_parse(data, Source)
    ips = ip_parse(data, Source)
    domains = url_parse(data, Source)
    return [md5s, sha1s, sha256s, ips, domains]


def csv_formatter(StoreInd):
    sourcePage = indicatorSelector = allIndicators = singleIndicator = indicatorInfo = 0
    mantisFile = csv.writer(open('mantisIndicators.csv', 'w'))
    mantisFile.writerow(['Type', 'Indicator', 'Source'])
    for sourcePage in xrange(len(StoreInd)):
        # Grabs the source number
        for indicatorSelector in xrange(len(StoreInd[sourcePage])):
            #  Grabs ALL indicators from source
            for allIndicators in xrange(len(StoreInd[sourcePage][indicatorSelector])):
                # Grabs ALL of each type of indicator
                tableIndicator = StoreInd[sourcePage][indicatorSelector][allIndicators]
                mantisFile.writerow(tableIndicator)


def dynamoo_scrape(data, source):
    '''anything -> Yellow Highlight -> blocklist -> anything -> : -> newline ->
    all indicators -> <div style="clear: both;"></div>'''
    mooRegex = r'blocklist.*(?:<br/>\n)+(?:<b>.*<\/b>.*\n)*'
    mooIndicators = re.findall(mooRegex, data, re.IGNORECASE | re.MULTILINE)
    mooMooMilk = collect_all_indicators(str(mooIndicators), source.strip('\n'))
    print(mooMooMilk)
    return mooMooMilk


def source_scrape():
    intelSources = 'Intel.txt'
    # raw_input("Please enter the text file to pull from: ")
    with open(intelSources) as Sources:
        lines = Sources.readlines()
        StoreInd = []
        for Source in lines:
            if 'fireeye' in Source:
                page = urllib2.urlopen(Source).read()
                soup = BeautifulSoup(page)
                data = str(soup.find_all('table'))
                StoreInd.append(collect_all_indicators(data, Source.strip('\n')))
                continue
            if 'dynamoo' in Source:
                page = urllib2.urlopen(Source).read()
                mooSoup = str(BeautifulSoup(page))
                mooMilk = dynamoo_scrape(mooSoup, Source)
                StoreInd.append(mooMilk)
            else:
                print(str(Source) + "Not supported")

            return StoreInd


ans = source_scrape()
csv_formatter(ans)

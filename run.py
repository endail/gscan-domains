import glob
from urllib.parse import urlparse
import re

urlmatch = re.compile("^[a-z]+://")
ipmatch = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:\:[0-9]{0,5})?$")

for filename in glob.iglob("lib/malware/*.txt"):
    for l in open(filename).readlines():

        l = l.strip()

        if l == '' or l.startswith('#') or l.isspace():
            continue

        if l.startswith("/"):
            continue

        if re.match(urlmatch, l):
            continue

        if re.match(ipmatch, l):
            continue

        p = urlparse("http://" + l)

        print(p.netloc)

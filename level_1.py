#!/usr/bin/env python3
# http://www.pythonchallenge.com/pc/def/map.html

from collections import deque
import string

cypher = (
    "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle "
    "gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle"
    ".kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
)

alphabet = deque(string.ascii_lowercase)
translation = deque(string.ascii_lowercase)
translation.rotate(-2)

caesar = str.maketrans(str(alphabet), str(translation))
print(cypher.translate(caesar))

url = "map"
print(url.translate(caesar))

# coding:utf-8
import re

# (((https?)|ftp)://)?  protocol, may be omitted
# ([-a-zA-Z0-9_:]+\.)+  domain name of letters, digits, some symbols with
#                       the followed dot
# ([-A-Za-z0-9]+)       top domain name, consists of letters, digits and some 
#                       symbols. for ip addr, this pattern also works

PT_URL = re.compile(r'(((https?)|ftp)://)?([-a-zA-Z0-9_:]+\.)+([-A-Za-z0-9]+)')
"""
The pattern for extracting url from str
"""

PT_PCOLON = re.compile(r':(?=(//))')
"""
The pattern for finding the colon after protocol name IN ONE URL
"""

PT_DOT = re.compile(r'\.')
"""
The pattern for finding the dot symbol IN ONE URL
"""

def is_not_ip(url:str)->bool:
    """
    Return True if url only consists of digits and dots and is not ip addr
    """
    temp = url.split('.')
    for i in temp:
        if not i.isdigit():
            return False
    if len(temp) < 4:
        return True
    return False


def mask_single_url(url:str)->str:
    """
    Return the masked version of URL where protocol colon is replaced with 冒号
    and dot with 点.
    """
    if is_not_ip(url):
        return url
    ret = PT_PCOLON.sub('冒号', url)
    ret = PT_DOT.sub('点', ret)
    return ret


def mask_url(text:str)->str:
    """
    Finding the url in the TEXT and return the text where the urls are masked to
    bypass some occasions where direct urls are not allowed.
    """
    ret = PT_URL.sub(lambda mt:mask_single_url(mt.group()), text)
    return ret


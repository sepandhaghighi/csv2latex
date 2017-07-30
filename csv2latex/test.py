'''
>>> from csv2latex import *
>>> line(6)
'------'
>>> line(6,"^")
'^^^^^^'
>>> escape_char([['asdasdasd','adsasdasdasd'],['asdasdasdasd','aasdasdsds']])
[['asdasdasd', 'adsasdasdasd'], ['asdasdasdasd', 'aasdasdsds']]
>>> white_space([['asdasdasd','adsasdasdasd'],['asdasdasdasd','aasdasdsds']])
[12, 12]

'''
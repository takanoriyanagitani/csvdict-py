def dict2kvpairs(d=dict()): return map(lambda k: (k, d[k]), sorted(d.keys()))

def dict2str(d=dict(), s1=":", s2=";", pairs=None): return s2.join(
  map(
    lambda t: s1.join(map(str, t)),
    pairs or dict2kvpairs(d)
  )
)

def dict2csv(d=dict(), c=",", pairs=None): return c.join(map(
  lambda pair: c.join(map(str, pair)),
  pairs or dict2kvpairs(d)
))

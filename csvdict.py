def dict2kvpairs(d=dict(), d2k=lambda x: sorted(x.keys())): return map(lambda k: (k, d[k]), d2k(d))

def dict2str(d=dict(), s1=":", s2=";", pairs=None, d2k=lambda x: sorted(x.keys())): return s2.join(
  map(
    lambda t: s1.join(map(str, t)),
    pairs or dict2kvpairs(d, d2k)
  )
)

def dict2csv(d=dict(), c=",", pairs=None): return c.join(map(
  lambda pair: c.join(map(str, pair)),
  pairs or dict2kvpairs(d)
))

def ds2str(ds=None, s1=":", s2=";", d2k=lambda x: sorted(x.keys())): return dict2str(ds,s1,s2) if dict == type(ds) else ds

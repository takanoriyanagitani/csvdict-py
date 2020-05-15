def dict2keys(d=dict()): return sorted(d.keys())

def dict2kvpairs(d=dict(), d2k=dict2keys): return map(lambda k: (k, d[k]), d2k(d))

def dict2str(d=dict(), s1=":", s2=";", d2k=dict2keys): return s2.join(
  map(
    lambda t: s1.join(map(str, t)),
    dict2kvpairs(d, d2k)
  )
)

def dict2csv(d=dict(), c=",", d2k=dict2keys): return c.join(map(
  lambda pair: c.join(map(str, pair)),
  dict2kvpairs(d, d2k)
))

def ds2str(ds=None, s1=":", s2=";", d2k=dict2keys): return dict2str(ds,s1,s2, d2k) if dict == type(ds) else ds

def dict2str2(d=dict(), s1="=|", s2=":;", d2k=dict2keys):
  keys = d2k(d)
  pairs = map(lambda k: (k, ds2str(d[k], s2[0], s2[1], d2k)), keys)
  strs  = map(lambda p: s1[0].join(map(str, p)), pairs)
  return s1[1].join(strs)

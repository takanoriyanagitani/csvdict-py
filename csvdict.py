def dict2str(d=dict(), s1=":", s2=";"): return s2.join(
  map(
    lambda t: s1.join(map(str, t)),
    d.items()
  )
)

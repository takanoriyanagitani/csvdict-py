import unittest

import csvdict

class dict2str(unittest.TestCase):
  def test_empty(self): self.assertEqual("", csvdict.dict2str(dict()))
  def test_tower(self): self.assertEqual("tst:634;tt:333", csvdict.dict2str(dict(tst=634, tt=333)))
  def test_mount(self): self.assertEqual("fuji=3776|takao=599", csvdict.dict2str(dict(fuji=3776,takao=599),"=","|"))
  pass

def main(): return unittest.main()

def try_exec(): return "__main__" == __name__ and main()

try_exec()

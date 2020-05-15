import unittest

import csvdict

class dict2str(unittest.TestCase):
  def test_empty(self): self.assertEqual("", csvdict.dict2str(dict()))
  def test_tower(self): self.assertEqual("tst:634;tt:333", csvdict.dict2str(dict(tst=634, tt=333)))
  def test_mount(self): self.assertEqual("fuji=3776|takao=599", csvdict.dict2str(dict(fuji=3776,takao=599),"=","|"))
  pass

class dict2csv(unittest.TestCase):
  def test_empty(self): self.assertEqual("", csvdict.dict2csv(dict()))
  def test_tower(self): self.assertEqual("tst,634,tt,333", csvdict.dict2csv(dict(tst=634, tt=333)))
  def test_mount(self): self.assertEqual("fuji-3776-takao-599", csvdict.dict2csv(dict(fuji=3776,takao=599),"-"))
  pass

class ds2str(unittest.TestCase):
  def test_empty(self): self.assertEqual("", csvdict.ds2str(""))
  def test_tower(self): self.assertEqual("tst:634;tt:333", csvdict.ds2str(dict(tst=634, tt=333)))
  def test_mount(self): self.assertEqual("fuji=3776|takao=599", csvdict.ds2str(dict(fuji=3776,takao=599),"=","|"))

def main(): return unittest.main()

def try_exec(): return "__main__" == __name__ and main()

try_exec()

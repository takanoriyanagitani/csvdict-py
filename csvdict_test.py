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

class dict2str2(unittest.TestCase):
  def test_empty(self): self.assertEqual("", csvdict.dict2str2(dict()))
  def test_phone(self): self.assertEqual(
    "cam1=name:front;res:2k|cam2=name:back;res:4k|cameras=2|type=phone",
    csvdict.dict2str2(dict(
      type="phone",
      cameras=2,
      cam1=dict(name="front", res="2k"),
      cam2=dict(name="back",  res="4k"),
    ))
  )
  def test_drive(self): self.assertEqual(
    "count=3|d1=read:4GB/s;rotate:False;size:2TB;write:2GB/s|d2=read:2GB/s;rotate:False;size:1TB;write:1GB/s|raid=False",
    csvdict.dict2str2(dict(
      raid=False,
      count=3,
      d1=dict(size="2TB", rotate=False, write="2GB/s", read="4GB/s"),
      d2=dict(size="1TB", rotate=False, write="1GB/s", read="2GB/s"),
    ))
  )

def main(): return unittest.main()

def try_exec(): return "__main__" == __name__ and main()

try_exec()

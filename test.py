# -*- coding: utf-8 -*-
from pytanggalmerah import TanggalMerah
import unittest

class TanggalMerahTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.t = TanggalMerah()
	
	# end setUpClass()
	
	def test_check(self):
		self.assertFalse(self.t.check())
	
	def test_check2(self):
		self.t.set_date("2019", "02", "05")
		self.assertTrue(self.t.check())
	
if __name__=="__main__":
	unittest.main()
	
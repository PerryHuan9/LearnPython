#ecoding=gbk

def getFormattedName(first,last,middle=''):
	if (middle):
		fullName=first+' '+middle+' '+last
	else:
		fullName=first+' '+last
	return fullName.title()


print(getFormattedName('perry','huang','lu'))


import unittest

class NameTestCase(unittest.TestCase):
	"""测试getFormattedName()这个方法"""
	def testFirstMiddleLatName(self):
		fullName=getFormattedName('perry','huang','lu')
		self.assertEqual(fullName,'Perry Lu Huang')
		
	def testFirstLastName(self):
		fullName=getFormattedName('益凛','huang')
		self.assertEqual(fullName,'益凛 Huang')



unittest.main()










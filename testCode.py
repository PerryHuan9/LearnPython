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
	"""����getFormattedName()�������"""
	def testFirstMiddleLatName(self):
		fullName=getFormattedName('perry','huang','lu')
		self.assertEqual(fullName,'Perry Lu Huang')
		
	def testFirstLastName(self):
		fullName=getFormattedName('����','huang')
		self.assertEqual(fullName,'���� Huang')



unittest.main()










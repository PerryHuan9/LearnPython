#ecoding=gbk

class AnonymousSurvey():
	"""收集匿名调查问卷的答案"""
	def __init__(self,question):
		self.question=question
		self.answers=[]
	
	def showQuestion(self):
		print(self.question)
		
	def storeAnswer(self,answer):
		self.answers.append(answer)
		
	def showResults(self):
		print("Survey results:")
		for answer in self.answers:
			print('- '+answer)
	
	
	
def testAnonymousSurvey():		
	question="What language did you first learn to speak?"
	survey=AnonymousSurvey(question)
	print('Please enter "q" to quit at any time.')
	survey.showQuestion()
	while True:
		answer=input('Language:')
		if answer=='q':
			break
		survey.storeAnswer(answer)
		
	print("Thank you to everyone who participated in the survey!")
	survey.showResults()
	
# testAnonymousSurvey()

import unittest
class TestSurveyCase(unittest.TestCase):
	
	def setUp(self):
		"""测试时将会最先运行这个函数，再运行其它test-函数"""
		question="What's your favorite language?"
		self.survey=AnonymousSurvey(question)
		self.languages=['Chinese','English','Japanese']
	
	def testStoreAnswer(self):
		self.survey.storeAnswer("Chinese")
		self.assertIn('Chinese',self.survey.answers)
		
	def testThreeAnsers(self):
		for language in self.languages:
			self.survey.storeAnswer(language)
		for language in self.languages:
			self.assertIn(language,self.survey.answers)
			
		
		
unittest.main()
	
	
			











































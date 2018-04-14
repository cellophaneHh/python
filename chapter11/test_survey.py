import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善的存储"""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        self.my_survey.store_response(self.responses[0])
        self.assertIn("English", self.my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案会被妥善的存储"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_case1(self):
        stmt = "I am glad this happened"
        resp = emotion_detector(stmt)
        print(resp)
        self.assertEqual(resp['dominant_emotion'],'joy')


    def test_case2(self):
        stmt = "I am really mad about this"
        resp = emotion_detector(stmt)
        print(resp)
        self.assertEqual(resp['dominant_emotion'],'anger')

    def test_case3(self):
        stmt = "I feel disgusted just hearing about this"
        resp = emotion_detector(stmt)
        print(resp)
        self.assertEqual(resp['dominant_emotion'],'disgust')

    def test_case4(self):
        stmt = "I am so sad about this"
        resp = emotion_detector(stmt)
        print(resp)
        self.assertEqual(resp['dominant_emotion'],'sadness')

    def test_case5(self):
        stmt = "I am really afraid that this will happen"
        resp = emotion_detector(stmt)
        print(resp)
        self.assertEqual(resp['dominant_emotion'],'fear')



if __name__ == "__main__":
    unittest.main()


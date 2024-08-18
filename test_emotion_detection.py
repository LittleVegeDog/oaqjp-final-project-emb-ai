from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy emotion
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 
                                          "joy")
        
        # Test case for anger emotion
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], 
                                            "anger")
        
        # Test case for disgust emotion
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 
                                            "disgust")
        
        # Test case for sadness emotion
        self.assertEqual(emotion_detector("I am so sad about this	")['dominant_emotion'], 
                                            "sadness")

        # Test case for fear emotion
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], 
                                            "fear")

# Run all the test cases defined in the module when the script is executed.
unittest.main()
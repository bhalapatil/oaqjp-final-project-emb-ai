
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze:
        emotion_dict = emotion_detector(text_to_analyze)
        if not emotion_detection['dominant_emotion']:
            return "Invalid text! Please try again!."
        else:    
            stmt = f"For the given statement, the system response is 'anger': {emotion_dict['anger']} , 'disgust' : {emotion_dict['disgust']} , 'fear' : {emotion_dict['fear']}, 'joy' : {emotion_dict['joy']} and 'sadness' : {emotion_dict['sadness']}. The dominant emtion is {emotion_dict['dominant_emotion']}"
            return stmt



# test
#added another line 


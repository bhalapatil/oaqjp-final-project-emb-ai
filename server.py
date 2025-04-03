from flask import Flask , request , render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_dict = emotion_detector(text_to_analyze)
    stmt = f"For the given statement, the system response is 'anger': {emotion_dict['anger']} , 'disgust' : {emotion_dict['disgust']} , 'fear' : {emotion_dict['fear']}, 'joy' : {emotion_dict['joy']} and 'sadness' : {emotion_dict['sadness']}. The dominant emtion is {emotion_dict['dominant_emotion']}"
    return stmt



''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its emotion  
        socres and the dominant emotion for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    emot_resp = emotion_detector(text_to_analyze)

    # If the dominant emotion in the response is None,
    # the input text is invalid
    if emot_resp['dominant_emotion'] is None:
        return "Invalid input ! Try again"

    # Extract the emotion scores and the dominant emotion from the response
    anger = emot_resp['anger']
    fear = emot_resp['fear']
    joy = emot_resp['joy']
    sadness = emot_resp['sadness']
    disgust = emot_resp['disgust']
    dom_emot = emot_resp['dominant_emotion']
    # Return a formatted string
    return (f"For the given statement, the system response is 'anger': {anger}, "
            + f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and "
            + f"'sadness': {sadness}. The dominant emotion is {dom_emot}")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
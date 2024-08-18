# Import the requests library to handle HTTP requests
import requests, json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers = headers)

    # Invalid input error handling
    # If the response status code is 400, set all values in dict to None
    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 
                'fear': None, 'joy': None, 'sadness': None, 
                'dominant_emotion': None}
    elif response.status_code == 200:
        # Parsing the JSON response from the API
        resp_dict = json.loads(response.text)
        # Get dict that contains the scores of emotions
        emo_score_dict = resp_dict['emotionPredictions'][0]['emotion']
        # Find the dominant emotion and add key value pair into dict
        dom_emo_score = 0
        for emo in emo_score_dict.keys():
            if emo_score_dict[emo] > dom_emo_score:
                dominant_emotion = emo
                dom_emo_score = emo_score_dict[emo]
        emo_score_dict['dominant_emotion'] = dominant_emotion

        return emo_score_dict

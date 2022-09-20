import json
import requests


class GoogleTTS():
    def __init__(self) -> None:
        self.__token = "AIzaSyDpndmVRZWCdaXaCmrOEtlDMRKB_sd70S8" #API Token
    
    def __build_header(self):
        '''
        Buid the header to be sent with the request to Google API endpoint
        '''

        return {
            'X-Goog-Api-Key': self.__token,
            'Content-Type': 'application/json; charset=utf-8',
        } 

    def __build_data(self,text) ->str:
        '''
        Build the data to be sent in the body of the request to Google API endpoint
        '''

        return json.dumps({
            "input":{
                "text":text
            },
             "voice":{
                "languageCode":"en-US",
                "ssmlGender":"FEMALE"
            },
            "audioConfig":{
                "audioEncoding":"MP3"
            }
        })

    def convert_text_to_speech(self,text):
        '''
        Function to send request to Google API endpoint. Returns the base64 encoded string of the audio.s
        '''
        req = requests.post(
            'https://texttospeech.googleapis.com/v1/text:synthesize',
            headers=self.__build_header(),
            data=self.__build_data(text),
        )
        return json.loads(req.text)

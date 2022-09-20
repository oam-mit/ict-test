import json
import requests


class GoogleTTS():
    def __init__(self) -> None:
        self.__token = "AIzaSyDpndmVRZWCdaXaCmrOEtlDMRKB_sd70S8"
    
    def __build_header(self):
        return {
            'X-Goog-Api-Key': self.__token,
            'Content-Type': 'application/json; charset=utf-8',
        }

    def __build_data(self,text) ->str:
        return json.dumps({
            "input":{
                "text":text
            },
             "voice":{
                "languageCode":"en-gb",
                "name":"en-GB-Standard-A",
                "ssmlGender":"FEMALE"
            },
            "audioConfig":{
                "audioEncoding":"MP3"
            }
        })

    def convert_text_to_speech(self,text):
        req = requests.post(
            'https://texttospeech.googleapis.com/v1/text:synthesize',
            headers=self.__build_header(),
            data=self.__build_data(text),
        )
        return json.loads(req.text)

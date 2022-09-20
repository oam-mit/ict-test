import base64
import io

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


from .utils import GoogleTTS #Class which contains the code to send request to Google API

def index(request):
    '''
    Render home page
    '''
    return render(request,'decoder/index.html')


@api_view(['POST'])
def convert_text_to_speech(request):
    '''
    API endpoint which receives the input text, and returns the base64 encoded audio file in the response.
    Sample response: {
        'byte_data':{
            'audioContent':'//NExAASYDXkABjGBXgQASu7pQ4s8AQAAiOP/rRmBh5gf8Az//r+ugAH5/f4GAAI+GP+A4AMH4AZ4BA6IjnwHbgO/8x//H4AXD/jj////Mf0/AA6H8D......'
        }
    }
    '''

    tts = GoogleTTS()

    return Response({
        'byte_data':tts.convert_text_to_speech(request.data.get('input'))
    })


def download(request):
    '''
    Endpoint which receives a POST request with input_text as the data to be converted to audio file in the body. It decodes the received base64 encoded string from Google API and send back a mp3 file to the user
    '''

    if request.method =='POST':
        tts = GoogleTTS()
        data = tts.convert_text_to_speech(request.POST.get('input_text'))

        buffer = io.BytesIO()
        content = base64.b64decode(data['audioContent'])
        buffer.write(content)

        response = HttpResponse(
            buffer.getvalue(),
            content_type="audio/mpeg",
        )
        response['Content-Disposition'] = 'attachment;filename=output.mp3'
        return response


       
    
    else:
        return HttpResponse(request,"Sorry. Method not allowed")

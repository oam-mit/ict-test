import base64
import io

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from wsgiref.util import FileWrapper

from .utils import GoogleTTS
# Create your views here.

def index(request):
    return render(request,'decoder/index.html')


@api_view(['POST'])
def convert_text_to_speech(request):
    tts = GoogleTTS()

    return Response({
        'byte_data':tts.convert_text_to_speech(request.data.get('input'))
    })


def download(request):
    if request.method =='POST':
        tts = GoogleTTS()
        data = tts.convert_text_to_speech(request.POST.get('input_text'))

        # buffer = io.StringIO()
        # buffer.write(data['audioContent'])

        # response = HttpResponse(FileWrapper(buffer.getvalue()), content_type='application/zip')
        # response['Content-Disposition'] = 'attachment; filename=MY_FILE_NAME.zip'
        # return response

        buffer = io.BytesIO()
        content = base64.b64decode(data['audioContent'])
        buffer.write(content)

        response = HttpResponse(
            buffer.getvalue(),
            content_type="audio/mpeg",
        )
        response['Content-Disposition'] = 'attachment;filename=output.mp3'
        return response


        # with io.BytesIO(base64.b64decode(data['audioContent'])) as fh:
        #     response = HttpResponse(fh.read(), content_type="audio/mpeg")
        #     response['Content-Disposition'] = f'inline; filename=output.mp3'
        #     return response
    
    else:
        return HttpResponse(request,"Sorry. Method not allowed")

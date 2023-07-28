from django.http import JsonResponse
from googletrans import Translator
from django.shortcuts import render

# Create an instance of the Translator class from googletrans
trans = Translator()


def home(request):

    if request.method == "POST":
        data = request.POST.get('data')
        # Corrected to use 'language' instead of 'select'

        language = request.POST.get('language')
        # print(trans.detect(data))

        # Perform the translation using Google Translate
        transl = trans.translate(data, dest=language)
        translated_text = transl.text
        print(translated_text)
        print(data)

        return JsonResponse({'translated_text': translated_text})

# If you have a separate view for rendering the template, keep it as it is


def get_template(request):
    return render(request, "index.html")

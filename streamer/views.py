from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def stream(request, stream_id):
    context = {
        'stream_id': stream_id,
    }
    return render(request, 'stream.html', context)

def watch(request, stream_id):
    context = {
        'stream_id': stream_id,
    }
    return render(request, 'watch.html', context)

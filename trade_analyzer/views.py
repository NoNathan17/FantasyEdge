from django.shortcuts import render

# Create your views here.

def trade_analyzer_view(request):
    return render(request, 'trade_analyzer.html')

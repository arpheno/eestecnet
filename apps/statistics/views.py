# Create your views
def simpleStatistics(request):
    fig = figure()
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
    return HttpResponse('<h1>Page was found</h1>')

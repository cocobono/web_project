from django.shortcuts import render
from django.http import HttpResponse
from .google_trends import GoogleTrends
import plotly.graph_objs as go
import plotly.offline as opy
from rest_framework.decorators import api_view


#TODO: make this nicer!
@api_view(['GET'])
def trend(request):
    key = {}

    if not request.GET.get('keyword', False):
        return render(request, 'api/googletrends.html')
    else:
        keyword = request.GET['keyword']

        api = GoogleTrends()
        df = api.get_response(keyword)

        trace1 = go.Scatter(x=df['date'],
                            y=df[keyword],
                            marker={'color': 'blue', 'symbol': 104, 'size': 10},
                            mode="lines",
                            name='1st Trace')

        data = [trace1]
        layout = go.Layout(title=f"Interest Over Time for \'{keyword}\'",
                           xaxis={'title': 'Date'},
                           yaxis={'title': 'Relative Popularity'})
        figure = go.Figure(data=data,
                           layout=layout)
        div = opy.plot(figure,
                       auto_open=False,
                       output_type='div')

        return render(request, 'api/googletrends.html', {'graph': div})

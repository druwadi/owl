from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

import plotly.express as px
import pandas as pd

from influxdb import InfluxDBClient

client = InfluxDBClient(host='influxdb', port=8086)
client.switch_database('collector_metrics')

   
def index(request):
      value = request.POST.get("call")
      if value == 'cpu':
         rs = client.query('select value from cpu_percent;')
         resultfinal = list(rs.get_points(measurement='cpu_percent'))
         plot_div = plot(px.line(resultfinal, x="time", y="value", title="CPU per second"), output_type='div')
      
      if value == 'mem':
         rs = client.query('select value from mem_percent;')
         resultfinal = list(rs.get_points(measurement='mem_percent'))
         plot_div = plot(px.line(resultfinal, x="time", y="value", title="Memory per second"), output_type='div')
      
      else:
         rs = client.query('select value from cpu_percent;')
         resultfinal = list(rs.get_points(measurement='cpu_percent'))
         plot_div = plot(px.line(resultfinal, x="time", y="value", title="CPU per second"), output_type='div')

      return render(request, "webservice/index.html", context={'plot_div': plot_div})
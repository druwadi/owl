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
      # CPU Percent
      rs = client.query('select value from cpu_percent;')
      resultfinalcpu = list(rs.get_points(measurement='cpu_percent'))
      plot_div = plot(px.line(resultfinalcpu, x="time", y="value", title="CPU Use Percentage"), output_type='div')
      
      # Memory Percent
      rs = client.query('select value from mem_percent;')
      resultfinalmem = list(rs.get_points(measurement='mem_percent'))
      plot_div2 = plot(px.line(resultfinalmem, x="time", y="value", title="Memory Use Percentage"), output_type='div')

      # Swap Memory Percent
      rs = client.query('select value from swap_mem_percent;')
      resultfinalswapmem = list(rs.get_points(measurement='swap_mem_percent'))
      plot_div3 = plot(px.line(resultfinalswapmem, x="time", y="value", title="Swap Memory Use Percentage"), output_type='div')

      # Disk Percent
      rs = client.query('select value from disk_percent;')
      resultfinaldisk_p = list(rs.get_points(measurement='disk_percent'))
      plot_div4 = plot(px.line(resultfinaldisk_p, x="time", y="value", title="Disk Space Use Percentage"), output_type='div')

      return render(request, "webservice/index.html", context={'plot_div': plot_div, 'plot_div2': plot_div2, 'plot_div3': plot_div3, 'plot_div4': plot_div4})
import numpy as np
from django.shortcuts import render
import pandas as pd

from csvs.models import Csv
from .utils import generate_all_plates_count_by_emirate_graph, \
    generate_all_plates_count_by_time, generate_all_plates_error_count_by_emirate_color, \
    generate_all_plates_count_by_attributes_type, generate_all_plates_error_count_by_emirate, \
    generate_all_plates_count_by_emirate_color, generate_all_plates_error_count_by_attribute_type, \
    generate_all_plates_error_count_by_time, generate_all_attributes_error_count_by_time
from .models import Plate


# Create your views here.

def plate_graphs_view(request):
    graph = None
    error_message = None
    selected_csv_file = None
    csv_files = None
    provided_samples = None

    try:
        plates_df = pd.DataFrame(Plate.objects.all().values())
    except:
        error_message = "No data records found in database!"

    # try:
    provided_samples = plates_df['id'].count()
    csv_files = pd.DataFrame(Csv.objects.all().values()).get("file_name").astype(str).values.tolist()
    selected_csv_file = csv_files[0]
    if request.method == 'POST':
        graph = None
        if request.POST.get("csv_file"):
            selected_csv_file = request.POST.get("csv_file")

        emirate = request.POST.get('emirate')
        attribute = request.POST.get('attribute')
        result_type = request.POST.get('result_type')
        data_info = request.POST.get('data_info')

        chart_title = emirate + " " + attribute + " " + result_type + " by " + data_info
        print(chart_title)
        if chart_title == "all plates count by emirate":
            graph = generate_all_plates_count_by_emirate_graph(plates_df)
        elif chart_title == "all plates count by time (hours)":
            graph = generate_all_plates_count_by_time(plates_df)
        elif chart_title == "all plates count by emirate-color":
            graph = generate_all_plates_count_by_emirate_color(plates_df)
        elif chart_title == "all plates count by attribute-type":
            graph = generate_all_plates_count_by_attributes_type(plates_df)
        elif chart_title == "all plates error count by emirate":
            graph = generate_all_plates_error_count_by_emirate(plates_df)
        elif chart_title == "all plates error count by emirate-color":
            graph = generate_all_plates_error_count_by_emirate_color(plates_df)
        elif chart_title == "all plates error count by attribute-type":
            graph = generate_all_plates_error_count_by_attribute_type(plates_df)
        elif chart_title == "all plates error count by time (hours)":
            graph = generate_all_plates_error_count_by_time(plates_df)
        elif chart_title == "all attributes error count by time (hours)":
            graph = generate_all_attributes_error_count_by_time(plates_df)
    # except:
    #     error_message = "Ups. Something went wrong!"

    context = {
        'graph': graph,
        'error_message': error_message,
        'csv_files': csv_files,
        'selected_csv_file': selected_csv_file,
        'provided_samples': provided_samples,
    }
    return render(request, 'products/main.html', context)

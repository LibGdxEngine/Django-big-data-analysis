import numpy as np
from django.shortcuts import render
import pandas as pd

from csvs.models import Csv
from .utils import get_simple_plots
from .forms import PurchaseForm
from .models import Plate


# Create your views here.

def plate_graphs_view(request):
    graph = None
    error_message = None
    selected_csv_file = None
    csv_files = None
    provided_samples = None
    plates_df = pd.DataFrame(Plate.objects.all().values())

    all_emirates = plates_df[["predicted_emirate", "gt_emirate"]].values.ravel()
    all_emirates = pd.unique(all_emirates)
    emirates_plates_count = plates_df['gt_emirate'].value_counts().values

    emirates_colors = plates_df[['gt_emirate', 'gt_color']].agg('-'.join, axis=1)
    emirates_colors_count = emirates_colors.value_counts().values
    emirates_colors = pd.unique(emirates_colors)

    try:

        provided_samples = plates_df['id'].count()
        csv_files = pd.DataFrame(Csv.objects.all().values()).get("file_name").astype(str).values.tolist()
        selected_csv_file = csv_files[0]

        if request.method == 'POST':
            if request.POST.get("csv_file"):
                selected_csv_file = request.POST.get("csv_file")

            emirate = request.POST.get('emirate')
            attribute = request.POST.get('attribute')
            result_type = request.POST.get('result_type')
            data_info = request.POST.get('data_info')


            if data_info == "emirate":
                # print(emirates_plates_count, all_emirates)
                graph = get_simple_plots('bar plot', x=all_emirates, y=emirates_plates_count,
                                         emirate=emirate, attribute=attribute,
                                         result_type=result_type, data_info=data_info)
            else:
                # print(emirates_plates_count, all_emirates)
                graph = get_simple_plots('bar plot', x=emirates_colors, y=emirates_colors_count,
                                         emirate=emirate, attribute=attribute,
                                         result_type=result_type, data_info=data_info)
            # df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            # df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
    except:
        error_message = "Ups. Something went wrong!"

    context = {
        'graph': graph,
        'error_message': error_message,
        'csv_files': csv_files,
        'selected_csv_file': selected_csv_file,
        'provided_samples': provided_samples,
    }
    return render(request, 'products/main.html', context)

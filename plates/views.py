from django.shortcuts import render
import pandas as pd
from .utils import get_simple_plots
from .forms import PurchaseForm


# Create your views here.

def plate_graphs_view(request):
    graph = None
    error_message = None
    df = None
    price = None
    try:
        # products_df = pd.DataFrame(Product.objects.all().values())
        # purchases_df = pd.DataFrame(Purchase.objects.all().values())
        # products_df['product_id'] = products_df['id']

        # if purchases_df.shape[0] > 0:
        #     df = pd.merge(purchases_df, products_df, on='product_id') \
        #         .drop(['id_y', 'date_y'], axis=1) \
        #         .rename({'id_x': 'id', 'date_x': 'date'}, axis=1)
        #     price = df['price']
            if request.method == 'POST':
                emirate = request.POST.get('emirate')
                attribute = request.POST.get('attribute')
                result_type = request.POST.get('result_type')
                data_info = request.POST.get('data_info')
                # df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
                # df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                # if chart_type != "":
                #     if date_from != "" and date_to != "":
                #         df = df[(df['date'] > date_from) & (df['date'] < date_to)]
                #
                # #     graph = get_simple_plots(chart_type, x=df2['date'], y=df2['total_price'], data=df)
                # else:
                #     error_message = "Please select a chart type!"
                print(emirate, attribute, result_type + " by " + data_info)
        # else:
        #     error_message = "No records in database"
    except:
        products_df = None
        purchases_df = None
        error_message = "No records in database"

    context = {
        'graph': graph,
        'price': price,
        'error_message': error_message,
    }
    return render(request, 'products/main.html', context)


def add_purchase_view(request):
    added_message = None
    form = PurchaseForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.salesman = request.user
        obj.save()

        form = PurchaseForm()
        added_message = "The message has been added"
    context = {
        'form': form,
        'added_message': added_message,
    }

    return render(request, 'products/add.html', context)

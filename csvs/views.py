import time

from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from plates.models import Plate
from django.contrib.auth.decorators import login_required


# Create your views here.


def upload_csv_view(request):
    error_message = None
    success_message = None
    is_loading = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                is_loading = True
                for index, row in enumerate(reader):
                    if index != 0:
                        plate, _ = Plate.objects.get_or_create(
                            csv_file=obj.file_name,
                            image_path=row[0],
                            predicted_code=row[1],
                            predicted_number=row[2],
                            predicted_emirate=row[3],
                            predicted_color=row[4],
                            gt_code=row[5],
                            gt_number=row[6],
                            gt_emirate=row[7],
                            gt_color=row[8],
                        )
                        print(index, "done")

            obj.activated = True
            obj.save()
            success_message = "Uploaded sucessfully"
        except:
            error_message = "Ups. Something went wrong...."
        finally:
            is_loading = False
    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
        'is_loading': is_loading,
    }
    return render(request, 'csvs/upload.html', context)

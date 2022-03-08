import time

from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from plates.models import Plate
from django.contrib.auth.decorators import login_required


def upload_csv_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for index, row in enumerate(reader):
                    if index != 0:
                        if str(row[1]):
                            image_hour = row[1].split(" ")[1].split(":")[0]
                        plate, _ = Plate.objects.get_or_create(
                            csv_file=obj.file_name,
                            image_path=row[0],
                            image_time=image_hour,
                            gt_color=row[2],
                            gt_emirate=row[3],
                            gt_code=row[4],
                            gt_number=row[5],
                            description=row[6],
                            predicted_code=row[7],
                            predicted_color=row[8],
                            predicted_number=row[9],
                            predicted_emirate=row[10],
                            status=row[11],
                        )
                        print(index, "done")

            obj.activated = True
            obj.save()
            success_message = "Uploaded successfully"
        except:
            error_message = "Ups. Something went wrong...."

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'csvs/upload.html', context)

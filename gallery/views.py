from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from datetime import date, timedelta
from .models import Image

def gallery_view(request):
    today = date.today()
    last_month_start = date(today.year, today.month - 1, 1)
    last_month_end = date(today.year, today.month, 1) - timedelta(days=1)

    images = Image.objects.filter(created_date__range=(last_month_start, last_month_end))

    return render(request, 'gallery.html', {'images': images})

def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)

    return render(request, 'image_detail.html', {'image': image})
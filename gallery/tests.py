from datetime import date, timedelta
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from .models import Category, Image
from .views import image_detail
class GalleryViewTestCase(TestCase):
    def test_gallery_view(self):
        category1 = Category.objects.create(name='Category 1')
        category2 = Category.objects.create(name='Category 2')

        today = date.today()
        last_month_start = date(today.year, today.month - 1, 1)
        last_month_end = date(today.year, today.month, 1) - timedelta(days=1)

        image1 = Image.objects.create(
            title='Image 1',
            image='path/to/image1.jpg',
            created_date=last_month_start,
            age_limit=18
        )
        image1.categories.add(category1)

        image2 = Image.objects.create(
            title='Image 2',
            image='path/to/image2.jpg',
            created_date=last_month_end,
            age_limit=21
        )
        image2.categories.add(category1, category2)

        image3 = Image.objects.create(
            title='Image 3',
            image='path/to/image3.jpg',
            created_date=today,
            age_limit=16
        )

        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'gallery.html')

        images_in_context = response.context['images']
        self.assertIn(image1, images_in_context)
        self.assertIn(image2, images_in_context)
        self.assertNotIn(image3, images_in_context)



# management/commands/fetch_products.py

import requests
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from air.store.models import Brand, Product, Image  # Adjust import as per your project structure

class Command(BaseCommand):
    help = 'Fetch products from API and store in the database'

    def handle(self, *args, **kwargs):
        brand_urls = [
            "https://www.bulclima.com/tools/api/items/2",
            "https://www.bulclima.com/tools/api/items/3",
            "https://www.bulclima.com/tools/api/items/359",
            "https://www.bulclima.com/tools/api/items/92",
            "https://www.bulclima.com/tools/api/items/94",
            "https://www.bulclima.com/tools/api/items/101",
            "https://www.bulclima.com/tools/api/items/137",
            "https://www.bulclima.com/tools/api/items/145",
            "https://www.bulclima.com/tools/api/items/342",
            "https://www.bulclima.com/tools/api/items/360",
            "https://www.bulclima.com/tools/api/items/362",
            "https://www.bulclima.com/tools/api/items/363",
        ]

        for url in brand_urls:
            response = requests.get(url)
            if response.status_code == 200:
                self.parse_and_save(response.text)
            else:
                self.stdout.write(self.style.ERROR(f'Failed to fetch data from {url}'))

    def parse_and_save(self, xml_data):
        root = ET.fromstring(xml_data)
        for product in root.findall('product'):
            try:
                product_code = product.find('product_code').text
                title = product.find('title').text
                category = product.find('category').text
                sub_category = product.find('sub_category').text
                manufacturer = product.find('manufacturer').text
                price = product.find('price').text
                sku = product.find('sku').text
                brand_name = manufacturer

                if not all([product_code, title, category, sub_category, manufacturer, price, sku]):
                    self.stdout.write(self.style.WARNING(f'Skipping product with missing fields: {title}'))
                    continue

                brand, _ = Brand.objects.get_or_create(name=brand_name)
                product_instance, created = Product.objects.update_or_create(
                    product_code=product_code,
                    defaults={
                        'title': title,
                        'short_description': product.find('short_description').text if product.find('short_description') is not None else '',
                        'description': product.find('description').text if product.find('description') is not None else '',
                        'category': category,
                        'sub_category': sub_category,
                        'manufacturer': manufacturer,
                        'price': price,
                        'sku': sku,
                        'brand': brand,
                    }
                )

                # Handle multiple images
                images = product.findall('images/image')
                for img in images:
                    image_url = img.text
                    Image.objects.get_or_create(product=product_instance, url=image_url)

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error saving product: {e}'))

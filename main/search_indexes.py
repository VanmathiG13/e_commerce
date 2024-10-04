# search_indexes.py

from haystack import indexes
from .models import Product

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)  # Allows searching on text
    product_id = indexes.IntegerField(model_attr='product_id')
    product_name = indexes.CharField(model_attr='product_name')
    image_url = indexes.CharField(model_attr='image_url')
    mrp = indexes.DecimalField(model_attr='mrp')
    discounted_price = indexes.DecimalField(model_attr='discounted_price')
    
    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def get_updated_field(self):
        return 'updated_at'  # Change if you have a timestamp field for updates

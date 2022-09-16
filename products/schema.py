import graphene
from graphene_django import DjangoObjectType
from products.models import Product
  
class Producttype(DjangoObjectType):
    class Meta: 
        model = Product
        fields = (
            'id',
            'category',
            'title',
            'price',
            'image',
            'discount', 
            'description',
            'status',
            'date_created',
            'unique_id'
        )  


class Query(graphene.ObjectType):
    products = graphene.List(Producttype)

    def resolve_products(root, info, **kwargs):
        # Querying a list
        return Product.objects.all()
        
schema = graphene.Schema(query=Query)
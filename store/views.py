from rest_framework.permissions import AllowAny
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductSerializer, CategorySerializer, ProfileSerializer
from .models import Category, Product, Profile


class ProfileApi(ListAPIView):
    serializer_class = ProfileSerializer
    parser_classes = [FileUploadParser, JSONParser]
    queryset = Profile.objects.all()
    permission_classes = [AllowAny]

class ProductsApi(ListAPIView):
    serializer_class = ProductSerializer
    parser_classes = [FileUploadParser, JSONParser]
    queryset = Product.objects.all().order_by('category')
    permission_classes = [AllowAny]


class CategoryApi(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class DetailedCategoryApi(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "pk"
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]


class DetailedProductApi(RetrieveAPIView):
    serializer_class = ProductSerializer
    parser_classes = [FileUploadParser, JSONParser]
    queryset = Product.objects.all()
    lookup_field = 'pk'
    permission_classes = [AllowAny]

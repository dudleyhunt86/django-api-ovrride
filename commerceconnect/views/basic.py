from django.contrib import auth
from oscar.core.loading import get_model
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from commerceconnect import serializers, permissions


__all__ = (
    'BasketList', 'BasketDetail',
    'LineAttributeList', 'LineAttributeDetail',
    'ProductList', 'ProductDetail',
    'StockRecordList', 'StockRecordDetail',
    'UserList', 'UserDetail',
    'OptionList', 'OptionDetail',
    'CountryList', 'CountryDetail',
    'ShippingMethodList', 'ShippingMethodDetail',
)

Basket = get_model('basket', 'Basket')
LineAttribute = get_model('basket', 'LineAttribute')
Product = get_model('catalogue', 'Product')
StockRecord = get_model('partner', 'StockRecord')
Option = get_model('catalogue', 'Option')
User = auth.get_user_model()
ShippingMethod = get_model('shipping', 'OrderAndItemCharges')
Country = get_model('address', 'Country')


# TODO: For all API's in this file, the permissions should be checked if they
# are sensible.
class CountryList(generics.ListAPIView):
    serializer_class = serializers.CountrySerializer
    model = Country
class CountryDetail(generics.RetrieveAPIView):
    serializer_class = serializers.CountrySerializer
    model = Country


class ShippingMethodList(generics.ListAPIView):
    serializer_class = serializers.ShippingMethodSerializer
    model = ShippingMethod
class ShippingMethodDetail(generics.RetrieveAPIView):
    serializer_class = serializers.ShippingMethodSerializer
    model = ShippingMethod


class BasketList(generics.ListCreateAPIView):
    model = Basket
    serializer_class = serializers.BasketSerializer
    permission_classes = (IsAdminUser,)
class BasketDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Basket
    serializer_class = serializers.BasketSerializer
    permission_classes = (permissions.IsAdminUserOrRequestOwner,)


class LineAttributeList(generics.ListCreateAPIView):
    model = LineAttribute
    serializer_class = serializers.LineAttributeSerializer
class LineAttributeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = LineAttribute
    serializer_class = serializers.LineAttributeSerializer


class ProductList(generics.ListAPIView):
    model = Product
    serializer_class = serializers.ProductLinkSerializer
class ProductDetail(generics.RetrieveAPIView):
    model = Product
    serializer_class = serializers.ProductSerializer


class StockRecordList(generics.ListAPIView):
    model = StockRecord
    serializer_class = serializers.StockRecordSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            self.queryset = self.get_queryset().filter(product__id=pk)

        return super(StockRecordList, self).get(request, *args, **kwargs)
class StockRecordDetail(generics.RetrieveAPIView):
    model = StockRecord
    serializer_class = serializers.StockRecordSerializer


class UserList(generics.ListAPIView):
    model = User
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAdminUser,)
class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAdminUser,)


class OptionList(generics.ListAPIView):
    model = Option
    serializer_class = serializers.OptionSerializer
class OptionDetail(generics.RetrieveAPIView):
    model = Option
    serializer_class = serializers.OptionSerializer

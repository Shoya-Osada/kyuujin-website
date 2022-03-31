from rest_framework import generics
from jobs.models import JobOffer
from jobs.api.permissions import IsAdminUserOrReadOnly
from jobs.api.serializers import JobOfferSerializer


#Django REST Framework は、GenericAPIView の中に一般的に必要な開発のコードをすでに用意されている。

class ListView(generics.ListCreateAPIView):
    #querysetにJobOfferのすべてを降順に入れていく
    queryset = JobOffer.objects.all().order_by("-id")
    #serializer_classにJobOfferSerializerを入れる
    serializer_class = JobOfferSerializer
    #フロントでログイン機能を実装していないから、下記はコメントアウト
    # permission_classes = [IsAdminUserOrReadOnly]

#generics.RetrieveUpdateDestroyAPIViewを継承することで、詳細を作成することができる。
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    #querysetにJobOfferのすべてを入れていく
    queryset = JobOffer.objects.all()
    #serializer_classにJobOfferSerializerを入れる
    serializer_class = JobOfferSerializer
    #フロントでログイン機能を実装していないから、下記はコメントアウト
    # permission_classes = [IsAdminUserOrReadOnly]
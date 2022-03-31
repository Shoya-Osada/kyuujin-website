from rest_framework import serializers
from jobs.models import JobOffer

#serializers の ModelSerializer クラスを継承すことにより、簡単に書く事が可能
class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = "__all__"
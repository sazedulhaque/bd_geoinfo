from django.core.serializers import serialize
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.translation import ugettext_lazy as _

from . import models

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    DistrictSerializer,
    # UpazilaSerializer,
    # UnionSerializer
)
# Create your views here.


class ajax_district_list(APIView):

    def post(self, request, *args, **kwargs):

        q = request.POST
        print(q)
        districtList = models.District.objects.filter(
            division_id=q['division_id'])
        print('districtList.count()-------------')
        print(districtList.count())

        serializer = DistrictSerializer(districtList, many=True)
        return Response(serializer.data)

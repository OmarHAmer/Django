from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

# @api_view(['GET', 'POST'])
# def jobapi(request):

#     job = Job.objects.all()

#     data = JobSerializer (job,many=True).data

#     return Response({'data':data})

# @api_view(['GET'])
# def job_details(request,id):

#     job = Job.objects.get(id =id)

#     data = JobSerializer(job).data

#     return Response({'data':data})


class JobApi(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
    
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def jobapi(request):

    job = Job.objects.all()

    data = JobSerializer (job,many=True).data

    return Response({'data':data})
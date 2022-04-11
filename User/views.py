from django.shortcuts import render
from .forms import AddJobForm
from .models import Jobs
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import JobSerializer

# Create your views here.
def Jobs_Page(request):
    form_data= AddJobForm()
    return render(request, 'User/index.html', {'form': form_data})

class JobViewSet(ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
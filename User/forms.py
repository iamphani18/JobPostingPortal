from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Jobs


class AddJobForm(ModelForm):
    class Meta:
        model = Jobs
        fields = "__all__"
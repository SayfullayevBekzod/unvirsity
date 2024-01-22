from django import forms

from courses.models import Speciality


class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=36)
    date = forms.DateField()
    is_active = forms.BooleanField()

    def save(self):
        name = self.cleaned_data["name"]
        date = str(self.cleaned_data["date"])
        is_active = self.cleaned_data["is_active"]
        speciality = Speciality.objects.create(name=name, start_date=date, is_active=is_active)
        return speciality

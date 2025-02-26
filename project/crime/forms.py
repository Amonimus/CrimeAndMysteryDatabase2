from django import forms

from .models import Case, Crime


class CrimeForm(forms.ModelForm):
	name = forms.CharField()

	class Meta:
		model = Crime
		fields = "__all__"


class CaseForm(forms.ModelForm):
	name = forms.CharField()

	class Meta:
		model = Case
		fields = "__all__"

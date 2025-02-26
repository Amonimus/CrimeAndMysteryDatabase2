from django import forms

from .models import Character, Work


class WorkForm(forms.ModelForm):
	title = forms.CharField()
	author = forms.CharField(required=False)
	release_date = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
	description = forms.CharField(widget=forms.Textarea(), required=False)

	class Meta:
		model = Work
		fields = "__all__"

	def clean(self):
		cleaned_data: dict = super().clean()
		release_date = cleaned_data.get("release_date", None)
		if release_date == "":
			cleaned_data["release_date"] = None


class CharacterForm(forms.ModelForm):
	name = forms.CharField()

	class Meta:
		model = Character
		fields = "__all__"

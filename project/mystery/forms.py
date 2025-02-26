from django import forms
from django.db.models import QuerySet

from work.models import Character
from .models import Incident, PersonOfInterst, Clue


class IncidentForm(forms.ModelForm):
	name = forms.CharField()
	people_of_interest = forms.ModelMultipleChoiceField(queryset=Character.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

	def __init__(self, *args, **kwargs):
		instance: Incident | None = kwargs.get("instance", None)
		super().__init__(*args, **kwargs)
		if instance:
			self.fields['people_of_interest'].queryset = Character.objects.filter(work=instance.case.work)
			self.fields['people_of_interest'].initial = Character.objects.filter(personofinterst__incident=instance)

	class Meta:
		model = Incident
		fields = "__all__"

	def save(self, commit=True):
		instance: Incident = super().save()
		characters: list[Character] = self.cleaned_data['people_of_interest']
		people_of_interest_ids: list[PersonOfInterst] = []
		for character in characters:
			person_of_interest, new = PersonOfInterst.objects.get_or_create(character=character, incident=instance)
			people_of_interest_ids.append(person_of_interest.id)
		extras: QuerySet | list[PersonOfInterst] = PersonOfInterst.objects.exclude(id__in=people_of_interest_ids)
		extras.delete()
		return instance


class ClueForm(forms.ModelForm):
	name = forms.CharField()

	class Meta:
		model = Clue
		fields = "__all__"


class PersonOfInterstForm(forms.ModelForm):
	reason = forms.ChoiceField(choices=PersonOfInterst.InterestReasonChoices.choices)

	class Meta:
		model = PersonOfInterst
		fields = "__all__"

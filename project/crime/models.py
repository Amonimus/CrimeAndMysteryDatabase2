from django.db import models
from django.shortcuts import redirect, reverse

from work.models import Work, Character


class Crime(models.Model):
	objects: models.Manager = models.Manager()
	name: str = models.TextField()
	description: str = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ["name"]

	def __repr__(self) -> str:
		return f"Crime({self.name})"

	def __str__(self) -> str:
		return self.name

	def get_absolute_url(self) -> str:
		return reverse("crime", kwargs={"crime_id": self.pk})

	def culprits(self):
		from mystery.models import PersonOfInterst
		return PersonOfInterst.objects.filter(incident__crime=self, reason=PersonOfInterst.InterestReasonChoices.culprit)

	def victims(self):
		from mystery.models import PersonOfInterst
		return PersonOfInterst.objects.filter(incident__crime=self, reason=PersonOfInterst.InterestReasonChoices.victim)

class Case(models.Model):
	objects: models.Manager = models.Manager()
	name: str = models.TextField()
	work: Work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='cases')
	description: str = models.TextField(null=True, blank=True)
	resolved: bool = models.BooleanField(default=True)
	resolution: str = models.TextField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	class Meta:
		ordering = ["name"]

	def __repr__(self) -> str:
		return f"Case({self.name})"

	def __str__(self) -> str:
		return self.name

	def get_view(self):
		return redirect("case", case_id=self.pk)

	def get_absolute_url(self) -> str:
		return reverse("case", kwargs={"case_id": self.pk})

	@property
	def people_of_interest(self):
		return Character.objects.filter(personofinterst__incident__case=self)

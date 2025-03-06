from datetime import date

from django.db import models
from django.db.models import Q
from django.shortcuts import redirect, reverse


class Work(models.Model):
	objects: models.Manager = models.Manager()
	title: str = models.TextField()
	author: str = models.TextField(null=True, blank=True)
	release_date: date = models.DateField(null=True, blank=True)
	description: str = models.TextField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	class Meta:
		ordering = ["title"]

	def __repr__(self) -> str:
		return f"Work({self.title})"

	def __str__(self) -> str:
		return self.title

	def get_view(self):
		return redirect("work", work_id=self.pk)

	def get_absolute_url(self) -> str:
		return reverse("work", kwargs={"work_id": self.pk})


class Character(models.Model):
	objects: models.Manager = models.Manager()
	name: str = models.TextField()
	work: Work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="characters")
	description: str = models.TextField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	class Meta:
		ordering = ["name"]

	def __repr__(self) -> str:
		return f"Character({self.name})"

	def __str__(self):
		return self.name

	def get_view(self):
		return redirect("character", work_id=self.pk)

	def get_absolute_url(self) -> str:
		return reverse("character", kwargs={"character_id": self.pk})

	@property
	def involvements(self) -> list["PersonOfInterst"]:
		from mystery.models import PersonOfInterst
		query: Q = Q(reason=PersonOfInterst.InterestReasonChoices.culprit)
		query.add(Q(reason=PersonOfInterst.InterestReasonChoices.accomplice), Q.OR)
		query.add(Q(character=self), Q.AND)
		involvements: list[PersonOfInterst] = PersonOfInterst.objects.filter(query)
		return involvements

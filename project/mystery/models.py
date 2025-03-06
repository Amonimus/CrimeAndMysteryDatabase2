from django.db import models
from django.shortcuts import redirect, reverse

from crime.models import Case, Crime
from work.models import Character


class Clue(models.Model):
	objects: models.Manager = models.Manager()
	name: str = models.TextField()
	case: Case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='clues')
	description: str = models.TextField(null=True, blank=True)
	order: int = models.IntegerField(default=1)
	image = models.ImageField(null=True, blank=True)

	class Meta:
		ordering = ["name"]

	def __repr__(self) -> str:
		return f"Clue({self.name} for {self.case.name})"

	def __str__(self) -> str:
		return self.name

	def get_view(self):
		return redirect("clue", clue_id=self.pk)

	def get_absolute_url(self) -> str:
		return reverse("clue", kwargs={"clue_id": self.pk})


class Incident(models.Model):
	objects: models.Manager = models.Manager()
	name: str = models.TextField()
	case: Case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='incidents')
	crime: Crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, null=True, blank=True, related_name='crime_incident')
	description: str = models.TextField(null=True, blank=True)
	order: int = models.IntegerField(default=1)
	image = models.ImageField(null=True, blank=True)

	class Meta:
		ordering = ["case__name", "order", "name"]

	def __repr__(self) -> str:
		return f"Incident({self.name})"

	def __str__(self) -> str:
		return self.name

	def get_view(self):
		return redirect("incident", incident_id=self.pk)

	def get_absolute_url(self) -> str:
		return reverse("incident", kwargs={"incident_id": self.pk})


class Relation(models.Model):
	relation_from: Character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='relation_from')
	relation_to: Character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='relation_to')
	description: str = models.TextField()

	class Meta:
		ordering = ["relation_from__name"]

	def __repr__(self) -> str:
		return f"Relation({self.relation_from.name} -> {self.relation_to.name})"

	def __str__(self):
		return f"{self.relation_from.name} -> {self.relation_to.name}"


class PersonOfInterst(models.Model):
	class InterestReasonChoices(models.TextChoices):
		unknown = "unknown"
		victim = "victim"
		suspect = "suspect"
		culprit = "culprit"
		accomplice = "accomplice"
		witness = "witness"

	objects: models.Manager = models.Manager()
	incident: Incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name="people_of_interest")
	character: Character = models.ForeignKey(Character, on_delete=models.CASCADE)
	reason: str = models.TextField(choices=InterestReasonChoices.choices, default=InterestReasonChoices.unknown, null=True, blank=True)

	class Meta:
		ordering = ["incident__name", "character__name"]

	def __repr__(self) -> str:
		return f"PersonOfInterst({self.incident.name} {self.character.name})"

	def __str__(self) -> str:
		return self.character.name

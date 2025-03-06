from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View

from crime.models import Case
from .forms import IncidentForm, ClueForm
from .models import Incident, Clue


class IncidentView(View):
	def get(self, request: HttpRequest, incident_id: int) -> HttpResponse:
		incident: Incident = Incident.objects.get(id=incident_id)
		context: dict = {"incident": incident}
		return render(request, "mystery/incident.html", context)


class EditIncidentView(View):
	def get(self, request: HttpRequest, incident_id: int = None, case_id: int = None) -> HttpResponse:
		if incident_id:
			incident: Incident = Incident.objects.get(id=incident_id)
			form: IncidentForm = IncidentForm(instance=incident)
		else:
			if case_id:
				case: Case = Case.objects.get(id=case_id)
				form: IncidentForm = IncidentForm(case=case)
				form.initial["case"] = case
			else:
				form: IncidentForm = IncidentForm()
		context: dict = {"form": form}
		return render(request, "mystery/edit_incident.html", context)

	def post(self, request: HttpRequest, incident_id: int = None, case_id: int = None) -> HttpResponse:
		if incident_id:
			incident: Incident = Incident.objects.get(id=incident_id)
			form: IncidentForm = IncidentForm(request.POST, request.FILES, instance=incident)
		else:
			form: IncidentForm = IncidentForm(request.POST, request.FILES)
		if form.is_valid():
			instance: Case = form.save()
			return instance.get_view()
		else:
			context: dict = {"form": form}
			return render(request, "mystery/edit_incident.html", context)


class DeleteIncidentView(View):
	def get(self, request: HttpRequest, incident_id: int) -> HttpResponse:
		incident: Incident = Incident.objects.get(id=incident_id)
		incident.delete()
		return incident.case.get_view()


class ClueView(View):
	def get(self, request: HttpRequest, clue_id: int) -> HttpResponse:
		clue: Clue = Clue.objects.get(id=clue_id)
		context: dict = {"clue": clue}
		return render(request, "mystery/clue.html", context)


class EditClueView(View):
	def get(self, request: HttpRequest, clue_id: int = None, case_id: int = None) -> HttpResponse:
		if clue_id:
			clue: Clue = Clue.objects.get(id=clue_id)
			form: ClueForm = ClueForm(instance=clue)
		else:
			if case_id:
				case: Case = Case.objects.get(id=case_id)
				form: ClueForm = ClueForm()
				form.initial["case"] = case
			else:
				form: ClueForm = ClueForm()
		context: dict = {"form": form}
		return render(request, "mystery/edit_clue.html", context)

	def post(self, request: HttpRequest, clue_id: int = None, case_id: int = None) -> HttpResponse:
		if clue_id:
			clue: Clue = Clue.objects.get(id=clue_id)
			form: ClueForm = ClueForm(request.POST, request.FILES, instance=clue)
		else:
			form: ClueForm = ClueForm(request.POST, request.FILES)
		if form.is_valid():
			instance: Clue = form.save()
			return instance.case.get_view()
		else:
			context: dict = {"form": form}
			return render(request, "mystery/edit_clue.html", context)


class DeleteClueView(View):
	def get(self, request: HttpRequest, clue_id: int) -> HttpResponse:
		clue: Clue = Clue.objects.get(id=clue_id)
		clue.delete()
		return clue.case.get_view()

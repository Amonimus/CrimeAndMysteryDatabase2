from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from work.models import Work
from .forms import CaseForm, CrimeForm
from mystery.forms import PersonOfInterstForm
from .models import Case, Crime
from mystery.models import PersonOfInterst


class CrimeListView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		crimes: list[Crime] = Crime.objects.all()
		context: dict = {"crimes": crimes}
		return render(request, "crime/crimes.html", context)


class CrimeView(View):
	def get(self, request: HttpRequest, crime_id: int) -> HttpResponse:
		crime: Crime = Crime.objects.get(id=crime_id)
		context: dict = {"crime": crime}
		return render(request, "crime/crime.html", context)


class EditCrimeView(View):

	def get(self, request: HttpRequest, crime_id: int = None) -> HttpResponse:
		if crime_id:
			crime: Crime = Crime.objects.get(id=crime_id)
			form: CrimeForm = CrimeForm(instance=crime)
		else:
			form: CrimeForm = CrimeForm()
		context: dict = {"form": form}
		return render(request, "crime/edit_crime.html", context)

	def post(self, request: HttpRequest, crime_id: int = None) -> HttpResponse:
		if crime_id:
			crime: Crime = Crime.objects.get(id=crime_id)
			form: CrimeForm = CrimeForm(request.POST, instance=crime)
		else:
			form: CrimeForm = CrimeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('crimes')
		else:
			context: dict = {"form": form}
			return render(request, "crime/edit_crime.html", context)


class DeleteCrimeView(View):
	def get(self, request: HttpRequest, crime_id: int) -> HttpResponse:
		crime: Crime = Crime.objects.get(id=crime_id)
		crime.delete()
		return redirect('crimes')


class CaseView(View):
	def get(self, request: HttpRequest, case_id: int) -> HttpResponse:
		case: Case = Case.objects.get(id=case_id)
		context: dict = {"case": case}
		return render(request, "crime/case.html", context)


class EditCaseView(View):
	def get(self, request: HttpRequest, case_id: int = None, work_id: int = None) -> HttpResponse:
		if case_id:
			case: Case = Case.objects.get(id=case_id)
			form: CaseForm = CaseForm(instance=case)
		else:
			if work_id:
				work: Work = Work.objects.get(id=work_id)
				form: CaseForm = CaseForm()
				form.initial["work"] = work
			else:
				form: CaseForm = CaseForm()
		context: dict = {"form": form}
		return render(request, "crime/edit_case.html", context)

	def post(self, request: HttpRequest, case_id: int = None, work_id: int = None) -> HttpResponse:
		if case_id:
			case: Case = Case.objects.get(id=case_id)
			form: CaseForm = CaseForm(request.POST, instance=case)
		else:
			form: CaseForm = CaseForm(request.POST)
		if form.is_valid():
			instance: Case = form.save()
			return instance.get_view()
		else:
			context: dict = {"form": form}
			return render(request, "crime/edit_case.html", context)


class EditInterestView(View):

	def get(self, request: HttpRequest, interest_id: int = None) -> HttpResponse:
		interest: PersonOfInterst = PersonOfInterst.objects.get(id=interest_id)
		form: PersonOfInterstForm = PersonOfInterstForm(instance=interest)
		context: dict = {"form": form}
		return render(request, "crime/edit_interest.html", context)

	def post(self, request: HttpRequest, interest_id: int = None) -> HttpResponse:
		interest: PersonOfInterst = PersonOfInterst.objects.get(id=interest_id)
		form: PersonOfInterstForm = PersonOfInterstForm(request.POST, instance=interest)
		if form.is_valid():
			instance: PersonOfInterst = form.save()
			return instance.incident.get_view()
		else:
			context: dict = {"form": form}
			return render(request, "crime/edit_interest.html", context)

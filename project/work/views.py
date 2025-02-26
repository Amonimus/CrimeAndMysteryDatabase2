from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import CharacterForm, WorkForm
from .models import Character, Work


class WorkListView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		works: list[Work] = Work.objects.all()
		context: dict = {"works": works}
		return render(request, "work/works.html", context)


class WorkView(View):
	def get(self, request: HttpRequest, work_id: int) -> HttpResponse:
		work: Work = Work.objects.get(id=work_id)
		context: dict = {"work": work}
		return render(request, "work/work.html", context)


class EditWorkView(View):
	def get(self, request: HttpRequest, work_id: int = None) -> HttpResponse:
		if work_id:
			work: Work = Work.objects.get(id=work_id)
			form: WorkForm = WorkForm(instance=work)
		else:
			form: WorkForm = WorkForm()
		context: dict = {"form": form}
		return render(request, "work/edit_work.html", context)

	def post(self, request: HttpRequest, work_id: int = None) -> HttpResponse:
		if work_id:
			work: Work = Work.objects.get(id=work_id)
			form: WorkForm = WorkForm(request.POST, instance=work)
		else:
			form: WorkForm = WorkForm(request.POST)
		if form.is_valid():
			instance: Work = form.save()
			return instance.get_view()
		else:
			context: dict = {"form": form}
			return render(request, "work/edit_work.html", context)


class DeleteWorkView(View):
	def get(self, request: HttpRequest, work_id: int) -> HttpResponse:
		work: Work = Work.objects.get(id=work_id)
		work.delete()
		return redirect('works')


class CharacterView(View):
	def get(self, request: HttpRequest, character_id: int) -> HttpResponse:
		character: Character = Character.objects.get(id=character_id)
		context: dict = {"character": character}
		return render(request, "work/character.html", context)


class EditCharacterView(View):
	def get(self, request: HttpRequest, character_id: int = None, work_id: int = None) -> HttpResponse:
		if character_id:
			character: Character = Character.objects.get(id=character_id)
			form: CharacterForm = CharacterForm(instance=character)
		else:
			form: CharacterForm = CharacterForm()
		if work_id:
			work: Work = Work.objects.get(id=work_id)
			form.initial["work"] = work
		context: dict = {"form": form}
		return render(request, "work/edit_character.html", context)

	def post(self, request: HttpRequest, character_id: int = None, work_id: int = None) -> HttpResponse:
		if character_id:
			character: Character = Character.objects.get(id=character_id)
			form: CharacterForm = CharacterForm(request.POST, instance=character)
		else:
			form: CharacterForm = CharacterForm(request.POST)
		if form.is_valid():
			instance: Character = form.save()
			return instance.work.get_view()
		else:
			context: dict = {"form": form}
			return render(request, "work/edit_character.html", context)


class DeleteCharacterView(View):
	def get(self, request: HttpRequest, character_id: int) -> HttpResponse:
		character: Character = Character.objects.get(id=character_id)
		character.delete()
		return character.work.get_view()

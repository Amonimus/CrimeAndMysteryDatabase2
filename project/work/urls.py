from django.urls import path

from .views import WorkView, WorkListView, EditWorkView, EditCharacterView, CharacterView, DeleteCharacterView, DeleteWorkView

urlpatterns: list = [
	path("works", WorkListView.as_view(), name="works"),
	path("work/<int:work_id>", WorkView.as_view(), name="work"),
	path("edit_work", EditWorkView.as_view(), name="edit_work"),
	path("edit_work/<int:work_id>", EditWorkView.as_view(), name="edit_work"),
	path("delete_work/<int:work_id>", DeleteWorkView.as_view(), name="delete_work"),

	path("character/<int:character_id>", CharacterView.as_view(), name="character"),
	path("work/<int:work_id>/edit_character", EditCharacterView.as_view(), name="add_character"),
	path("edit_character", EditCharacterView.as_view(), name="edit_character"),
	path("edit_character/<int:character_id>", EditCharacterView.as_view(), name="edit_character"),
	path("delete_character/<int:character_id>", DeleteCharacterView.as_view(), name="delete_character"),
]

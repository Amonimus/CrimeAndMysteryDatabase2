from django.urls import path

from .views import IncidentView, EditIncidentView, DeleteIncidentView, DeleteClueView, EditClueView, ClueView

urlpatterns: list = [
	path("incident/<int:incident_id>", IncidentView.as_view(), name="incident"),
	path("add_incident/<int:case_id>", EditIncidentView.as_view(), name="add_incident"),
	path("edit_incident/<int:incident_id>", EditIncidentView.as_view(), name="edit_incident"),
	path("delete_incident/<int:incident_id>", DeleteIncidentView.as_view(), name="delete_incident"),

	path("clue/<int:clue_id>", ClueView.as_view(), name="clue"),
	path("add_clue/<int:case_id>", EditClueView.as_view(), name="add_clue"),
	path("edit_clue/<int:clue_id>", EditClueView.as_view(), name="edit_clue"),
	path("delete_clue/<int:clue_id>", DeleteClueView.as_view(), name="delete_clue"),
]

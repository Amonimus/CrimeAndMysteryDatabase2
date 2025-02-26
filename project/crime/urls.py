from django.urls import path

from .views import EditCrimeView, CaseView, CrimeListView, EditCaseView, CrimeView, DeleteCrimeView, EditInterestView

urlpatterns: list = [
	path("crimes", CrimeListView.as_view(), name="crimes"),
	path("crime/<int:crime_id>", CrimeView.as_view(), name="crime"),
	path("add_crime", EditCrimeView.as_view(), name="add_crime"),
	path("edit_crime/<int:crime_id>", EditCrimeView.as_view(), name="edit_crime"),
	path("delete_crime/<int:crime_id>", DeleteCrimeView.as_view(), name="delete_crime"),

	path("case/<int:case_id>", CaseView.as_view(), name="case"),
	path("work/<int:work_id>/add_case", EditCaseView.as_view(), name="add_case"),
	path("edit_case/<int:case_id>", EditCaseView.as_view(), name="edit_case"),

	path("edit_interest/<int:interest_id>", EditInterestView.as_view(), name="edit_interest"),
]

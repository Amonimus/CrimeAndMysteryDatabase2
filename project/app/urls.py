from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import IndexView, LoginView, LogoutView, RegistrationView, UnauthenticatedView, ForbiddenView, ToggleEditingView

urlpatterns = [
	path("admin/", admin.site.urls),
	path("login", LoginView.as_view(), name="login"),
	path("logout", LogoutView.as_view(), name="logout"),
	path("register", RegistrationView.as_view(), name="register"),
	path("unauthenticated", UnauthenticatedView.as_view(), name="unauthenticated"),
	path("forbidden", ForbiddenView.as_view(), name="forbidden"),
	path("", IndexView.as_view(), name='index'),
	path("toggle_edit", ToggleEditingView.as_view(), name='toggle_edit'),
	path("", include("work.urls")),
	path("", include("crime.urls")),
	path("", include("mystery.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

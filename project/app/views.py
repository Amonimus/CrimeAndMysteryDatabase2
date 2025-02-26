from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View


class CustomAuthenticationForm(AuthenticationForm):

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		try:
			self.user_cache = User._default_manager.get(username__iexact=username)
			if self.user_cache is None:
				raise self.get_invalid_login_error()
			self.confirm_login_allowed(self.user_cache)
			self.user_cache = authenticate(username=self.user_cache.username, password=password)
			if self.user_cache is None:
				raise self.get_invalid_login_error()
		except User.DoesNotExist:
			raise self.get_invalid_login_error()
		except Exception as e:
			print(f'LOGIN EXCEPTION: {e}')
			raise e
		return self.cleaned_data


class LoginView(View):
	form_class = CustomAuthenticationForm
	template_name = 'auth/login.html'

	def get(self, request: HttpRequest) -> HttpResponse:
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request: HttpRequest) -> HttpResponse:
		form: CustomAuthenticationForm = self.form_class(data=request.POST)
		if form.is_valid():
			user: User = form.get_user()
			if user is not None:
				login(request, user)
				return redirect('index')
		else:
			print(f'FORM {form.errors} {form.non_field_errors()}')
		return render(request, self.template_name, {'form': form})


class RegistrationView(View):
	template_name = 'auth/register.html'

	def get(self, request: HttpRequest) -> HttpResponse:
		return render(request, self.template_name)

	def post(self, request: HttpRequest) -> HttpResponse:
		data: dict = request.POST.copy()
		if data['password'] != data['confirm_password']:
			raise Exception("Password don't match")
		user: User = User.objects.create_user(
			username=data['username'],
			email=data['email'],
			password=data['password']
		)
		login(request, user)
		return redirect('index')


class LogoutView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		request.session.flush()
		logout(request)
		return redirect('index')


class ForbiddenView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		return render(request, "auth/forbidden.html", status=401)


class UnauthenticatedView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		return render(request, "auth/unauthenticated.html", status=403)


class IndexView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		return render(request, "index.html")


class ToggleEditingView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		user: User = request.user
		if user.is_authenticated:
			can_edit, new = Group.objects.get_or_create(name="can_edit")
			if can_edit in user.groups.all():
				can_edit.user_set.remove(user)
			else:
				can_edit.user_set.add(user)
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

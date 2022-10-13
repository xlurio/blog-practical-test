from django.contrib.auth import views

from authentication.forms import AuthenticationForm


class LoginView(views.LoginView):
    """View for logging in"""

    form_class = AuthenticationForm
    template_name = "users/login.html"
    redirect_authenticated_user = True


class LogoutView(views.LogoutView):
    """View for logging in"""

    template_name = "users/logged_out.html"

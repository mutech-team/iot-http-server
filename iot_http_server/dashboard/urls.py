from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views

# TODO: Address the comments about redirecting user to another pages after completed actions
# TODO: Currently, url paths bound to auth_views are default named to eliminate the need to supply success_url to every auth_view
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
    path('password_reset',
         auth_views.PasswordResetView.as_view(template_name="dashboard/accounts/forgot_password.html",
                                              html_email_template_name="email/password_reset_email.html",
                                              # success_url="where to redirect after requesting password change email, currently to password_reset/done
                                              ),
         name='password_reset'),
    path('password_reset/done',
         auth_views.PasswordResetDoneView.as_view(
             template_name="dashboard/accounts/password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="dashboard/accounts/reset_password.html",
                                                     # success_url="where to redirect after password change via email link, currently to reset/done,
                                                     ),
         name='password_reset_confirm'),
    path('reset/done',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="dashboard/accounts/password_reset_successful.html"),
         name='password_reset_complete'),
    path('password_change',
         auth_views.PasswordChangeView.as_view(template_name="dashboard/accounts/change_password.html",
                                               # success_url="where to redirect after password change, currently to password_change/done ",
                                               ),
         name='password_change'),
    path('password_change/done',
         auth_views.PasswordChangeDoneView.as_view(
             template_name="dashboard/accounts/password_change_successful.html"),
         name='password_change_done'),

]

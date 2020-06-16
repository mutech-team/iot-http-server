from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
    # TODO: Specify template for sending the reset password eMail
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="dashboard/forgot_password.html",
                                                                 html_email_template_name="email/password_reset_email.html",
                                                                 ),
         name='password_reset'),
    path('password_reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name="dashboard/password_reset_done.html"),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="dashboard/reset_password.html"),
         name='password_reset_confirm'),
    path('password_reset/done',
         auth_views.PasswordResetCompleteView.as_view(template_name="dashboard/password_reset_successful.html"),
         name='password_reset_complete'),
    # TODO : Other urls are for changing user password manually, if user know old pass, enable later
    # path('password_change', auth_views.PasswordChangeView.as_view(),
    #    name='password_change'),
    # path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]

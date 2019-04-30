from django.urls import reverse, resolve 
from users.views import register, profile
from django.contrib.auth.views import (LoginView, 
                                        LogoutView, 
                                        PasswordResetView, 
                                        PasswordResetDoneView, 
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView)

class TestUrls:
    def test_register_url(self):
        path = reverse('register')

        assert resolve(path).func == register

    def test_profile_url(self):
        path = reverse('profile')

        assert resolve(path).func == profile

    def test_login_url(self):
        path = reverse('login')

        assert resolve(path).func.view_class == LoginView

    def test_logout_url(self):
        path = reverse('logout')

        assert resolve(path).func.view_class == LogoutView

        
    def test_password_reset_url(self):
        path = reverse('password_reset')

        assert resolve(path).func.view_class == PasswordResetView

    def test_password_reset_done_url(self):
        path = reverse('password_reset_done')

        assert resolve(path).func.view_class == PasswordResetDoneView        


    def test_password_reset_confirm_url(self):
        uidb64 = 'abc'
        token = 'abc'
        path = reverse('password_reset_confirm', kwargs={'uidb64':uidb64, 'token':token})

        assert resolve(path).func.view_class == PasswordResetConfirmView                

    def test_password_reset_complete_url(self):
        path = reverse('password_reset_complete')

        assert resolve(path).func.view_class == PasswordResetCompleteView        

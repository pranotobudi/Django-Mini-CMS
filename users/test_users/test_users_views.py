from django.test import RequestFactory, TestCase
from django.urls import reverse
from users.views import register, profile
from users.models import Profile 
from django.contrib.auth.models import User
from mixer.backend.django import mixer

class TestViews(TestCase):

    def test_register_get_status_code(self):
        path = reverse('register')
        request = RequestFactory().get(path)
        request.method = 'GET'
        response = register(request)
        assert response.status_code == 200

    def test_register_get_template_used(self):
        path = reverse('register')
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'users/register.html')        


    def test_profile_get_status_code(self):
        user = mixer.blend(User)
        Profile.objects.create(
            user = user,
            image = 'default.jpg'
        )
        path = reverse('profile')
        request = RequestFactory().get(path)
        request.method = 'GET'
        request.user = user
        response = profile(request)
        assert response.status_code == 200

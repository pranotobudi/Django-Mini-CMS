from users.models import Profile
from mixer.backend.django import mixer 
from django.contrib.auth.models import User 


class TestModels:
    def test_profile_db_is_created(self, db):
        Profile.objects.create(
            user = mixer.blend(User),
            image = 'default.jpg'
        )
        total_profile = Profile.objects.all().count()
        assert total_profile == 1

    def test_profile_db_is_empty(self, db):
        total_profile = Profile.objects.all().count()
        assert total_profile == 0

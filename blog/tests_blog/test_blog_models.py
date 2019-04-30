
from blog.models import Post 
from django.contrib.auth.models import User, AnonymousUser
import pytest
from mixer.backend.django import mixer 
class TestModels:
    # @pytest.fixture #it declare this function as fixture, we don't mean it, we want to use db fixture
    def test_post_db_is_created(self, db):
        #db is a fixture
        post = Post.objects.create(
            title = 'title 1',
            content = 'content 1',
            # date_posted = models.DateTimeField(default=timezone.now)
            author = mixer.blend(User) #mixer makes us easy to assign User, manually we need User.objects.get(id)
        )
        total_post = Post.objects.all().count()
        # print("############total POST: ", total_post)
        assert total_post == 1

    def test_post_db_not_created(self, db):
        total_post = Post.objects.all().count()
        # print("############total POST: ", total_post)
        assert total_post == 0

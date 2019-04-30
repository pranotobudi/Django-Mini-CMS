from django.urls import reverse, resolve
from blog.views import PostListView, PostDetailView, PostUpdateView, PostDeleteView, post_load, UserPostListView

class TestUrls:
    def test_blog_home_url(self):
        path = reverse('blog-home')
        assert resolve(path).func.view_class == PostListView

    def test_post_detail_url(self):
        path = reverse('post-detail', args=(1,))
        assert resolve(path).func.view_class == PostDetailView        

    def test_post_update_url(self):
        path = reverse('post-update', args=(1,))
        assert resolve(path).func.view_class == PostUpdateView                

    def test_post_delete_url(self):
        path = reverse('post-delete', args=(1,))
        assert resolve(path).func.view_class == PostDeleteView                        

    def test_post_load_url(self):
        path = reverse('post-load')
        assert resolve(path).func == post_load

    def test_post_user_url(self):
        path = reverse('post-user', args=('user1',))
        assert resolve(path).func.view_class == UserPostListView  
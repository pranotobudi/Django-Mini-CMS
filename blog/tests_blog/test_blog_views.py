from django.urls import reverse
from django.test import RequestFactory
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from blog.models import Post
from mixer.backend.django import mixer 

class TestViews(TestCase):

    def test_post_list_view_response_status_code(self):
        path = reverse('blog-home')
        # request = RequestFactory().get(path)
        response = self.client.get(path)
        assert response.status_code == 200

    def test_post_list_view_response_template_used(self):
        path = reverse('blog-home')
        # request = RequestFactory().get(path)
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_user_post_list_view_response_status_code(self):
        user = mixer.blend(User)
        path = reverse('post-user', args=(user,))
        # request = RequestFactory().get(path)
        response = self.client.get(path)
        assert response.status_code == 200

    def test_user_post_list_view_response_template_used(self):
        user = mixer.blend(User)
        path = reverse('post-user', args=(user,))
        # request = RequestFactory().get(path)
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'blog/post_user.html')

    def test_post_detail_view_response_status_code(self):
        post = mixer.blend(Post)
        path = reverse('post-detail', args=(post.id,))
        # request = RequestFactory().get(path)
        response = self.client.get(path)
        assert response.status_code == 200

    def test_post_detail_view_response_template_used(self):
        post = mixer.blend(Post)
        path = reverse('post-detail', args=(post.id,))
        # request = RequestFactory().get(path)
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_create_view_response_status_code(self):
        # here we use RequestFactory not client.get, another alternative
        path = reverse('post-create', )
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = PostCreateView.as_view()(request)
        assert response.status_code == 200

    def test_post_create_view_response_form_field_name(self):
        # here we use RequestFactory not client.get, another alternative
        path = reverse('post-create', )
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = PostCreateView.as_view()(request)
        response.render() #we must render it first before access response.content
        assert  b'title' in response.content #response.content is in byte, 'title' is form field name
        #we can't ave assertTemplateUsed, it is only for client.get


    # def test_post_update_view_response_status_code(self):
    #     # here we use RequestFactory not client.get, another alternative
    #     post = mixer.blend(Post)
    #     path = reverse('post-update', kwargs={'pk':post.id})
    #     request = RequestFactory().get(path)
    #     request.user = mixer.blend(User)

    #     response = PostUpdateView.as_view()(request)
    #     assert response.status_code == 200

    # def test_post_update_view_response_form_field_name(self):
    #     # here we use RequestFactory not client.get, another alternative
    #     post = mixer.blend(Post)
    #     path = reverse('post-update', kwargs={'pk':post.id})
    #     request = RequestFactory().get(path)
    #     request.user = mixer.blend(User)
    #     response = PostUpdateView.as_view()(request)
    #     response.render() #we must render it first before access response.content
    #     assert  b'title' in response.content #response.content is in byte
    #     #we can't ave assertTemplateUsed, it is only for client.get        

from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class TestForms:

    def test_user_register_form_valid(self, db):
        form = UserRegisterForm(data={
            'username': 'username1',
            'email': 'username1@email.com',
            'password1': 'username1password',
            'password2': 'username1password',
        })
        assert form.is_valid() == True

    def test_user_register_form_not_valid(self, db):
        form = UserRegisterForm(data={
            'username': 'username1',
            'email': 'username1', #email not valid
            'password1': 'username1password',
            'password2': 'username1password',
        })
        assert form.is_valid() == False        

    def test_user_update_form_valid(self, db):
        form = UserUpdateForm(data={
            'username': 'username1',
            'email': 'username1@email.com',
        })
        assert form.is_valid() == True

    def test_user_update_form_not_valid(self, db):
        form = UserUpdateForm(data={
            'username': 'username1',
            'email': 'username1', #email not valid
        })
        assert form.is_valid() == False


    # def test_profile_update_form_valid(self, db):
    #     form = ProfileUpdateForm(data={
    #         'image': 'default.png',
    #     })
    #     assert form.is_valid() == True

    # def test_profile_update_form_not_valid(self, db):
    #     form = ProfileUpdateForm(data={
    #         'image': 123, #
    #     })
    #     assert form.is_valid() == False

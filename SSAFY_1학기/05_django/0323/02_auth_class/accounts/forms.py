from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # User기능은 전반적으로 많이 사용하므로 장고 내부에서 함수를 만들어줌
        # get_user_model()을 통해 알아서 settings.py 에 정의한 내가 쓸 User 클래스를 가져와
        # 이 부분만 변경해준다.
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
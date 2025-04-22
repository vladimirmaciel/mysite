import pytest
from django.contrib.auth import get_user_model

from mysite.manager import UserManager


def test_user_has_customize_manager_instance():
    """
    Test UserManager instance creation.
    sempre que precisar de usuario, boa pratica é criar um usuario, utiliando
    get_user_model()

    """
    User = get_user_model()
    assert isinstance(User.objects, UserManager)
    

@pytest.mark.django_db()
def test_user_creation_with_lower_case_email():
    """
    Testa se o email do usuário é salvo em letras minúsculas.
    """
    User = get_user_model()
    email = "TESTE@EMAIL.COM"
    user = User.objects.create_user(email=email)
    assert user.email == "teste@email.com"

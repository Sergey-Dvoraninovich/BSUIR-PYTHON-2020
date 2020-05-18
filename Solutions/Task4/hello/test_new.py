import pytest
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

from firstapp.models import New_Archi
from firstapp.models import New_Style
from firstapp.models import New_Building
from firstapp.models import CommentForm

@pytest.mark.django_db
@pytest.fixture
def archi_fixture():
    New_Archi.objects.create(id = 15, name="Архитектор",
                             date="30.11.2000",
                             text="good")
    archi = New_Archi.objects.get(id = 15)
    return archi

@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() ==  1

@pytest.mark.django_db
def test_model_archi_amount(archi_fixture):
  assert archi_fixture.date == "30.11.2000"

@pytest.mark.django_db
def test_model_archi_name_old():
    New_Archi.objects.create(name="Архитектор",
                             date="30.11.2000",
                             text="good")
    archi = New_Archi.objects.get(name="Архитектор")
    assert archi.name == 'Архитектор'

@pytest.mark.django_db
def test_model_style_name():
    New_Style.objects.create(name="Конструктивизм",
                             text="good")
    style = New_Style.objects.get(name="Конструктивизм")
    assert style.name == "Конструктивизм"


@pytest.mark.django_db
def test_model_building_date():
    New_Archi.objects.create(id = 15, name="Архитектор",
                             date="30.11.2000",
                             text="good")
    New_Style.objects.create(id = 15, name="Конструктивизм",
                             text="good")
    New_Building.objects.create(name="Сооружение",
                                date="30.11.2000",
                                archi_id=15,
                                style_id=15,
                                text="good")
    building = New_Building.objects.get(name="Сооружение")
    assert building.date == "30.11.2000"


def test_forms_CommentForm_field_label():
    form = CommentForm()
    assert form.fields['comment'].label == None or form.fields['comment'].label == 'comment'

def test_forms_CommentForm_field_help_text():
    form = CommentForm()
    assert form.fields['comment'].help_text == 'Введите комментарий'

def test_forms_CommentForm_no_text():
    data = ''
    form_data = {'comment': data}
    form = CommentForm(data=form_data)
    assert form.is_valid() == False

def test_forms_CommentForm_text():
    data = 'text'
    form_data = {'comment': data}
    form = CommentForm(data=form_data)
    assert form.is_valid() == True

@pytest.mark.django_db
def test_view_pagination(client):
    New_Archi.objects.create(id=15, name="Архитектор",
                             date="30.11.2000",
                             text="good")
    New_Style.objects.create(id=15, name="Конструктивизм",
                             text="good")
    New_Building.objects.create(name="Сооружение",
                                date="30.11.2000",
                                archi_id=15,
                                style_id=15,
                                text="good")
    resp = client.get(reverse('buildings'))
    assert resp.status_code == 200


@pytest.mark.parametrize('name, mail, password',
                         [('alex' , 'alex@gmail.com', 'alexpassword'),
                          ('piter' , 'piter@gmail.com', 'piterpassword'),
                          ('bob' , 'bob@gmail.com', 'bobpassword'),])
@pytest.mark.django_db
def test_user_create(name, mail, password):
  User.objects.create_user(name, mail, password)
  user = User.objects.get(email = mail)
  assert user.email ==  mail
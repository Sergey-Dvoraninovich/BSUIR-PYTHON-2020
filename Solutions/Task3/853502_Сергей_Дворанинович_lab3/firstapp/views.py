from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserForm
from .models import Person
from django.contrib.auth.decorators import login_required
from .models import Building
from .models import BuildingForm
from .models import Building_photo
from .models import Archi
from .models import User_Comment
from .models import UserProfile
from .models import UserForm
from .models import Test
from .models import New_User
from .models import New_Archi
from .models import New_Style
from .models import New_Building
from .models import new_Building_photo
from .models import New_User_Building_Comment
from .models import My_New_User_Comment
from django.views.generic import ListView
from django.views import generic
from django.contrib.auth.models import User
from .models import Test_User_Info
from .models import Test_User_Comment
from .models import CommentForm
from .models import EditCommentForm
import datetime
from django.http import HttpResponseRedirect

def base(request):
    data = {}
    if (request.user.id):
        data['user_id'] = request.user.id
        user_info = Test_User_Info.objects.get(user_id__id=request.user.id)
        data['user_photo'] = user_info.photo
    data['is_base'] = True
    return render(request, "base.html", context = data)

def comment_edit(request, request_id, comment_id):
    data = {}
    form = CommentForm()
    if (request.user.id):
        data['user_id'] = request.user.id
        user_info = Test_User_Info.objects.get(user_id__id = request.user.id)
        data['user_photo'] = user_info.photo

    if (request.user.id):
        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                new_comment = My_New_User_Comment(id = comment_id,
                                                  user_id = request.user.id,
                                                  is_edited = True,
                                                  time = datetime.datetime.now(),
                                                  building_id = request_id)
                new_comment.text = form.cleaned_data['comment']
                new_comment.save()
                s = "http://127.0.0.1:8000/building/"
                s += str(request_id) + '/'
                return HttpResponseRedirect(s)

    data['form'] = form
    return render(request, "firstapp/edit_comment.html", context=data)

def comment_delete(request, request_id, comment_id):
    comment = My_New_User_Comment.objects.get(id=comment_id)
    comment.delete()
    s = "http://127.0.0.1:8000/building/"
    s += str(request_id) + '/'
    return HttpResponseRedirect(s)

def buildings(request, request_id):
    data = {}
    form = CommentForm()
    data['ref_building_id'] = request_id

    if (request.user.id):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = My_New_User_Comment(user_id = request.user.id,
                                                  is_edited = False,
                                                  time = datetime.datetime.now(),
                                                  building_id = request_id)
                new_comment.text = form.cleaned_data['comment']
                new_comment.save()
                HttpResponseRedirect(request.path)

    if (request.user.id):
        data['user_id'] = request.user.id
        user_info = Test_User_Info.objects.get(user_id__id = request.user.id)
        data['user_photo'] = user_info.photo
    building = New_Building.objects.get(id=request_id)
    data["building"] = building
    archi = New_Archi.objects.get(id=building.archi_id)
    data["archi"] = archi
    style = New_Style.objects.get(id=building.style_id)
    data["style"] = style
    photoes = new_Building_photo.objects.filter(building_id__id=request_id)
    data["photoes"] = photoes
    comments = My_New_User_Comment.objects.filter(building_id__id=request_id)
    comments = list(comments)
    comments_data = []
    for comment in comments:
        user = User.objects.get(id = comment.user_id)
        user_info = Test_User_Info.objects.get(user_id__id = user.id)
        comments_data.append([user, user_info, comment])
    data["comments_data"] = comments_data
    data['form'] = form

    return render(request, "firstapp/building.html", context=data)

def archis(request, request_id):
    data = {}
    if (request.user.id):
        data['user_id'] = request.user.id
        user_info = Test_User_Info.objects.get(user_id__id = request.user.id)
        data['user_photo'] = user_info.photo
    archi = New_Archi.objects.get(id=request_id)
    data["archi"] = archi
    buildings = New_Building.objects.filter(archi_id__id=request_id)
    data["buildings"] = buildings

    photo_array = []
    for building in list(buildings):
        photoes = new_Building_photo.objects.filter(building_id__id=building.id)
        photo_array.append([building.id, photoes])
    data["photo_array"] = photo_array

    return render(request, "firstapp/archi.html", context=data)


def styles(request, request_id):
    data = {}
    if (request.user.id):
        data['user_id'] = request.user.id
        user_info = Test_User_Info.objects.get(user_id__id = request.user.id)
        data['user_photo'] = user_info.photo
    style = New_Style.objects.get(id=request_id)
    data["style"] = style
    buildings = New_Building.objects.filter(style_id__id=request_id)
    data["buildings"] = buildings

    photo_array = []
    for building in list(buildings):
        photoes = new_Building_photo.objects.filter(building_id__id=building.id)
        photo_array.append([building.id, photoes])
    data["photo_array"] = photo_array

    return render(request, "firstapp/style.html", context=data)

#class BuildingListView(generic.ListView):
#    model = New_Building
#    paginate_by = 8

class ArchiListView(generic.ListView):
    model = New_Archi
    paginate_by = 8

class StyleListView(generic.ListView):
    model = New_Style
    paginate_by = 8

class BuildingListView(generic.ListView):
    model = New_Building
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(BuildingListView, self).get_context_data(**kwargs)
        context['photoes'] = new_Building_photo.objects.all()
        return context







#Загрузка изображений
def index(request):
    header = "Personal Data"  # обычная переменная
    langs = ["English", "German", "French", "Spanish", "Chinese"] # массив
    user = {"name": "Tom", "age": 23}  # словарь
    addr = ("Абрикосовая", 23, 45)  # кортеж
    userform = UserForm()

    data = {"header": header, "langs": langs, "user": user, "address": addr}
    data["form"] = userform



    num_buildings = New_Building.objects.count()  # The 'all()' is implied by default.
    num_archis = New_Archi.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    data['num_books'] = num_buildings
    #data['num_instances'] = num_instances
    #data['num_instances_available'] = num_instances_available
    data['num_authors'] = num_archis
    data['num_visits'] = num_visits


    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            tom = Person(name=name, age=23)
            tom.save()
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "index.html", context=data)
def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0}  Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)
def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)
def test_main(request):
    dict = {}
    dict['num_books'] = 3
    dict['num_instances'] = 5
    dict['num_instances_available'] = 1
    dict['num_authors'] = 2
    return render(request, "firstapp/new_building_list.html", context = dict)
def cabinet(request):
  form = ProfileForm(request.POST, request.FILES or None)
  if request.method == 'POST' and form.is_valid():
    obj = UserProfile(profile_img=request.FILES['profile_img'])
    obj = form.save(commit=False)
    obj.profile_user = request.user
    obj.save()
    return redirect(reverse(cabinet))
  return render(request, 'firstapp/cabinet.html', {'form': form})
#Вывод изображений
def user_page(request):
  profile = Test.objects.all()
  photoes = new_Building_photo.objects.filter(building_id__id=1)
  return render(request, 'firstapp/user_page.html', {'profile':profile, "n": "       ", 'photoes':photoes,})
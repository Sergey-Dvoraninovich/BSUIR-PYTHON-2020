from django.test import TestCase
from firstapp.models import New_Archi
from firstapp.models import New_Style
from firstapp.models import New_Building

# Create your tests here.
class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        #"setUpTestData: Run once to set up non-modified data for all class methods."
        New_Archi.objects.create(name = "Архитектор",
                                 date = "30.11.2000",
                                 text = "good"
        )
        New_Style.objects.create(name="Конструктивизм",
                                 text="good"
        )
        New_Building.objects.create(name="Сооружение",
                                 date="30.11.2000",
                                 archi_id = 1,
                                 style_id = 1,
                                 text="good"
        )

    def setUp(self):
        #"setUp: Run once for every test method to setup clean data."
        pass

    def test_model_archi_name(self):
        archi = New_Archi.objects.get(id=1)
        self.assertEquals(archi.name, "Архитектор")

    def test_model_style_name(self):
        style = New_Style.objects.get(id=1)
        self.assertEquals(style.name, "Конструктивизм")

    def test_model_building_name(self):
        building = New_Building.objects.get(id=1)
        self.assertEquals(building.name, "Сооружение")

    def test_model_building_date(self):
        building = New_Building.objects.get(id=1)
        max_length = building._meta.get_field('date').max_length
        self.assertEquals(max_length, 30)


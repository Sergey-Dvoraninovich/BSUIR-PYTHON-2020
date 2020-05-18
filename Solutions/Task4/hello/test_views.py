from django.test import TestCase
from django.urls import reverse
from firstapp.models import New_Building
from firstapp.models import New_Archi
from firstapp.models import New_Style


class BuildingListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #New_Archi.objects.create(name="Архитектор",
        #                         date="30.11.2000",
       #                          text="good"
        #                         )
        pass

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/buildings/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('buildings'))
        self.assertEqual(resp.status_code, 200)

    def test_view_view_uses_correct_template(self):
        resp = self.client.get(reverse('buildings'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/new_building_list.html')

    def test_view_pagination_is_ten(self):
        resp = self.client.get(reverse('buildings'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == False)
        #self.assertTrue(len(resp.context['new_building_list']) == 8)
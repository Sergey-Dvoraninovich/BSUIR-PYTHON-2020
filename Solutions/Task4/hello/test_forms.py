from django.test import TestCase

# Создайте ваши тесты здесь

from firstapp.models import CommentForm


class CommentFormTest(TestCase):

    def test_forms_CommentForm_field_label(self):
        form = CommentForm()
        self.assertTrue(form.fields['comment'].label == None or form.fields['comment'].label == 'comment')

    def test_forms_CommentForm_field_help_text(self):
        form = CommentForm()
        self.assertEqual(form.fields['comment'].help_text, 'Введите комментарий')

    def test_forms_CommentForm_no_text(self):
        data = ''
        form_data = {'comment': data}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_CommentForm_text(self):
        data = 'text'
        form_data = {'comment': data}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())
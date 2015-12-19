# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from students.models import Student
from courses.models import Course

def create_student():
    student1 = Student.objects.create(
              name = 'Test',
              surname = 'StandardError',
              date_of_birth = '2015-02-18',
              email = 'ts@test.vs',
              phone = '+3809251744',
              address = 'Kiev',
              skype = 'test_students',)
    return student1

class StudentsListTest(TestCase):

    def test_students_list(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
     
    def test_student_form(self):
        self.assertEqual(Student.objects.all().count(), 0)
        student = create_student()
        self.assertEqual(Student.objects.all().count(), 1)
        
    def test_student_add(self):
        response = self.client.get('/students/add/')
        self.assertEqual(response.status_code, 200)
        
    def test_student_edit(self):
        response = self.client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 404)
        student = create_student()
        response = self.client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 200)
       
    def test_student_dell(self):
        response = self.client.get('/students/remove/1/')
        self.assertEqual(response.status_code, 404)
        student = create_student()
        response = self.client.get('/students/remove/1/')
        self.assertEqual(response.status_code, 200)
        
class StudentsDetailTest(TestCase):

    def test_students_detail(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student = create_student()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        
    def test_student_detail_template(self):
        student = create_student()
        response = self.client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')
        
    def test_student_add_template(self):
        response = self.client.get('/students/add/')
        self.assertTemplateUsed(response, 'students/student_form.html')
 
    def test_student_edit_template(self):
        student = create_student()
        response = self.client.get('/students/edit/1/')
        self.assertTemplateUsed(response, 'students/student_form.html')
        
    def test_student_dell_template(self):
        student = create_student()
        response = self.client.get('/students/remove/1/')
        self.assertTemplateUsed(response, 'students/student_confirm_delete.html')
        

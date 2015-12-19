# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from students.models import Student
from courses.models import Course

class StudentsListTest(TestCase):

    def test_students_list(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(Student.objects.all().count(), 0)
        student1 = Student.objects.create(
                  name = 'Test',
                  surname = 'StandardError',
                  date_of_birth = '2015-02-18',
                  email = 'ts@test.vs',
                  phone = '+3809251744',
                  address = 'Kiev',
                  skype = 'test_students',)
                  
        self.assertEqual(Student.objects.all().count(), 1)
                          
class StudentsDetailTest(TestCase):

    def test_students_detail(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student1 = Student.objects.create(
                  name = 'Test',
                  surname = 'StandardError',
                  date_of_birth = '2015-02-18',
                  email = 'ts@test.vs',
                  phone = '+3809251744',
                  address = 'Kiev',
                  skype = 'test_students',)
                  
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        
# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from coaches.models import Coach
from courses.models import Course
from django.contrib.auth.models import User


class CoursesListTest(TestCase):

    def test_courses_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_creating_courses(self):
        self.assertEqual(Course.objects.all().count(), 0)
        
        coach1 = Coach.objects.create(
                        user=User.objects.create(),
                        date_of_birth='2015-12-19',
                        gender='M',
                        phone='22232323333',
                        address='Kharkov',
                        skype='test_sk',
                        description = 'test description'
                    )
       
        course1 = Course.objects.create(
                        name = 'Test course',
                        short_description = 'Test course short_description',
                        description = 'Test course description',
                        coach=coach1,
                        assistant=coach1
                    )
        
        self.assertEqual(Course.objects.all().count(), 1)

    def test_course_list_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_course_list_add_course_button(self):
        response = self.client.get('/')
        self.assertContains(response, 'Добавить курс')

    def test_course_create(self):
        course1 = Course.objects.create(
                        name = 'Test course',
                        short_description = 'Test course short_description',
                        description = 'Test course description',
                    )
        self.assertEqual(Course.objects.all().count(), 1)
        
        
class CoursesDetailTest(TestCase):
    
    def test_courses_detail(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        
        coach1 = Coach.objects.create(
                        user=User.objects.create(),
                        date_of_birth='2015-12-19',
                        gender='M',
                        phone='22232323333',
                        address='Kharkov',
                        skype='test_sk',
                        description = 'test description'
                    )
       
        course1 = Course.objects.create(
                        name = 'Test course',
                        short_description = 'Test course short_description',
                        description = 'Test course description',
                        coach=coach1,
                        assistant=coach1
                    )
        
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        
        
        
# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from coaches.models import Coach
from courses.models import Course
from django.contrib.auth.models import User

def create_course():
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
                assistant=coach1,
            )
    return course1


class CoursesListTest(TestCase):

    def test_courses_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_creating_courses(self):
        self.assertEqual(Course.objects.all().count(), 0)
        self.course1 = create_course()
        self.assertEqual(Course.objects.all().count(), 1)

    def test_course_list_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_course_list_add_course_button(self):
        response = self.client.get('/')
        self.assertContains(response, 'Добавить курс')

    def test_course_create(self):
        self.course1 = create_course()
        self.assertEqual(Course.objects.all().count(), 1)
        
        
class CoursesDetailTest(TestCase):
    
    def test_course_detail_404(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        
    def test_courses_detail(self):
        self.course1 = create_course()
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        
    def test_course_detail_template(self):
        self.course1 = create_course()
        response = self.client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')
        
    def test_add_template(self):	
        response = self.client.get('/courses/add/')
        self.assertTemplateUsed(response, 'courses/add.html')
        
    def test_remove_template(self):	
        self.course1 = create_course()
        response = self.client.get('/courses/remove/1/')
        self.assertTemplateUsed(response, 'courses/remove.html')

        
        
# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from students.models import Student
from courses.models import Course

import logging
logger = logging.getLogger('testing') 

class StudentsListTest(TestCase):

    def test_students_list(self):
        client = Client()
        response = client.get('/students/')
#        logger.debug(response)
        self.assertEqual(response.status_code, 200)
        
        response = client.get('/students/101/')
        #self.assertEqual(response.status_code, 401)
        student1 = Student.objects.create(
                  name = 'Test',
                  surname = 'StandardError',
                  date_of_birth = '2015-02-18',
                  email = 'ts@test.vs',
                  phone = '+3809251744',
                  address = 'Kiev',
                  skype = 'test_students',)
                  
        self.assertEqual(response.status_code, 200)
                          
                          
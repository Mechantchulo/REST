""" from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title = '1st Todo', body = 'This is the first todo')
        
    def test_title_content(self):
        todo = Todo.objects.get(id = 1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, '1st Todo')
        
    def test_body_content(self):
        todo = Todo.objects.get(id = 1)
        expected_object_name = f'{todo.body}'
        self.assertEqual(expected_object_name, 'This is the first todo')
        
    
class TodoModelTest2(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title = 'HTTP', body = 'HTTP todo')
            
    def test_title_content(self):
        todo = Todo.objects.get(id = 1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'HTTP')
        
    def test_body_content(self):
        todo = Todo.objects.get(id = 1)
        expected_object_name = f'{todo.body}'
        self.assertEqual(expected_object_name, 'HTTP todo')
        
    
    
class TodoModelTest3(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title = 'Third item', body = 'Third item to learn')   
    def test_title_content(self):
        todo = Todo.objects.get(id = 1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'Third item')
        
    def test_body_content(self):
        todo = Todo.objects.get(id = 1)
        expected_object_name = f'{todo.body}'
        self.assertEqual(expected_object_name, 'Third item to learn')
         
    
        
        
        

 """
 
 #optimized code
from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo1 = Todo.objects.create(title='1st Todo', body='This is the first todo')
        cls.todo2 = Todo.objects.create(title='HTTP', body='HTTP todo')
        cls.todo3 = Todo.objects.create(title='Third item', body='Third item to learn')
    
    def test_title_content_todo1(self):
        self.assertEqual(self.todo1.title, '1st Todo')
    
    def test_body_content_todo1(self):
        self.assertEqual(self.todo1.body, 'This is the first todo')
    
    def test_title_content_todo2(self):
        self.assertEqual(self.todo2.title, 'HTTP')
    
    def test_body_content_todo2(self):
        self.assertEqual(self.todo2.body, 'HTTP todo')
    
    def test_title_content_todo3(self):
        self.assertEqual(self.todo3.title, 'Third item')
    
    def test_body_content_todo3(self):
        self.assertEqual(self.todo3.body, 'Third item to learn')

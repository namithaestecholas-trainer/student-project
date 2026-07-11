from django.test import TestCase
from django.urls import reverse
from .models import Department, Student

class StudentDepartmentTest(TestCase):
    def setUp(self):
        self.dept = Department.objects.create(name="Computer Science")
        self.student = Student.objects.create(
            name="John Doe",
            age=20,
            email="john@example.com",
            department=self.dept
        )

    def test_department_list(self):
        response = self.client.get(reverse("department_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Computer Science")

    def test_department_create(self):
        response = self.client.post(reverse("department_create"), {"name": "Mathematics"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Department.objects.filter(name="Mathematics").exists())

    def test_department_update(self):
        response = self.client.post(
            reverse("department_update", args=[self.dept.id]),
            {"name": "CS & Engineering"}
        )
        self.assertEqual(response.status_code, 302)
        self.dept.refresh_from_db()
        self.assertEqual(self.dept.name, "CS & Engineering")

    def test_student_list(self):
        response = self.client.get(reverse("student_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")

    def test_student_create(self):
        response = self.client.post(reverse("student_create"), {
            "name": "Jane Doe",
            "age": 22,
            "email": "jane@example.com",
            "department": self.dept.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(name="Jane Doe").exists())

    def test_student_update(self):
        response = self.client.post(reverse("student_update", args=[self.student.id]), {
            "name": "Johnathan Doe",
            "age": 21,
            "email": "johnathan@example.com",
            "department": self.dept.id
        })
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, "Johnathan Doe")
        self.assertEqual(self.student.age, 21)


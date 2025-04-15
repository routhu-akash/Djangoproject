from django.db import models

class BookRecord(models.Model):
    student_name = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.student_name} - {self.book_name}"


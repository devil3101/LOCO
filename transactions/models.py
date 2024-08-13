from django.db import models

class Transaction(models.Model):
    amount = models.FloatField()
    type = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction {self.id} - {self.type} - {self.amount}"

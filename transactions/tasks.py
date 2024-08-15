
from celery import shared_task
from .models import Transaction

@shared_task
def calculate_sum_task(transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    
    def recursive_sum(transaction):
        total = transaction.amount
        for child in transaction.children.all():
            total += recursive_sum(child)
        return total
    
    return recursive_sum(transaction)

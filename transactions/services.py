from .models import Transaction
from django.db import transaction as db_transaction
from .tasks import calculate_sum_task

class TransactionService:

    @staticmethod
    def create_transaction(data):
        with db_transaction.atomic():
            new_transaction = Transaction.objects.create(**data)
            return new_transaction

    @staticmethod
    def get_transaction(transaction_id):
        return Transaction.objects.get(id=transaction_id)

    @staticmethod
    def get_transactions_by_type(transaction_type):
        return Transaction.objects.filter(type=transaction_type)

    @staticmethod
    def calculate_transaction_sum(transaction_id):
        transaction = Transaction.objects.get(id=transaction_id)
        total_sum = calculate_sum_task.delay(transaction.id).get(timeout=10)
        return total_sum

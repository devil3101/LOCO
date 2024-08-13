from django.test import TestCase
from rest_framework.test import APIClient
from .models import Transaction

class TransactionTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.transaction = Transaction.objects.create(amount=5000, type='cars')

    def test_create_transaction(self):
        response = self.client.put(f'/transactionservice/transaction/{self.transaction.id}', {
            'amount': 10000,
            'type': 'shopping',
            'parent': self.transaction.id
        }, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_transaction(self):
        response = self.client.get(f'/transactionservice/transaction/{self.transaction.id}')
        self.assertEqual(response.status_code, 200)

    def test_get_transactions_by_type(self):
        response = self.client.get('/transactionservice/types/cars')
        self.assertEqual(response.status_code, 200)

    def test_calculate_transaction_sum(self):
        response = self.client.get(f'/transactionservice/sum/{self.transaction.id}')
        self.assertEqual(response.status_code, 200)

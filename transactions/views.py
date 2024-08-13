from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import TransactionService
from .serializers import TransactionSerializer
from django.http import JsonResponse
from .models import Transaction

class TransactionView(APIView):
    
    def put(self, request, transaction_id):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            TransactionService.create_transaction(serializer.validated_data)
            return Response({"status": "ok"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, transaction_id):
        try:
            transaction = TransactionService.get_transaction(transaction_id)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)


class TransactionTypeView(APIView):
    
    def get(self, request, type_):
        transactions = TransactionService.get_transactions_by_type(type_)
        transaction_ids = [transaction.id for transaction in transactions]
        return JsonResponse(transaction_ids, safe=False)


class TransactionSumView(APIView):

    def get(self, request, transaction_id):
        try:
            total_sum = TransactionService.calculate_transaction_sum(transaction_id)
            return Response({"sum": total_sum})
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

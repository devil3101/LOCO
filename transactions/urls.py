from django.urls import path
from .views import TransactionView, TransactionTypeView, TransactionSumView

urlpatterns = [
    path('transaction/<int:transaction_id>', TransactionView.as_view()),
    path('types/<str:type_>', TransactionTypeView.as_view()),
    path('sum/<int:transaction_id>', TransactionSumView.as_view()),
]

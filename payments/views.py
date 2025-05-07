from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment, ServiceType
from .forms import PaymentForm
from rest_framework import viewsets
from .serializers import PaymentSerializer, ServiceTypeSerializer

from analytics.utils import log_user_action



class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'payments/payment_list.html', {'payments': payments})

@login_required
def payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.status = 'pending'
            payment.save()

            # логирование действия
            log_user_action(
                request,
                action="Создание оплаты",
                metadata={
                    "payment_id": payment.id,
                    "amount": str(payment.amount),
                    "status": payment.status
                }
            )

            return redirect('payments:payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payments/payment_form.html', {'form': form})
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Calculation

def calculator(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            result = 0

        # Save the calculation to the database
        Calculation.objects.create(num1=num1, num2=num2, operation=operation, result=result)

        # Pass the result to the template for display
        return render(request, 'index.html', {'result': result})
    else:
        return render(request, 'index.html')


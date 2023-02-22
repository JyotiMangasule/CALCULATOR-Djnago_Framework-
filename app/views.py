from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Calculations




def calculator(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operation = request.POST.get('operation')

        if not (num1.isnumeric() and num2.isnumeric()):
            message = "Please enter valid numbers."
            return render(request, 'index.html', {'message': message})

        num1 = float(num1)
        num2 = float(num2)

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            
            result = num1 - num2
        elif operation == 'multiply':
            if num2 == 0 or num1==0:
                message = "Result is 0."
                return render(request, 'index.html', {'message': message})
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0 :
                message = "Cannot divide by zero."
                return render(request, 'index.html', {'message': message})
            result = num1 / num2
        else:
        
            message = "0";
            return render(request, 'index.html', {'message': message})
        # Save the calculation to the database
        Calculations.objects.create(num1=num1, num2=num2, operation=operation, result=result)

        # Pass the result to the template for display
        return render(request, 'index.html', {'result': result})
    else:
        return render(request, 'index.html')

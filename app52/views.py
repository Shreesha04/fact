from django.shortcuts import render
from django.http import HttpResponse
import math

def factorial_view(request):
    if request.method == "POST":
        try:
            number = int(request.POST.get('number'))
            if 1 <= number <= 10:
                result = math.factorial(number)
                return render(request, 'app52/index.html', {'result': result, 'number': number})
            else:
                error = "Please enter a number between 1 and 10."
                return render(request, 'app52/index.html', {'error': error})
        except ValueError:
            error = "Invalid input. Please enter a number between 1 and 10."
            return render(request, 'app52/index.html', {'error': error})
    return render(request, 'app52/index.html')

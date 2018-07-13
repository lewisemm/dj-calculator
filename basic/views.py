from django.shortcuts import render, redirect

from basic import forms


# Create your views here.
def basic_operations(request):

    form = forms.BasicForm()
    context = {
        'basic_form': form
    }

    if request.method == 'POST':
        form = forms.BasicForm(request.POST)
        answer = None

        if form.is_valid():
            value1 = form.cleaned_data['value1']
            operation = form.cleaned_data['operation']
            value2 = form.cleaned_data['value2']

            if operation == '+':
                answer = value1 + value2
            elif operation == '-':
                answer = value1 - value2
            elif operation == '*':
                answer = value1 * value2
            elif operation == '/':
                if value2 == 0:
                    answer = "Division by Zero is not possible!"
                else:
                    answer = value1 / value2

        context['answer'] = answer
        context['basic_form'] = form

    return render(request, 'basic.html', context=context)

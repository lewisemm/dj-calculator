from django import forms


class BasicForm(forms.Form):

    operations = (
        ('+', 'ADD'),
        ('-', 'SUBTRACT'),
        ('*', 'MULTIPLY'),
        ('/', 'DIVIDE'),
    )
    value1 = forms.IntegerField(required=True)
    operation = forms.ChoiceField(required=True, choices=operations)
    value2 = forms.IntegerField(required=True)

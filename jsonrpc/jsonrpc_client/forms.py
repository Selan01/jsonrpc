from django import forms

class JsonRpcForm(forms.Form):
    method = forms.CharField(initial='auth.check', widget=forms.TextInput, label='Метод', help_text='Метод JSON-RPC для вызова.')
    params = forms.CharField(required=False, widget=forms.Textarea, label='Параметры', help_text='Введите параметры в формате JSON.')

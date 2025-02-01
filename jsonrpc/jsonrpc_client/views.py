from django.views.generic.edit import FormView
from .forms import JsonRpcForm
from .jsonrpc_service.jsonrpc_service import JsonRpcClient
import json

class JsonRpcFormView(FormView):
    template_name = 'jsonrpc_client/index.html'
    form_class = JsonRpcForm
    success_url = '/'

    def form_valid(self, form):
        method = form.cleaned_data['method']
        params = form.cleaned_data['params']

        try:
            params = json.loads(params) if params else {}
        except ValueError:
            params = {}

        client = JsonRpcClient(host='slb.medv.ru')
        response_data = client.call_method(method, params)

        if 'error' not in response_data:
            response_data = {'status': 'Авторизация прошла успешно'}
        else:
            response_data = {'status': 'Попытка авторизации не удалась'}


        return self.render_to_response(self.get_context_data(form=form, response=response_data))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

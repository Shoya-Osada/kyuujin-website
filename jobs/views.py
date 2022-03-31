from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'jobs/index.html' #TemplateViewを使用して、固定ページを作成。
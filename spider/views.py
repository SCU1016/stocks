__author__ = 'joeyzhao'

from django.http import HttpResponse
from django.template import RequestContext, Context, loader

from spider.models import StockDB

def index(request):
    t = loader.get_template('index.html')
    r = []
    # items = StockDB.objects.filter(name='hukexin')
    # for item in items:
    #     r.append(item.name)
    #     r.append(item.sex)
    #     r.append(item.age)

    c = Context({'data': r})
    return HttpResponse(t.render(c))
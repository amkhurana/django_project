from django.template.defaulttags import register
from django import template
from core.models import Order


register = template.Library()
# @register.filter
# def get_item(dictionary, key):
#     return dictionary.get(key)


# @register.filter(name='lookup')
# def lookup(value, arg):
#     return value.get(arg)

@register.filter
def lookup(list, key):
    d = dict(list)
    return d[key]


@register.filter
def tuplelookup(key, list):
    return list['key']


@register.filter
def item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0

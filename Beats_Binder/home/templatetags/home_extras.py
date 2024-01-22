from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def concatenate(str1, str2):
    return str(str1) + str(str2)

@register.filter
def returnHomeButton(name, text):
    return "<button type='submit' name='" + str(name) +"'>"+str(text)+"</button>"

@register.filter
def returnLink(url,text):
    return "<a href='" + url + "'>" + text + "</a>"
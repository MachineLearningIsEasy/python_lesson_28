from django import template

register = template.Library()


def my_upper(string):
    return string.upper()


def my_delete(string):

    return ''.join([string[i] if i%2 else '' for i in range(len(string))])

register.filter('my_upper', my_upper)
register.filter('my_delete', my_delete)
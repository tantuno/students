from ipware.ip import get_real_ip, get_ip
from django.template import  RequestContext
from django.contrib.gis.geoip import GeoIP
from django import template

register = template.Library()
@register.simple_tag
def current_location(request):
    ip = get_real_ip(request)
    g = GeoIP()
    if ip is not None:
       location = g.city(ip)
       return  str(location['city'])+', '+str(location['country_name'])
    else:
        return ''

from django.shortcuts import render
from django.conf import settings


def vis_main(request):
    template_info = dict()
    template_info["center_ip_address"] = getattr(settings, 'CENTER_IP_ADDRESS')
    template_info["center_port"] = getattr(settings, 'CENTER_PORT')
    return render(request, 'vis/layout.html', template_info)

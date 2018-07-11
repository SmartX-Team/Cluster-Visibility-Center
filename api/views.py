from influxdb import InfluxDBClient
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render
from .models import API
from django.conf import settings

client = InfluxDBClient('127.0.0.1', 8086, 'root', 'root', 'onk')

def api_main(request):
    template_info = dict()

    qs = API.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)

    template_info['api_list'] = qs
    template_info['q'] = q

    template_info["center_ip_address"] = getattr(settings, 'CENTER_IP_ADDRESS')
    template_info["center_port"] = getattr(settings, 'CENTER_PORT')

    return render(request, 'api/layout.html', template_info)


def test_api(request):
    data = [{
        'id': 'id 1',
        'title': 'title 1',
        'content': 'content 1',
    }]
    return JsonResponse(data, safe=False)


def total_record(request):
    rs = client.query("SELECT * FROM tcp4connect;")
    return JsonResponse(rs.raw, safe=False)


def country_code_stat(request):
    rs = client.query("SELECT * FROM tcp4connect GROUP BY COUNTRY;")
    return JsonResponse(rs.raw, safe=False)


def country_code_count(request, code):
    rs = client.query("SELECT * FROM tcp4connect WHERE COUNTRY='{}' \
    GROUP BY COUNTRY;".format(code))
    return JsonResponse(rs.raw, safe=False)


def comm_stat(request):
    rs = client.query("SELECT * FROM tcp4connect GROUP BY comm;")
    return JsonResponse(rs.raw, safe=False)


def comm_count(request, comm):
    rs = client.query("SELECT * FROM tcp4connect WHERE comm='{}' \
    GROUP BY comm;".format(comm))
    return JsonResponse(rs.raw, safe=False)


def dest_ip_stat(request):
    rs = client.query("SELECT * FROM tcp4connect GROUP BY destination_addr")
    return JsonResponse(rs.raw, safe=False)


def dest_ip_count(request, dest):
    rs = client.query("SELECT * FROM tcp4connect WHERE destination_addr='{}' \
    GROUP BY destination_addr".format(dest))
    return JsonResponse(rs.raw, safe=False)


def source_ip_stat(request):
    rs = client.query("SELECT * FROM tcp4connect GROUP BY source_addr")
    return JsonResponse(rs.raw, safe=False)


def source_ip_count(request, dest):
    rs = client.query("SELECT * FROM tcp4connect WHERE source_addr='{}' \
    GROUP BY destination_addr".format(dest))
    return JsonResponse(rs.raw, safe=False)


def onosbuild2017(request):
    rs = client.query("SELECT count(*) FROM onosbuild2017 GROUP BY source_addr")
    return_list = []
    for i, j in zip(rs.items(), list(rs)):
        temp_dict = {}
        addr = i[0][1]['source_addr']
        cnt = j[0]['count_PID']
        temp_dict["source_address"] = addr
        temp_dict["number_of_packet"] = cnt
        return_list.append(temp_dict)

    return JsonResponse(return_list, safe=False)

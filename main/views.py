from django.shortcuts import render
import requests
import json

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics" #https://rapidapi.com/api-sports/api/covid-193(Refered for Covid Statistics)

    c=request.POST.get('name')

    querystring = {"country":c}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "333b2d51ecmshceaedc6351185bfp1fbb4ejsn7ef0b372a76f"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data=response['response']
    d=data[0]
    print(d)
    context={
        'all':d['cases']['total'],
        'recovered':d['cases']['recovered'],
        'deaths':d['deaths']['total'],
        'new_deaths':d['deaths']['new'],
        'new_cases':d['cases']['new'],
        'active':d['cases']['active'],
        'day':d['day'],'critical':d['cases']['critical'],
        'country':d['country']

    }
    return render(request,'index.html',context)
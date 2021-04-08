from django.shortcuts import render, HttpResponse
import requests
import json




url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
mrl = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
headers = {
    'x-rapidapi-key': "9ddf9b769amshcfc55625c370898p172945jsn1a55d1e83b6d",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)
# Create your views here.   
def index(request):
    mylist=[]

    for x in range(0,220):
        mylist.append(response['countries_stat'][x]['country_name'])
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        for x in range(0,220):
            if selectedcountry==response['countries_stat'][x]['country_name']:
                cases = response['countries_stat'][x]['cases']
                deaths = response['countries_stat'][x]['deaths']
                total_recovered = response['countries_stat'][x]['total_recovered']
                new_deaths = response['countries_stat'][x]['new_deaths']
                new_cases = response['countries_stat'][x]['new_cases']
                active_cases = response['countries_stat'][x]['active_cases']
        if selectedcountry  == "Select Country":
            cases = ""
            deaths =""
            total_recovered = ""
            new_deaths = ""
            new_cases = ""
            active_cases = ""
            selectedcountry = "Please Select Country First."       
        context ={'selectedcountry':selectedcountry,'mylist':mylist,'cases': cases, 'deaths': deaths,'total_recovered':total_recovered,'new_deaths':new_deaths,'new_cases':new_cases,'active_cases':active_cases}
        return render(request, 'index.html',context)
    mylist=[]
    for x in range(0,220):
        mylist.append(response['countries_stat'][x]['country_name'])
        
    # print(response.text)
    context ={'mylist':mylist}

    # return HttpResponse("this is home page")
    return render(request, 'index.html',context)
def home(request):
    mylist1 =[]
    response = requests.request("GET", mrl, headers=headers).json()
    for x in response['state_wise']:
        mylist1.append(x)
    if request.method=="POST":
        selectedstate = request.POST['selectedstate']
        for x in response['state_wise']:
            if selectedstate == x:
                active = response['state_wise'][selectedstate]['active']
                confirmed = response['state_wise'][selectedstate]['confirmed']
                deaths = response['state_wise'][selectedstate]['deaths']
                recovered = response['state_wise'][selectedstate]['recovered']
                todayrecovered = response['state_wise'][selectedstate]['deltarecovered']
                todaydeaths = response['state_wise'][selectedstate]['deltadeaths']
        if selectedstate =="Select State":
            active = ''
            confirmed = ''
            deaths = ''
            recovered = ''
            todayrecovered = ''
            todaydeaths = ''
            selectedstate = 'Please Select State First.'
        cont = {'selectedstate':selectedstate,'mylist1':mylist1,'active':active,'confirmed':confirmed,'deaths':deaths,'recovered':recovered,'todayrecovered':todayrecovered,'todaydeaths':todaydeaths}
        
        return render(request, 'home.html',cont)
                

        # print(selectedstate) 
    

    for x in response['state_wise']:
        mylist1.append(x)
    cont = {'mylist1':mylist1}    
        
 

    return render(request, 'home.html',cont)
def city(request):
    mylist=[]
    mylist = list(set(mylist))
    response = requests.request("GET", mrl, headers=headers).json()
    for x in response['state_wise']:
        if int(response['state_wise'][x]['active']) != 0 :
            for city in response['state_wise'][x]['district']:
                mylist.append(city)
    contd = {'mylist':sorted(list(set(mylist)))}
    if request.method=="POST":
        selectedcity = request.POST['selectedcity']
        
        for x in response['state_wise']:
            if int(response['state_wise'][x]['active']) != 0 :
                for city in response['state_wise'][x]['district']:
                    if selectedcity == city:
                        active = response['state_wise'][x]['district'][city]['active']
                        confirmed = response['state_wise'][x]['district'][city]['confirmed']
                        deceased = response['state_wise'][x]['district'][city]['deceased']
                        recovered = response['state_wise'][x]['district'][city]['recovered']
        if selectedcity =="Select City":
            active = ''
            confirmed = ''
            deceased = ''
            recovered = ''
            selectedcity = "Please Select City First."
        contd = {'selectedcity':selectedcity,'mylist':sorted(mylist),'active':active,'confirmed':confirmed,'deceased':deceased,'recovered':recovered}
        return render(request, 'city.html',contd)
    for x in response['state_wise']:
        if int(response['state_wise'][x]['active']) != 0 :
            for city in response['state_wise'][x]['district']:
                mylist.append(city)
    contd = {'mylist':sorted(list(set(mylist)))}
  
    return render(request, 'city.html',contd)
def totals(request):
    url = "https://api.covid19india.org/data.json"
    response = requests.request("GET", url, headers=headers).json()
    osf = f'''{int(response["tested"][-2]['over60years1stdose']):,}'''
    oss = f'''{int(response["tested"][-2]['over60years2nddose']):,}'''
    srt = f'''{int(response["tested"][-2]['samplereportedtoday']):,}'''
    tst = f'''{int(response["tested"][-2]['totalsamplestested']):,}'''
    tiv = f'''{int(response["tested"][-2]['totalindividualsvaccinated']):,}'''
    drsa = f'''{int(response["tested"][-2]['dailyrtpcrsamplescollectedicmrapplication']):,}'''
    contd ={'TFV':osf,'TMV':oss,'SRT':srt,'FDA':tiv,'TST':tst,'SDA':drsa}
    return render(request,'total.html',contd)
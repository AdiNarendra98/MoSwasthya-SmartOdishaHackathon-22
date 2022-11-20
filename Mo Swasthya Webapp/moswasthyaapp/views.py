from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from django.http import HttpResponse, request,FileResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import os
import pymongo
from PIL import Image
import gridfs
from bson.objectid import ObjectId
import base64
from geopy.distance import geodesic
import pandas as pd
import bson.json_util as json_util
import time
import requests
# Create your views here.

imgpath="static/img/Rectangle 841.png"
def conn():
    connection_url='MongoDb Database connection_url'
    client = pymongo.MongoClient(connection_url) 
    db = client.myFirstDatabase.card_hosp
    hospitals = db.find()
    return hospitals

def landing(request):
    hospitals = conn()
    hospitall=list(hospitals)
    print(hospitall)
    df = pd.DataFrame(hospitall)
    setshospitallist=df.to_dict('records')
    errormsg= "Please Enable your location for better result"
    context={
        'setshospitallist':setshospitallist,
        'errormsg':errormsg
        }
    return render(request, "index.html",context=context)

def getaddress(latlong):
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={}&key=Maps_api_key'.format(latlong))
    resp_json_payload = response.json()
    # print(resp_json_payload['results'][0])
    address=resp_json_payload['results'][0]['formatted_address']
    return(address)

def getlatlong(address):
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key=Maps_api_key'.format(address))
    resp_json_payload = response.json()
    # print(resp_json_payload)
    lat=resp_json_payload['results'][0]['geometry']['location']['lat']
    lng=resp_json_payload['results'][0]['geometry']['location']['lng']
    latlong=str(lat)+','+str(lng)
    return(latlong)

def landinghosp(request,loc):
    hospitals = conn()
    hospitall=list(hospitals)
    print(hospitall)
    df = pd.DataFrame(hospitall)
    if request.method == 'POST':   
        if 'Location' in request.POST:
            Location = request.POST['Location']
            print(Location)
            latlong=getlatlong(Location)
            setshospitallist=getsearchdistance(df,latlong)
            print("locatentry: --",setshospitallist)
            context={
            'setshospitallist':setshospitallist,
            # 'locs':locs,
            'address':Location,
            }
            return render(request, "index.html",context=context)
    address=getaddress(loc)
    loc=str(loc)
    print(loc)
    setshospitallist=getlanddistance(df,loc)
    print(setshospitallist)
    context={
            'setshospitallist':setshospitallist,
            # 'loc':loc,
            'address':address,
        }
    return render(request, "index.html",context=context)


def getsearchdistance(df,myloc):
    ldist=[]
    ddf=df['location']
    for i in ddf:
        latlong=i['coordinates']
        lat=latlong[1]
        long=latlong[0]
        reqloc=str(lat)+','+str(long)
        dist="{:.2f}".format(geodesic(myloc, reqloc).km)
        kdist=float(dist)
        # print(kdist)
        ldist.append(kdist)
    df['distance']=ldist
    df["id"]=df["_id"]
    sdf=df.sort_values('distance',ascending=True)
    hospitallist=sdf.to_dict('records')
    # print(sdf)
    # hospitallist=json_util.dumps(hospitallist)
    # hospitallist='hospitallist'
    return hospitallist

def getlanddistance(df,myloc):
    ldist=[]
    # hospitals = conn()
    # hospitall=list(hospitals)
    # # print(hospitall)
    # df = pd.DataFrame(hospitall)
    ddf=df[['location', 'hospital_name']].copy()
    for i in range(len(ddf)):
        latlong=ddf['location'][i]['coordinates']
    # for i in ddf['location']:
    #     latlong=i['coordinates']
        lat=latlong[1]
        long=latlong[0]
        reqloc=str(lat)+','+str(long)
        dist="{:.2f}".format(geodesic(myloc, reqloc).km)
        kdist=float(dist)
        # print(kdist)
        ldist.append(kdist)
    df['distance']=ldist
    df["id"]=df["_id"]
    sdf=df.sort_values('distance',ascending=True)
    sdf=sdf.head(15)
    hospitallist=sdf.to_dict('records')
    # print(sdf)
    # hospitallist=json_util.dumps(hospitallist)
    # hospitallist='hospitallist'
    return hospitallist


def detailsection(request,id):
    hospitals = conn()
    hospitall=list(hospitals)
    print(hospitall)
    df = pd.DataFrame(hospitall)
    df=df.fillna('nan')
    df["id"]=df["_id"]
    print(id)
    objInstance = ObjectId(id)
    sdf=df.loc[df["id"]==objInstance]
    setshospitallist=sdf.to_dict('records')
    print(setshospitallist)
    return render(request, "details.html",{"setshospitallist":setshospitallist})

def showdefault(request):
    img=imgpath
    imgo=open(img,'rb')
 
    return FileResponse(imgo)

def show(request,img):
    connection_url='MongoDb Database connection_url'
    client = pymongo.MongoClient(connection_url) 
    db = client.myFirstDatabase
    fs = gridfs.GridFS(db)
    image = fs.get_last_version(filename=simg)
    
    return FileResponse(image)
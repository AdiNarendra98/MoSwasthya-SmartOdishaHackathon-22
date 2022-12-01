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
import numpy as np
import pickle
import sklearn

# Create your views here.

imgpath="static/img/Rectangle 841.png"
def conn():
    connection_url='Mongodb Api'
    client = pymongo.MongoClient(connection_url) 
    db = client.myFirstDatabase.card_hosp_en
    hospitals = db.find()
    return hospitals

def odiaconn():
    connection_url='Api Key'
    client = pymongo.MongoClient(connection_url) 
    db = client.myFirstDatabase.card_hosp_od
    hospitals = db.find()
    return hospitals

def bsky(request):
    return render(request, "bsky.html")
def bskyodia(request):
    return render(request, "bskyodia.html")
def ostf(request):
    return render(request, "ostf.html")
def ostfodia(request):
    return render(request, "ostfodia.html")
def niramaya(request):
    return render(request, "niramaya.html")
def niramayaodia(request):
    return render(request, "niramayaodia.html")
def prediction(request):
    loaded_model = pickle.load(open('moswasthyaapp\model\model_lr_final.pkl',"rb"))
    features = np.array([[24.2,3,2,3,0.0,0.0,2,3,10,7,2,3,2,8.0,3,3,2]])
    pred = loaded_model.predict(features)
    print(pred)
    return render(request, "prediction.html",{'pred':pred})
def predictionodia(request):
    return render(request, "predictionodia.html")
def scheme(request):
    return render(request, "scheme.html")
def schemeodia(request):
    return render(request, "schemeodia.html")
def tableu(request):
    return render(request, "tableu.html")
def tableuodia(request):
    return render(request, "tableuodia.html")
def landingodia(request):
    errormsg= "ଡାକ୍ତରଖାନା ତାଲିକା ଦେଖିବାକୁ ଦୟାକରି ଆପଣଙ୍କର ଅବସ୍ଥାନ ସକ୍ଷମ କରନ୍ତୁ |"
    context={
        # 'setshospitallist':setshospitallist,
        'errormsg':errormsg
        }
    return render(request, "indexodia.html",context=context)


def pred_disease(request):
    if request.method == 'POST':
        BMi = request.POST['BMI']
        Smoking = request.POST['Smoking']
        Alcohol_Drinking = request.POST['Alcohol_Drinking']
        Stroke = request.POST['Stroke']
        Physical_Health = request.POST['Physical_Health']
        Mental_Health = request.POST['Mental_Health']
        DiffWalking = request.POST['DiffWalking']
        Sex = request.POST['Sex']
        AgeCategory = request.POST['AgeCategory']
        # Race = request.POST['Race']
        Diabetic = request.POST['Diabetic']
        PhysicalActivity = request.POST['PhysicalActivity']
        GenHealth = request.POST['GenHealth']
        SleepTime = request.POST['SleepTime']
        Asthma = request.POST['Asthma']
        KidneyDisease = request.POST['KidneyDisease']
        SkinCancer = request.POST['SkinCancer']
        
        # text=BMi,Smoking,Alcohol_Drinking,Stroke,Physical_Health,Mental_Health,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma,KidneyDisease,SkinCancer
        # print(text)
        
        loaded_model = pickle.load(open('moswasthyaapp\model\model.pkl',"rb"))
        features = np.array([[int(BMi),int(Smoking),int(Alcohol_Drinking),int(Stroke),int(Physical_Health),int(Mental_Health),int(DiffWalking),int(Sex),int(AgeCategory),int(Diabetic),int(PhysicalActivity),int(GenHealth),int(SleepTime),int(Asthma),int(KidneyDisease),int(SkinCancer)]])
        print(features)
        pred = loaded_model.predict(features)
        pred=str(pred[0])
        if pred=='1':
            out="You may be at risk of developing heart disease. "
        else:
            out="You are not at risk of developing heart disease."
            
        print(pred[0])
        return render(request, "prediction.html",{'out':out})
    return render(request, "prediction.html")



def pred_disease_odia(request):
    if request.method == 'POST':
        BMi = request.POST['BMI']
        Smoking = request.POST['Smoking']
        Alcohol_Drinking = request.POST['Alcohol_Drinking']
        Stroke = request.POST['Stroke']
        Physical_Health = request.POST['Physical_Health']
        Mental_Health = request.POST['Mental_Health']
        DiffWalking = request.POST['DiffWalking']
        Sex = request.POST['Sex']
        AgeCategory = request.POST['AgeCategory']
        # Race = request.POST['Race']
        Diabetic = request.POST['Diabetic']
        PhysicalActivity = request.POST['PhysicalActivity']
        GenHealth = request.POST['GenHealth']
        SleepTime = request.POST['SleepTime']
        Asthma = request.POST['Asthma']
        KidneyDisease = request.POST['KidneyDisease']
        SkinCancer = request.POST['SkinCancer']
        
        # text=BMi,Smoking,Alcohol_Drinking,Stroke,Physical_Health,Mental_Health,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma,KidneyDisease,SkinCancer
        # print(text)
        
        loaded_model = pickle.load(open('moswasthyaapp\model\model.pkl',"rb"))
        features = np.array([[int(BMi),int(Smoking),int(Alcohol_Drinking),int(Stroke),int(Physical_Health),int(Mental_Health),int(DiffWalking),int(Sex),int(AgeCategory),int(Diabetic),int(PhysicalActivity),int(GenHealth),int(SleepTime),int(Asthma),int(KidneyDisease),int(SkinCancer)]])
        print(features)
        pred = loaded_model.predict(features)
        pred=str(pred[0])
        if pred=='1':
            out="ଆପଣଙ୍କର ହୃଦରୋଗ ହେବାର ଆଶଙ୍କା ଥାଇପାରେ | "
        else:
            out="ଆପଣଙ୍କର ହୃଦରୋଗ ହେବାର ଆଶଙ୍କା ନାହିଁ |"
            
        print(pred[0])
        return render(request, "predictionodia.html",{'out':out})
    return render(request, "predictionodia.html")

def landing(request):
    # hospitals = conn()
    # hospitall=list(hospitals)
    # print(hospitall)
    # df = pd.DataFrame(hospitall)
    # setshospitallist=df.to_dict('records')
    errormsg= "Please Enable your location to see Hospital list"
    context={
        # 'setshospitallist':setshospitallist,
        'errormsg':errormsg
        }
    return render(request, "index.html",context=context)

def getaddress(latlong):
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={}&key=Key'.format(latlong))
    resp_json_payload = response.json()
    # print(resp_json_payload['results'][0])
    address=resp_json_payload['results'][0]['formatted_address']
    return(address)

def getlatlong(address):
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key=Key'.format(address))
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


def landinghospodia(request,loc):
    hospitals = odiaconn()
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
            return render(request, "indexodia.html",context=context)
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
    return render(request, "indexodia.html",context=context)


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
    # df = pd.read_csv('moswasthyaapp\card_hosp_list.csv')
    df=df.fillna('nan')
    df["id"]=df["_id"]
    print(id)
    objInstance = ObjectId(id)
    sdf=df.loc[df["id"]==objInstance]
    setshospitallist=sdf.to_dict('records')
    print(setshospitallist)
    return render(request, "about.html",{"setshospitallist":setshospitallist})

def detailsectionodia(request,id):
    hospitals = odiaconn()
    hospitall=list(hospitals)
    print(hospitall)
    df = pd.DataFrame(hospitall)
    # df = pd.read_csv('moswasthyaapp\card_hosp_list.csv')
    df=df.fillna('nan')
    df["id"]=df["_id"]
    print(id)
    objInstance = ObjectId(id)
    sdf=df.loc[df["id"]==objInstance]
    setshospitallist=sdf.to_dict('records')
    print(setshospitallist)
    return render(request, "aboutodia.html",{"setshospitallist":setshospitallist})

def showdefault(request):
    img=imgpath
    imgo=open(img,'rb')
 
    return FileResponse(imgo)

def show(request,img):
    connection_url='Api key'
    client = pymongo.MongoClient(connection_url) 
    db = client.myFirstDatabase
    fs = gridfs.GridFS(db)
    simg=img.replace('https://rah108.in/api/img/', '')
    image = fs.get_last_version(filename=simg)
    
    return FileResponse(image)
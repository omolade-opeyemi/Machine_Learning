from django.shortcuts import render, redirect, reverse
from django.core.files.storage import FileSystemStorage
from .models import CarImage
from .forms import CarForm
import requests 
from requests.compat import quote_plus
import os

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
import numpy as np

# Create your views here.
def homePage(request):
    return render(request, 'home.html')

def predictPage(request):
    if request.method == 'POST':
        fileObj = request.FILES['document']
        x=fileObj.name
        y=x.replace(' ','')
        fs= FileSystemStorage()
        filePath=fs.save(y,fileObj)
        filePath=fs.url(filePath)
        
        with open('./vehicle_classes.json', 'r') as f:
            label=f.read()
        labelinfo = json.loads(label)
        model = load_model('./Vehicle_Recognition_Model_b.h5')
        test_image = tf.keras.preprocessing.image.load_img('.'+filePath, color_mode= 'rgb', target_size = (32, 32, 3))
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        prediction = model.predict(test_image)
        predictLabel=labelinfo[str(np.argmax(prediction))]

        context={'predictLabel':predictLabel, 'filePath':filePath}
        return render(request, 'home.html', context)
    return render(request, 'index.html', )

 
def viewPage(request):
    ListOfImages=os.listdir('./media/')
    print('IMAGESSSSSSSS' , ListOfImages)
    ListOfImagesPath=['./media/'+i for i in ListOfImages]
    zipped = zip(ListOfImages, ListOfImagesPath)
    N ='No image to display'
    context={'zipped':zipped, 'N':N, 'LOI':ListOfImages}
    return render(request, 'viewDB.html',context)

def blogPage(request):
    return render(request, 'blog.html')
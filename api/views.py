from os import name
from django.contrib import auth
from api.models import Informatiomuser, postincordenent, postinf
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, logout
import base64

# Create your views here.
class Posation(View):
    
    a=''
    
    def get(self, request):
        
        post=postincordenent.objects.all()
        # a=list(post.values(''))
        c=[]
        b=list(post.values('user','longtude','lattude'))
        for i in range(len(b)):
            a=b[i]['user']
            user=Informatiomuser.objects.filter(user_id=int(a))
            ima=list(user.values('name','phone'))
            latued=b[i]['lattude']
            nameuser=ima[0]['name']
            phone=ima[0]['phone']
            longtude=b[i]['longtude']
        
            c.append({
                'id':a,
                'phone':phone,
                'nameuser':nameuser,
                'latued':float(latued),
                'longtude':float(longtude)

            })

           
        return JsonResponse(c, safe=False)
    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Posation, self).dispatch(request, *args, **kwargs)

    def post(self, request):
            global a
            dat = request.body
            data=json.loads(dat)
            print(data) 
            id_user=data['id_user']
            lautude=data['lautude']
            longtude=data['longtude']
           
                        
            user=User.objects.get(id=id_user)
            # infuser=postincordenent()
            # infuser.user=user
            # infuser.lattude=lautude
            # infuser.longtude=longtude
            
            # infuser.save()
            a=[{'noterrer':"secsse"}]
                
            return JsonResponse(a, safe=False)

class Getposation(View):
    
    a=''
    
    def get(self, request):
        
        a=[{'noterrer':"secsse"}]
        return JsonResponse(a, safe=False)
    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Getposation, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        
        # a=list(post.values(''))
        global a
        data = request.body
        data = json.loads(data)
        print(data)
        
       
        id=data['id']
            
        
            
        aa=postincordenent.objects.filter(user_id=id)
        a=list(aa.values('longtude','lattude')) 
        a=[{
            'longtude':float(a[0]['longtude']),
            'lattude':float(a[0]['lattude'])
        }]       
        return JsonResponse(a, safe=False)
       

        


class Posting(View):
    
    
    def get(self, request):
        post=postinf.objects.all()
        # a=list(post.values(''))
        c=[]
        b=list(post.values('byuser','imag'))
        for i in range(len(b)):
            a=b[i]['byuser']
            user=Informatiomuser.objects.filter(user_id=int(a))
            ima=user.values('image','name')
            imageuser=ima[0]['image']
            nameuser=ima[0]['name']
            imagepost=b[i]['imag']
        
            c.append({
                'nameuser':nameuser,
                'imageuser':imageuser,
                'imagepost':imagepost

            })

           
        return JsonResponse(c, safe=False)
    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Posting, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        global a
        dat = request.body
        data=json.loads(dat)
        
        iduser=data['id']
        posting=postinf.objects.filter(byuser_id=iduser)
        a=list(posting.values('imag'))
        
            
                
                
           

        return JsonResponse(a, safe=False)
class Users(View):
    a=''
    
    def get(self, request):
        
        return JsonResponse({"error":'لايتوفر بينات'})
    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Users, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        global a
        data = request.body
        data = json.loads(data)
        print(data)
        
        a1={}
        if data==a1:
            return JsonResponse({"error":'لايتوفر بينات'})
        else:
            name=data['username']
            password=data['password']
            user = authenticate(username=name, password=password)
            
            if user is not None:
                
                aa=Informatiomuser.objects.filter(user_id=user)
                a=list(aa.values('user_id','infromation'))
                
                if a==[]:
                    a=[{"erre":'notuserinformation',"user_id":user.pk}]
                else:
                    a=a
                
                
            else:
                b={'erre':'theuserisnotfound'}
                a=[b]

        
        return JsonResponse(a, safe=False)
class Infor(View):
    a=''
    
    def get(self, request):
        
        return JsonResponse({"error":'لايتوفر بينات'})
    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Infor, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        global a
        data = request.body
        data = json.loads(data)
        print(data)
        
        a1={}
        if data==a1:
            return JsonResponse({"error":'لايتوفر بينات'})
        else:
            id=data['id']
            
        
            
            aa=Informatiomuser.objects.filter(user_id=id)
            a=list(aa.values('user','name','lastname','image','nameworke','nameinstgran','Date','phone'))
            
            
                
                
        

        
        return JsonResponse(a, safe=False)
class AddPosting(View):
    
    
    def get(self, request):
        a=[{"errer:non"}]
        return JsonResponse(a, safe=False)
    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AddPosting, self).dispatch(request, *args, **kwargs)

    def post(self, request):
            global a
            dat = request.body
            data=json.loads(dat)
            id=data['id']
            nameimage=data['image']
            image=base64.b64decode(data['codeimage']) 
        
            
            with open('media/posting/'+nameimage, 'wb', ) as f_out:
                    f_out.write(image)
                        
            user=User.objects.get(id=id)
            infuser=postinf()
            infuser.byuser=user
            infuser.imag=nameimage
            infuser.save()
            a=[{'noterrer':"secsse"}]
        
            print('ok man')
                
                
           

            return JsonResponse(a, safe=False)
class Insert(View):

    a=''
    
    def get(self, request):
        
        return JsonResponse({"error":'لايتوفر بينات'})
    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Insert, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        global a
        dat = request.body
        data=json.loads(dat)
        print(data)
        
        a1={
            'id_user':'',
            'name':'',
            'lastname':'',
            'image':''
        } 
        if data==a1:
            a=[{"error": 'notinformationtoinsert'}]
        else:
            id_user=data['id_user']
           
            name=data['name']
            lastname=data['lastname']
            nameimage=data['image']
            phon=data['phonnuber']
            insta=data['nameinstgram']
            work=data['namework']
            image=base64.b64decode(data['codeimage']) 
        
            
            with open('media/user/'+nameimage, 'wb', ) as f_out:
                    f_out.write(image)
                        
            user=User.objects.get(id=id_user)
            
            infuser=Informatiomuser()
            infuser.user=user
            infuser.name=name
            infuser.lastname=lastname
            infuser.image=nameimage
            infuser.phone=phon
            infuser.nameworke=work
            infuser.nameinstgran=insta
            infuser.save()
            a=[{'noterrer':"secsse"}]
                
                
           

        return JsonResponse(a, safe=False)
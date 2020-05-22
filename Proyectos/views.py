from django.shortcuts import render
from .forms import ObrasForm,ImagenesForm
from .models import Obra, Images_model
# Create your views here.
def home(request):
    queryset = Obra.objects.all()[:3]
    context= {
        'object_list':queryset
    }
    
    return render(request, 'Home.html',context)

def obras_list(request):
    queryset = Obra.objects.all()
    context= {
        'object_list':queryset
    }
    return render(request, 'Proyectos/works.html',context)

def detalle_obra(request,id):
    obj = Obra.objects.get(id=id)
    imagenes= Images_model.objects.filter(obra__id=id)
    context= {
        'object':obj,
        'imagenes':imagenes
        
    }
    return render(request, 'Proyectos/works-single.html',context)


def form_view(request):
    my_form = ObrasForm()
    images_form=ImagenesForm()
    if request.method == 'POST':
        my_form = ObrasForm(request.POST,request.FILES)
        images_form = ImagenesForm(request.POST, request.FILES)
        files = request.FILES.getlist('img')
        if my_form.is_valid() and images_form.is_valid():
            instance = my_form.save(commit=False)
            instance.save()       
            #Obra.objects.create(**my_form.cleaned_data)
            
            for f in files:
                file_instance = Images_model(img=f, obra=instance)
                file_instance.save()
            context={
            #'form':my_form
            }
            return render(request,'Proyectos/Form_view.html',context)
        else:
            print('no pasa na')
            return render(request,'Proyectos/Form_view.html',{})
    else:
        print('nofre')
        return render(request,'Proyectos/Form_view.html',{})
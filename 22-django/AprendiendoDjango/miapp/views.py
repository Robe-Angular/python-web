from django.shortcuts import render,HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages


# Create your views here.
# MVC Modelo Vista Controlador
# MVT Modelo Template Vista

layout = """
    <h1>Sitio Web con Django | Víctor Robles</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Página de pruebas</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
"""

def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050: </p>
        <ul>
    ""
    year = 2021
    
    while year <= 2050:
        if year % 2 ==0:
            html += f"<li>{year}</li>"
        year += 1

    html += '</ul></hr>'
    """
    year = 2021
    hasta = range(year, 2051)
    nombre = 'Víctor Robless'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']
    

    return render(request, 'index.html',{
        'title': 'Inicio | Home',
        'mi_variable': 'Soy un dato que está en la vista',
        'years': hasta,
        'nombre': nombre,
        'lenguajes': lenguajes
    })


def  hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):

    if redirigir == 1:
        return redirect('contacto', nombre="Víctor", apellidos="Robles")

    return render(request,'pagina.html',{
        'texto': 'Texto sí hay',
        'lista': ['uno', 'dos', 'tres']
    })

def contacto(request, nombre = "", apellidos= ""):

    html ="""
    """
    
    if nombre and apellidos:
        html = f"<h3>El nombre completo es {nombre} {apellidos}</h3>"

    return HttpResponse(layout + f"""
        <h2>Contacto</h2>
    """ + html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()

    

    return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulo(request):
    try:
        articulo = Article.objects.get(pk=11, public = False)
        response = f"Articulo: {articulo.title}"
    except:
        response = 'Error: Hubo un problema con el Artículo'
    
    return HttpResponse(response)

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Editado a False"
    articulo.content = "Película del 2017"
    articulo.public = False
    articulo.save()

    return HttpResponse(f"Artículo editado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):
    
    articulos = Article.objects.all().filter(public=True).order_by('-updated_at')
    #articulos = Article.objects.order_by('-id')
    #articulos = Article.objects.order_by('-title')
    #articulos = Article.objects.order_by('-id')[:5]
    #articulos = Article.objects.order_by('-id')[2:5]
    """
    articulos = Article.objects.filter(id__lte=7)
    articulos = Article.objects.filter(
        title = "Artículo",
    ).exclude(
        public = True
    )
    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE public=0")


    articulos = Article.objects.filter(
        Q(title__contains = "2")|Q(public=True)
    )
    """

    """
    return  HttpResponse(articulos)

    """
    return  render(request, 'articulos.html',{
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')

def save_article(request):

    if request.method == 'POST':
        title = request.POST['title']
        if len(title) <= 5:
            return HttpResponse('El título es muy pequeño')

        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        articulo.save()
        
        return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el artículo</h2>")

    

def create_article(request):
    return render(request, 'create_article.html')

def create_full_article(request):
    if request.method == 'POST':        
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title= data_form.get('title')
            content= data_form['content']
            public= data_form['public']

            articulo = Article(
            title = title,
            content = content,
            public = public
            )
            articulo.save()

            #Crear mensaje flash
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            return redirect('articulos')

            return HttpResponse(articulo.title + ' ' + articulo.content + ' ' + str(articulo.public))
    else:
       formulario = FormArticle()

    
    return render(request, 'create_full_article.html',{
        'form': formulario
    })
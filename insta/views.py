from django.views.generic import TemplateView,ListView
    


# Create your views here.
class HelloDjango(TemplateView):
    template_name = "home.html"

class PostView(ListView):
    model = Post
    template_name = "posts.html"

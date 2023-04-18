from django.views.generic import ListView, DetailView, TemplateView

from houses.models import House


class BaseView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class HomeView(ListView):
    queryset = House.objects.order_by("-id")
    template_name = "home.html"
    context_object_name = "houses"


class HousesListView(ListView):
    queryset = House.objects.order_by("-id")
    template_name = "houses/houses.html"
    context_object_name = "houses"


class HouseDetailView(DetailView):
    queryset = House.objects.all()
    template_name = "houses/house_detail.html"
    context_object_name = "house"
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     house_id = self.kwargs.get(self.pk_url_kwarg)
    #     context["first_house"] = House.objects.first()
    #     context["house"] = House.objects.filter(id=house_id).first()
    #     return context


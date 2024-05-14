from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from tablib import Dataset
from .models import SimCard
from .forms import SimCardForm
from .ressources import SIMRessource


def simcard_view(request, pk=None, sim=None):
    queryset = SimCard.objects.all()
    filter_title = "Filter"

    if pk:
        sim = SimCard.objects.get(id=pk)
        simform = SimCardForm(request.POST, instance=sim)
    else:
        simform = SimCardForm()

    if request.htmx:
        if "all" in request.GET:
            queryset = SimCard.objects.all()
            filter_title = "ALL"
        if "sim_ok" in request.GET:
            queryset = SimCard.objects.filter(status="ok")
            filter_title = "OK"
        if "sim_broken" in request.GET:
            queryset = SimCard.objects.filter(status="broken")
            filter_title = "BROKEN"
        if "sim_lost" in request.GET:
            queryset = SimCard.objects.filter(status="lost")
            filter_title = "LOST"
        if "sim_stolen" in request.GET:
            queryset = SimCard.objects.filter(status="stolen")
            filter_title = "STOLEN"
        if "sim_in_stock" in request.GET:
            queryset = SimCard.objects.filter(in_stock=True)
            filter_title = "IN STOCK"

        print(filter_title)

        context = {
            "queryset": queryset,
            "filter_title": filter_title,
            "obj": sim,
            "simform": simform,
        }
        return render(request, "snippets/loop_table_row.html", context)
    
    context = {
        "queryset": queryset,
        "simform": simform,
        "obj": sim,
        "filter_title": filter_title,
    }
    return render(request, "simcard/simcard.html", context)


# Search Sim Card View
def search_view(request):
    query = request.GET.get("search", "").strip()
    queryset = SimCard.objects.all()

    if query:
        queryset = SimCard.objects.filter(
            Q(imsi__icontains=query)
            | Q(number__icontains=query)
            | Q(comment__icontains=query)
        )

    return render(request, "snippets/loop_table_row.html", {"queryset": queryset})


# Create Sim Card View
def add_simcard_view(request):
    simform = SimCardForm()
    if request.method == "POST":
        simform = SimCardForm(request.POST)
        if simform.is_valid():
            sim = simform.save(commit=False)
            sim.save()

    ctx = {
        "simform": simform,
        "obj": sim,
    }
    return render(request, "snippets/add_simcard.html", ctx)


# Update Sim Card View
def edit_simcard_view(request, pk):
    obj = get_object_or_404(SimCard, id=pk)
    if request.method == "POST":
        simform = SimCardForm(request.POST, instance=obj)
        if simform.is_valid():
            simform.save()
    else:
        simform = SimCardForm(instance=obj)

        ctx = {"simform": simform, "obj": obj}
        return render(request, "snippets/edit_simcard.html", ctx)
    return redirect('/simcards/')

# Delete Sim Card View
def delete_simcard_view(request, pk):
    sim = get_object_or_404(SimCard, id=pk)
    sim.delete()
    return HttpResponse("")

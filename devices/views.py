from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from .models import Asset
from .forms import AssetForm


def devices(request, pk=None, device=None):
    queryset = Asset.objects.all()
    count = queryset.count()
    if pk:
        device = Asset.objects.get(id=pk)
        deviceform = AssetForm(request.POST, instance=device)
    else:
        deviceform = AssetForm()

    if request.htmx:
        if "all" in request.GET:
            queryset = Asset.objects.all()
        if "galooli" in request.GET:
            queryset = Asset.objects.filter(plateforme="Galooli")
        if "wialon" in request.GET:
            queryset = Asset.objects.filter(plateforme="wialon")
        if "Mix OBC" in request.GET:
            queryset = Asset.objects.filter(plateforme="Mix OBC")
        if "Camera JC" in request.GET:
            queryset = Asset.objects.filter(plateforme="Camera JC")
        if "ums" in request.GET:
            queryset = Asset.objects.filter(site="ums")
            
        context = {
            "queryset": queryset,
            "a_count": count,
            "obj": device,
            "devideform": deviceform,
        }
        return render(request, "snippets/loop_device_table_row.html", context)

    context = {
        "queryset": queryset,
        "obj": device,
        "deviceform": deviceform,
    }
    return render(request, "devices/devices.html", context)


"""
def devices_list(request, pk=None, device=None):
    queryset = Asset.objects.all()
    
    if pk:
        device = Asset.objects.get(id=pk)
        deviceform = AssetForm(request.POST, instance=device)
    else:
        deviceform = AssetForm()

    context = {
        "queryset": queryset,
        "device": device,
        "deviceform": deviceform,
    }

    return render(request, 'snippets/loop_device_table_row.html', context)
"""


def search_device_view(request):
    query = request.GET.get("search", "").strip()
    queryset = Asset.objects.all()

    # If a search query is provided, filter the queryset
    if query:
        # Use Q objects to perform a complex lookup with OR conditions
        queryset = Asset.objects.filter(
            # Search in device type name, sim card IMSI, sim card number, site name, plateforme name, IMEI,
            # registration number, and asset description
            Q(device_type__icontains=query)
            | Q(imsi__icontains=query)
            | Q(number__icontains=query)
            | Q(site__icontains=query)
            | Q(plateforme__icontains=query)
            | Q(imei__icontains=query)
            | Q(registration_number__icontains=query)
            | Q(asset_description__icontains=query)
        )

    return render(
        request,
        "snippets/loop_device_table_row.html",
        {"queryset": queryset, "count": queryset.count()},
    )


# Asset Create View
def device_create_view(request):
    form = AssetForm()
    if request.method == "POST":
        form = AssetForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the value to the model
            instance = form.save(commit=False)
            instance.save()

    ctx = {
        "deviceform": form,
        "obj": instance,
    }

    return render(request, "snippets/device_create.html", ctx)


def device_edit_view(request, pk):
    obj = get_object_or_404(Asset, id=pk)
    if request.method == "POST":
        form = AssetForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = AssetForm(instance=obj)
        ctx = {
            "deviceform": form,
            "obj": obj,
        }
        return render(request, "snippets/device_edit.html", ctx)
    return redirect("/devices/")


def device_delete_view(request, pk):
    device = get_object_or_404(Asset, id=pk)
    if request.method == "POST":
        device.delete()
        return redirect("/devices/")
    #return HttpResponse(status=204, headers={'hx-trigger': 'confirmed'})
    return render(request, "snippets/device_delete.html", {"obj": device})


def asset_count(request):
    asset_list = Asset.objects.all()
    count = asset_list.count()
    print(f"Devices count: {count}")

    return render(request, "snippets/device_count.html", {"a_count": count})

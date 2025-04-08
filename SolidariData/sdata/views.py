from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Family
from .forms import FamilyForm, RelativeFormSet


# Create your views here.
def landing_page(request):
    return render(request, 'landing_page/landing_page.html')

def home(request):
    return render(request, 'sdata/home.html')

#def families(request):
#    return render(request, 'sdata/families/families.html')

def events(request):
    return render(request, 'sdata/events/events.html')

def institutions(request):
    return render(request, 'sdata/institutions/institutions.html')


### Families views ###
# List all families
def family_list(request):
    families = Family.objects.all()
    return render(request, 'sdata/family_list.html', {'families': families})
# View details of a specific family
def family_detail(request, pk):
    family = get_object_or_404(Family, pk=pk)
    return render(request, 'sdata/family_detail.html', {'family': family})
def family_create(request):
    if request.method == "POST":
        family_form = FamilyForm(request.POST)
        relative_formset = RelativeFormSet(request.POST)
        if family_form.is_valid() and relative_formset.is_valid():
            family = family_form.save()
            relatives = relative_formset.save(commit=False)
            for relative in relatives:
                relative.relative_family = family
                relative.save()
            return redirect('family_list')
    else:
        family_form = FamilyForm()
        relative_formset = RelativeFormSet()
    return render(request, 'sdata/family_form.html', {
        'family_form': family_form,
        'relative_formset': relative_formset,
    })

# Update a specific family
def family_update(request, pk):
    family = get_object_or_404(Family, pk=pk)
    if request.method == "POST":
        family_form = FamilyForm(request.POST, instance=family)
        relative_formset = RelativeFormSet(request.POST, instance=family)
        if family_form.is_valid() and relative_formset.is_valid():
            family_form.save()
            relative_formset.save()
            return redirect('family_detail', pk=family.pk)
    else:
        family_form = FamilyForm(instance=family)
        relative_formset = RelativeFormSet(instance=family)
    return render(request, 'sdata/family_form.html', {
        'family_form': family_form,
        'relative_formset': relative_formset,
    })

# Delete a specific family
def family_delete(request, pk):
    family = get_object_or_404(Family, pk=pk)
    if request.method == "POST":
        family.delete()
        return redirect('family_list')
    return render(request, 'sdata/family_confirm_delete.html', {'family': family})
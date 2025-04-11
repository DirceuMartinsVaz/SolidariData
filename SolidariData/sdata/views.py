from django.core.paginator import Paginator
from django.db.models import Q  # For complex queries
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Family
from .forms import FamilyForm, RelativeFormSet
import unicodedata # For accent removal

# Ignore accents in search queries
def remove_accents(input_str):
    return ''.join(
        c for c in unicodedata.normalize('NFD', input_str)
        if unicodedata.category(c) != 'Mn'
    )

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page/landing_page.html')

def home(request):
    return render(request, 'sdata/home.html')

def events(request):
    return render(request, 'sdata/events/events.html')

def institutions(request):
    return render(request, 'sdata/institutions/institutions.html')


### Family views ###
# List all families
def family_list(request):
    # Retrieve ordering and pagination size from query parameters
    search_query = request.GET.get('search', '').lower()  # Convert to lowercase
    search_query_normalized = remove_accents(search_query)  # Normalize the search term
    order_by = request.GET.get('order_by', 'family_representative_name')  # Default ordering
    per_page = request.GET.get('per_page', '10')  # Default page size is 10

       # Filter families based on the normalized search term
    families = [f for f in Family.objects.all().order_by(order_by) if
                remove_accents(f.family_representative_name.lower()).find(search_query_normalized) != -1
                ]

    #families = Family.objects.all().order_by(order_by)

    # Paginate the families based on the selected page size
    paginator = Paginator(families, int(per_page))
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sdata/family_list.html', {
        'page_obj': page_obj, 
        'order_by': order_by, 
        'per_page': per_page,
        'search_query': search_query,
        })

# View details of a specific family
def family_detail(request, pk):
    family = get_object_or_404(Family, pk=pk)
    return render(request, 'sdata/family_detail.html', {'family': family})
# Create a new family
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
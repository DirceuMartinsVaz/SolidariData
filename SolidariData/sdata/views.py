from django.core.paginator import Paginator
#from django.db.models import Q  # For complex queries
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Family, Event, Institution, InstitutionEvent, FamilyEvent, FamilyEventInstitution, InstitutionRepresentative
from .forms import FamilyForm, RelativeFormSet, EventForm, InstitutionForm, InstitutionEventForm, FamilyEventForm, FamilyEventInstitutionForm, InstitutionRepresentativeFormSet, InstitutionRepresentativeForm
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


### Event views ###
def event_list(request):
    # Retrieve ordering and pagination size from query parameters
    search_query = request.GET.get('search', '').lower()
    search_query_normalized = remove_accents(search_query)  # Normalize the search term
    order_by = request.GET.get('order_by', 'event_name')  # Default ordering
    per_page = request.GET.get('per_page', '10')  # Default page size is 10

    # Filter events based on the normalized search term
    events = [e for e in Event.objects.all().order_by(order_by) if
              remove_accents(e.event_name.lower()).find(search_query_normalized) != -1
              ]

    # Paginate the events
    paginator = Paginator(events, int(per_page))
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sdata/event_list.html', {
        'page_obj': page_obj,
        'order_by': order_by,
        'per_page': per_page,
        'search_query': search_query,
    })

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'sdata/event_detail.html', {'event': event})

def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'sdata/event_form.html', {'form': form})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'sdata/event_form.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'sdata/event_confirm_delete.html', {'event': event})


### Institution views ###
def institution_list(request):
    # Retrieve ordering and pagination size from query parameters
    search_query = request.GET.get('search', '').lower()
    search_query_normalized = remove_accents(search_query)  # Normalize the search term
    order_by = request.GET.get('order_by', 'institution_name')  # Default ordering
    per_page = request.GET.get('per_page', '10')  # Default page size is 10

    # Filter institutions based on the normalized search term
    institutions = [i for i in Institution.objects.all().order_by(order_by) if
                    remove_accents(i.institution_name.lower()).find(search_query_normalized) != -1
                    ]

    # Paginate the institutions
    paginator = Paginator(institutions, int(per_page))
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sdata/institution_list.html', {
        'page_obj': page_obj,
        'order_by': order_by,
        'per_page': per_page,
        'search_query': search_query,
    })

def institution_detail(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    return render(request, 'sdata/institution_detail.html', {'institution': institution})

def institution_create(request):
    if request.method == "POST":
        institution_form = InstitutionForm(request.POST)
        representative_formset = InstitutionRepresentativeFormSet(request.POST)
        if institution_form.is_valid() and representative_formset.is_valid():
            institution = institution_form.save()
            representatives = representative_formset.save(commit=False)
            for representative in representatives:
                representative.institution_representative_institution = institution
                representative.save()
            # Redirect to the institution_detail page of the newly created institution
            return redirect('institution_detail', pk=institution.pk)
    else:
        institution_form = InstitutionForm()
        representative_formset = InstitutionRepresentativeFormSet()
    return render(request, 'sdata/institution_form.html', {
        'form': institution_form,
        'representative_formset': representative_formset,
    })

def institution_update(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    if request.method == "POST":
        institution_form = InstitutionForm(request.POST, instance=institution)
        representative_formset = InstitutionRepresentativeFormSet(request.POST, instance=institution)
        if institution_form.is_valid() and representative_formset.is_valid():
            institution_form.save()
            representative_formset.save()
            return redirect('institution_detail', pk=institution.pk)
    else:
        institution_form = InstitutionForm(instance=institution)
        representative_formset = InstitutionRepresentativeFormSet(instance=institution)
    return render(request, 'sdata/institution_form.html', {
        'form': institution_form,
        'representative_formset': representative_formset,
    })

def institution_delete(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    if request.method == "POST":
        institution.delete()
        return redirect('institution_list')
    return render(request, 'sdata/institution_confirm_delete.html', {'institution': institution})


### Institution Representative views ###
def institution_representative_list(request, institution_pk):
    institution = get_object_or_404(Institution, pk=institution_pk)
    representatives = institution.representatives.all()
    return render(request, 'sdata/institution_representative_list.html', {
        'institution': institution,
        'representatives': representatives,
    })


def institution_representative_create(request, institution_pk):
    institution = get_object_or_404(Institution, pk=institution_pk)
    if request.method == "POST":
        form = InstitutionRepresentativeForm(request.POST)
        if form.is_valid():
            representative = form.save(commit=False)
            representative.institution_representative_institution = institution
            representative.save()
            # Redirect to institution_representative_list instead of institution_detail
            return redirect('institution_representative_list', institution_pk=institution.pk)
    else:
        form = InstitutionRepresentativeForm()
    return render(request, 'sdata/institution_representative_form.html', {
        'form': form,
        'institution': institution,
    })


def institution_representative_update(request, institution_pk, pk):
    institution = get_object_or_404(Institution, pk=institution_pk)
    representative = get_object_or_404(InstitutionRepresentative, pk=pk, institution_representative_institution=institution)
    if request.method == "POST":
        form = InstitutionRepresentativeForm(request.POST, instance=representative)
        if form.is_valid():
            form.save()
            # Redirect to institution_representative_list instead of institution_detail
            return redirect('institution_representative_list', institution_pk=institution.pk)
    else:
        form = InstitutionRepresentativeForm(instance=representative)
    return render(request, 'sdata/institution_representative_form.html', {
        'form': form,
        'institution': institution,
    })


def institution_representative_delete(request, institution_pk, pk):
    institution = get_object_or_404(Institution, pk=institution_pk)
    representative = get_object_or_404(InstitutionRepresentative, pk=pk, institution_representative_institution=institution)
    if request.method == "POST":
        representative.delete()
        # Redirect to institution_detail instead of institution_representative_list
        return redirect('institution_detail', pk=institution.pk)
    return render(request, 'sdata/institution_representative_confirm_delete.html', {
        'representative': representative,
        'institution': institution,
    })


### Institution Event views ###
def institution_event_list(request):
    institution_events = InstitutionEvent.objects.all().order_by('-institution_event_registration_date')
    return render(request, 'sdata/institution_event_list.html', {'institution_events': institution_events})

def institution_event_create(request):
    if request.method == "POST":
        form = InstitutionEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('institution_event_list')
    else:
        form = InstitutionEventForm()
    return render(request, 'sdata/institution_event_form.html', {'form': form})

def institution_event_delete(request, pk):
    institution_event = get_object_or_404(InstitutionEvent, pk=pk)
    if request.method == "POST":
        institution_event.delete()
        return redirect('institution_event_list')
    return render(request, 'sdata/institution_event_confirm_delete.html', {'institution_event': institution_event})


### Family Event views ###
def family_event_list(request):
    family_events = FamilyEvent.objects.all().order_by('-family_event_registration_date')
    return render(request, 'sdata/family_event_list.html', {'family_events': family_events})

def family_event_create(request):
    if request.method == "POST":
        form = FamilyEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family_event_list')
    else:
        form = FamilyEventForm()
    return render(request, 'sdata/family_event_form.html', {'form': form})

def family_event_delete(request, pk):
    family_event = get_object_or_404(FamilyEvent, pk=pk)
    if request.method == "POST":
        family_event.delete()
        return redirect('family_event_list')
    return render(request, 'sdata/family_event_confirm_delete.html', {'family_event': family_event})


### Family Event Institution views ###
def family_event_institution_list(request):
    assignments = FamilyEventInstitution.objects.all().order_by('-assigned_date')
    return render(request, 'sdata/family_event_institution_list.html', {'assignments': assignments})

def family_event_institution_create(request):
    if request.method == "POST":
        form = FamilyEventInstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family_event_institution_list')
    else:
        form = FamilyEventInstitutionForm()
    return render(request, 'sdata/family_event_institution_form.html', {'form': form})

def family_event_institution_delete(request, pk):
    assignment = get_object_or_404(FamilyEventInstitution, pk=pk)
    if request.method == "POST":
        assignment.delete()
        return redirect('family_event_institution_list')
    return render(request, 'sdata/family_event_institution_confirm_delete.html', {'assignment': assignment})
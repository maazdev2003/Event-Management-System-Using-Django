# events/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Category
from .forms import EventForm, RegistrationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'events/home.html')  # Ensure this template exists

def event_list(request):
    query = request.GET.get('q', '')
    if query:
        events = Event.objects.filter(title__icontains=query)
    else:
        events = Event.objects.all()
    
    categories = Category.objects.all()
    return render(request, 'events/event_list.html', {'events': events, 'categories': categories})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def events_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    events = Event.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'events/events_by_category.html', {'events': events, 'category': category, 'categories': categories})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def register_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.attendee = request.user
            registration.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = RegistrationForm()
    return render(request, 'events/registration_form.html', {'form': form, 'event': event})

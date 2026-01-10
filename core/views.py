from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import HouseholdProfile, LocationCity, ActivityType, HouseholdActivityLog
from datetime import date

def landing(request):
    return render(request, 'core/landing.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # create empty household profile
            HouseholdProfile.objects.create(
                user=user,
                members_count=1,
                income_bracket='mid',
            )
            login(request, user)
            return redirect('household_profile')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('household_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

@login_required
def household_profile(request):
    profile = HouseholdProfile.objects.get(user=request.user)
    cities = LocationCity.objects.all()
    if request.method == 'POST':
        profile.members_count = request.POST.get('members_count') or 1
        profile.income_bracket = request.POST.get('income_bracket') or 'mid'
        profile.diet_type = request.POST.get('diet_type') or 'nonveg'
        city_id = request.POST.get('city')
        if city_id:
            profile.city_id = city_id
        profile.save()
        return redirect('daily_choices')
    return render(request, 'core/household_profile.html', {
        'profile': profile,
        'cities': cities,
    })

@login_required
def daily_choices(request):
    profile = HouseholdProfile.objects.get(user=request.user)
    activities = ActivityType.objects.all()
    if request.method == 'POST':
        for activity in activities:
            field_name = f"activity_{activity.id}"
            value = request.POST.get(field_name)
            if value:
                HouseholdActivityLog.objects.create(
                    household=profile,
                    activity_type=activity,
                    value=float(value),
                    period_start=date.today(),
                    period_end=date.today(),
                )
        return redirect('ripple_results')
    return render(request, 'core/daily_choices.html', {'activities': activities})

@login_required
def ripple_results(request):
    profile = HouseholdProfile.objects.get(user=request.user)
    logs = HouseholdActivityLog.objects.filter(household=profile).select_related('activity_type')

    # Very simplified calculation: just multiply values by dummy factors
    total_plastic_cost = 0
    total_fashion_cost = 0
    total_transport_cost = 0

    for log in logs:
        if log.activity_type.category == 'plastic':
            total_plastic_cost += log.value * 2  # pretend ₹2 ripple per unit
        elif log.activity_type.category == 'fashion':
            total_fashion_cost += log.value * 5  # pretend ₹5 ripple per item
        elif log.activity_type.category == 'transport':
            total_transport_cost += log.value * 1  # pretend ₹1 per km

    total_cost_5y = (total_plastic_cost + total_fashion_cost + total_transport_cost) * 5

    return render(request, 'core/ripple_results.html', {
        'profile': profile,
        'total_plastic_cost': total_plastic_cost,
        'total_fashion_cost': total_fashion_cost,
        'total_transport_cost': total_transport_cost,
        'total_cost_5y': total_cost_5y,
    })
def ripple_graph(request):
    chain_data = {
        "nodes": [
            {"id": "bags", "label": "Plastic Bags", "group": "plastic"},
            {"id": "leakage", "label": "Plastic Leakage", "group": "env"},
            {"id": "microplastics", "label": "Microplastics", "group": "env"},
            {"id": "fish", "label": "Fish Stocks", "group": "eco"},
            {"id": "prices", "label": "Food Prices ₹500", "group": "money"}
        ],
        "links": [
            {"source": "bags", "target": "leakage", "value": 0.3},
            {"source": "leakage", "target": "microplastics", "value": 0.8},
            {"source": "microplastics", "target": "fish", "value": 0.6},
            {"source": "fish", "target": "prices", "value": 1.0}
        ]
    }
    return render(request, 'core/ripple_graph.html', {'chain_data': chain_data})
def india_map(request):
    cities = LocationCity.objects.values('name', 'state', 'is_coastal', 'id')
    return render(request, 'core/india_map.html', {'cities': list(cities)})

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from dancepartyapp.models import DanceParty


@login_required
def dashboard(request):
    logged_user = request.user
    joined_dance_parties = DanceParty.objects.filter(participants=logged_user)
    unjoined_dance_parties = DanceParty.objects.filter(~Q(participants=logged_user))
    template = loader.get_template('dashboard.html')
    context = {
        'joined_dance_parties': joined_dance_parties,
        'unjoined_dance_parties': unjoined_dance_parties
    }
    return HttpResponse(template.render(context, request))


@login_required
def join_dance_party(request, pk):
    logged_user = request.user
    dance_party = DanceParty.objects.get(pk=pk)
    dance_party.participants.add(logged_user)
    return redirect('dancepartyapp:dashboard')


@login_required
def leave_dance_party(request, pk):
    logged_user = request.user
    dance_party = DanceParty.objects.get(pk=pk)
    dance_party.participants.remove(logged_user)
    return redirect('dancepartyapp:dashboard')

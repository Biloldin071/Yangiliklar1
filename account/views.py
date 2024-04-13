
from django.shortcuts import render

from .models import Profil



def profil_view(request):
    user = request.user
    profil = Profil.objects.get(user=user)
    context = {
        'user': user,
        'profile':profil
    }

    return render(request, 'pages/user_profil.html', context)

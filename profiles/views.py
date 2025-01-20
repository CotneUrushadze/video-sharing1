from django.shortcuts import render, get_object_or_404
from django.views import View 
from profiles.models import *
from videos.models import *


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk-pk)
        videos = Video.object.all().filter(uploader=pk).order_by('-date_poasted')
        user = request.user

        context = {
            'profile': profile,
            'videos': videos,
             'user.profile': user,
        }

        return render(request, 'profiles/profile.html', context)
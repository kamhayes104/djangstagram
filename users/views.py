from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import SignUpForm, ProfileForm

# Create your views here.
@login_required
def profile_list_view(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':
        logged_in_user = request.user.profile
        profile_id = request.POST.get('pk')
        profile = Profile.objects.get(pk=profile_id)
        action = request.POST.get('follow')
        if action == 'follow':
            logged_in_user.following.add(profile)
        elif action == 'unfollow':
            logged_in_user.following.remove(profile)
        logged_in_user.save()
        return redirect('profile_list_view')
    

    context = {
        'profiles': profiles
    }

    return render(request, 'users/profile_list_view.html', context=context)

@login_required
def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)

    posts = profile.user.posts.order_by('-timestamp')
    date_joined = profile.user.date_joined.strftime('%b %d, %Y')

    if request.method == 'POST':
        logged_in_user = request.user.profile
        action = request.POST.get('follow')
        if action == 'follow':
            logged_in_user.following.add(profile)
        elif action == 'unfollow':
            logged_in_user.following.remove(profile)
        logged_in_user.save()
        return redirect('profile_detail', pk)

    context = {
        'profile': profile,
        'posts': posts,
        'date_joined': date_joined
    }

    return render(request, 'users/profile_detail.html', context=context)


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                pk = user.pk
                login(request, user)
                return redirect('complete_profile', pk)
        elif request.method == 'GET':
            form = SignUpForm()
            context = {
                'form': form
            }
            return render(request, 'users/sign_up.html', context=context)
    else:
        return render(request, 'users/sign_up_error.html')


def complete_profile(request, pk):
    user = User.objects.get(pk=pk)
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.user = user
            form.save()
            return redirect('confirm_profile')
    elif request.method == 'GET':
        form = ProfileForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'users/complete_profile.html', context=context)



def confirm_profile(request):
    return render(request, 'users/confirm_profile.html')
    

def edit_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            pk = user.pk
            login(request, user)
            return redirect('complete_profile', pk)
    elif request.method == 'GET':
        form = SignUpForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'users/sign_up.html', context=context)


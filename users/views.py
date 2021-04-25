from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from users.models import Message
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login: {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        # instance param will populate the form
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


@login_required
def chat(request):
    receiver_name = request.GET.get('receiver')

    other_user = User.objects.get(username=receiver_name)
    current_user = request.user
    context = {}
    if request.method == 'GET':
        context['msg_history'] = Message.objects.filter(
            (Q(sender=current_user) & Q(receiver=other_user)) |
            (Q(sender=other_user) & Q(receiver=current_user))).order_by('created_at')

    return render(request, 'users/chat.html', context)


@login_required
def sendmsg(request):
    receiver = request.GET.get('receiver')
    if request.method == 'POST':
        msg_instance = Message(sender=request.user, receiver=User.objects.get(username=receiver))
        form = SendMsgForm(request.POST, instance=msg_instance)
        if form.is_valid():
            form.save()
            messages.success(request, f'Message sent to: {receiver}')
            return redirect('products-home')
    else:
        form = SendMsgForm()

    return render(request, 'users/sendmsg.html', {'form': form})

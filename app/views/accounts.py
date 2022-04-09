from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from app.forms.users import CreateUserForm, EditUserForm, ChangeUserPasswordForm
from app.models import Profile
from django.contrib import messages


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect('/accounts/login')

@login_required
def list(request):
    users = User.objects.filter(is_superuser=0)
    return render(request, 'account/list.html', {'users':users, 'i': 0})

@login_required
def create(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                first_name = form.cleaned_data['first_name']
                username = form.cleaned_data['username']
                last_name = form.cleaned_data['last_name']
                job_title = form.cleaned_data['job_title']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                mobile = form.cleaned_data['mobile']
                permissions = form.cleaned_data['permissions']
                dashboard_row_num = None

                user = User.objects.create(first_name=first_name, username=username, last_name=last_name,
                                             email=email,is_staff=permissions)
                user.set_password(password)
                user.save()
                profile = Profile.objects.create(job_title=job_title, mobile=mobile,user_id=user.id,
                                                 dashboard_row_num=dashboard_row_num)
                profile.save()
                messages.success(request, 'با موفقیت افزوده شد')
                return redirect("/accounts")
            except Exception as e:
                messages.error(request, e.__str__())
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = CreateUserForm()
    return render(request, 'account/create.html', {'form': form})

@login_required
def edit(request, id):
    user = get_object_or_404(User, pk=id)
    profile = Profile.objects.filter(user_id=user.id)[0]
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            try:
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                profile.job_title = form.cleaned_data['job_title']
                user.email = form.cleaned_data['email']
                profile.mobile = form.cleaned_data['mobile']
                user.is_staff = form.cleaned_data['permissions']
                if user.username != "admin":
                    user.is_active = form.cleaned_data['is_active']
                user.save()
                profile.save()
                messages.success(request, 'با موفقیت ویرایش شد')
                return redirect("/accounts")
            except Exception as e:
                messages.error(request, e.__str__())
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = EditUserForm()
        form.initial["username"] = user.username
        form.initial["first_name"] = user.first_name
        form.initial["last_name"] = user.last_name
        form.initial["email"] = user.email
        form.initial["permissions"] = "1" if user.is_staff else "0"
        form.initial["is_active"] = "1" if user.is_active else "0"
        form.initial["job_title"] = profile.job_title
        form.initial["mobile"] = profile.mobile
    return render(request, 'account/edit.html', {'form': form})

@login_required
def change_user_password(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = ChangeUserPasswordForm(request.POST)
        if form.is_valid():
            try:
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                messages.success(request, 'با موفقیت ویرایش شد')
                return redirect("/accounts")
            except Exception as e:
                messages.error(request, e.__str__())
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = ChangeUserPasswordForm()
        form.initial["username"] = user.username
    return render(request, 'account/change_user_password.html', {'form': form})

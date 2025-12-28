from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Copier
from .forms import CopierForm
from .utils import is_admin, is_serwisant, is_super_admin


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Copier
from .forms import CopierForm


from django.http import HttpResponseForbidden

def is_admin(user):
    return user.groups.filter(name='admin').exists() or user.is_superuser


def is_serwisant(user):
    return user.groups.filter(name='serwisant').exists()


@login_required
def home(request):
    copiers = Copier.objects.all()

    context = {
        'copiers': copiers,
        'is_super_admin': is_super_admin(request.user),
        'is_admin': is_admin(request.user),
        'is_serwisant': is_serwisant(request.user),
    }

    return render(request, 'copiers/home.html', context)



# ===== ROLE =====
@login_required
def add_copier(request):
    if not (is_super_admin(request.user) or is_admin(request.user)):
        return redirect('home')

    if request.method == 'POST':
        form = CopierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CopierForm()

    return render(request, 'copiers/add_copier.html', {'form': form})


@login_required
def delete_copier(request, id):
    if not (is_super_admin(request.user) or is_admin(request.user)):
        return redirect('home')

    copier = get_object_or_404(Copier, id=id)
    copier.delete()
    return redirect('home')


# ===== HOME =====
@login_required
def home(request):
    copiers = Copier.objects.all()
    copiers_count = copiers.count()  # 👈 LICZBA

    context = {
        'copiers': copiers,
        'copiers_count': copiers_count,
        'is_super_admin': is_super_admin(request.user),
        'is_admin': is_admin(request.user),
        'is_serwisant': is_serwisant(request.user),
    }

    return render(request, 'copiers/home.html', context)


@login_required
def add_copier(request):
    if request.method == 'POST':
        form = CopierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CopierForm()

    return render(request, 'copiers/add_copier.html', {'form': form})


@login_required
def edit_copier(request, pk):
    copier = get_object_or_404(Copier, pk=pk)

    if is_serwisant(request.user):
        allowed_fields = ['total_counter', 'mono_counter', 'color_counter']
    elif is_admin(request.user):
        allowed_fields = None
    else:
        return HttpResponseForbidden("Brak uprawnień")

    if request.method == "POST":
        form = CopierForm(request.POST, instance=copier)

        if form.is_valid():
            if allowed_fields is not None:
                for field in form.cleaned_data:
                    if field not in allowed_fields:
                        setattr(copier, field, getattr(copier, field))
            copier.save()
            return redirect('home')
    else:
        form = CopierForm(instance=copier)

        if allowed_fields is not None:
            for field in form.fields:
                if field not in allowed_fields:
                    form.fields[field].disabled = True

    return render(request, 'copiers/edit_copier.html', {
        'form': form,
        'copier': copier
    })



@login_required
def confirm_delete_copier(request, id):
    copier = get_object_or_404(Copier, id=id)
    return render(request, 'copiers/confirm_delete.html', {
        'copier': copier
    })


@login_required
def delete_copier(request, id):
    copier = Copier.objects.get(id=id)
    copier.delete()
    return redirect('home')

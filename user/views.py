from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm

# ყველა მომხმარებლების სიის ნახვა
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

# ახალი მომხმარებლის დამატება
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

# მომხმარებლის რედაქტირება
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

# მომხმარებლის წაშლა
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_delete.html', {'user': user})
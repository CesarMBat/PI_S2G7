from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddAnimalForm
from .models.animais import Animal


def home(request):
	records = Animal.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Você está logado...")
			return redirect('home')
		else:
			messages.success(request, "Houve um erro ao tentar logar...Tente novamente...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'animais':records})



def logout_user(request):
	logout(request)
	messages.success(request, "Voçê saiu da sua conta...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Voçe foi registrado com sucesso...Bem vindo...")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def registro_do_animal(request, pk):
	if request.user.is_authenticated:
		animais = Animal.objects.get(id=pk)
		return render(request, 'record.html', {'animais':animais})
	else:
		messages.success(request, "Voce precisa estar logado para fazer isso...")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Animal.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Animal Deletado...")
		return redirect('home')
	else:
		messages.success(request, "Voçe precisa estar logado para fazer isso...")
		return redirect('home')


def add_animal(request):
	form = AddAnimalForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Animal adcionado")
				return redirect('home')
		return render(request, 'add_animal.html', {'form':form})
	else:
		messages.success(request, "Voçe precisa estar logado para fazer isso...")
		return redirect('home')


def update_animal(request, pk):
	if request.user.is_authenticated:
		current_record = Animal.objects.get(id=pk)
		form = AddAnimalForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Animal Atualizado")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Voçe precisa estar logado para fazer isso...")
		return redirect('home')
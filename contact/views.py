from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from contact.forms import ContactForm



# Функция формы обратной связи
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']
			name = form.cleaned_data['name']


			recepients = ['andreydecua@gmail.com']

			global_message = "Імя: " + name + "\n" + "Повідомлення: " + message

            # Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recepients.append(sender)
			try:
				send_mail(subject, global_message, sender, recepients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			# Переходим на другую страницу, если сообщение отправлено
			return render(request, 'contact/thanks.html', {'form': form})

		else:
			form = ContactForm()
	# Выводим форму в шаблон
	return render(request, 'contact/contact.html')

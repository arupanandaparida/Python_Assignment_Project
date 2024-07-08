from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
import random
from .models import User

def index(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    quotes = [
        "I beg to introduce myself to you as a clerk in the Accounts Department of the Port Trust Office at Madras…After leaving school, I have been employing the spare time at my disposal to work at Mathematics. -Srinivasa Ramanujan"
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb"
    ]
 
    random_quote = random.choice(quotes)
    return render(request,'SimplewebApp/index.html',{'current_time':current_time,'random_qutoes':random_quote})
def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = User(name=name, email=email)
        user.save()
        return redirect('show_data')
    else:
        return render(request, 'SimplewebApp/index.html')

def show_data(request):
    users = User.objects.all()
    return render(request, 'SimplewebApp/data.html', {'users': users})

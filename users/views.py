
from datetime import datetime

from allauth.account.forms import LoginForm, SignupForm



def login_signup(request):

    data = {
        'form1': LoginForm,
        'form2': SignupForm,

    }



    return render(request, 'account/login_signup.html', data)

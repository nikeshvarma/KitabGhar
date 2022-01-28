from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.template.loader import render_to_string, get_template
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import TemplateView, CreateView

User = get_user_model()


class SignUpUserView(CreateView):
    """ Create New User Account """

    queryset = User.objects.all()
    fields = ('name', 'email', 'phone', 'password')
    template_name = 'account/signup.html'

    def post(self, request, *args, **kwargs):

        if not User.objects.filter(email=request.POST.get('email')).exists():
            User.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                password=make_password(request.POST.get('password'))
            )
            return redirect('home_view')

        else:
            messages.error(request, 'The email address you have entered is already registered.', extra_tags='danger')
            return redirect('signup_user')


class LoginUserView(TemplateView):
    """ Login an existing user """

    template_name = 'account/login.html'

    def post(self, request, *args, **kwargs):
        user = authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('home_view')

        else:
            messages.error(request, 'Incorrect email or password', extra_tags='danger')
            return redirect('login_user')


def logout_user(request):
    """ Logout User """

    logout(request)
    return redirect('home_view')


class ProfileView(TemplateView):
    """ Display the profile of user """

    template_name = 'account/profile.html'


class ForgetPasswordRequestView(TemplateView):
    """ Initiate forget password process """

    template_name = 'account/forget_password_request.html'

    def generate_email(self, user, request, metadata):
        data = {
            'domain': metadata['HTTP_HOST'],
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
            'protocol': metadata['wsgi.url_scheme'],
            'user': user
        }

        email = render_to_string('extra/password_reset_template.html', data)
        html_email = get_template('extra/password_reset_template.html').render(data)

        try:
            mail = EmailMultiAlternatives('Password Reset', email, 'nikeshvarma08@gmail.com', [user.email])
            mail.attach_alternative(html_email, 'text/html')
            mail.send()

        except BadHeaderError:
            messages.error(request, 'Provided email address not registered in our system', extra_tags='danger')
            return redirect('forgot_pass_request')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            self.generate_email(User.objects.get(email=email), request, request.META)
            return redirect('forgot_pass_mail_sent')

        else:
            messages.error(request, 'Provided email address not registered in our system', extra_tags='danger')
            return redirect('forgot_pass_request')


class ForgetPasswordLinkSendView(TemplateView):
    """ Display after successful email link send """

    template_name = 'account/forget_password_link_send.html'


class ForgetPasswordChangePasswordView(TemplateView):
    """ Set the new password """

    template_name = 'account/forget_password_change.html'

    def get_context_data(self, **kwargs):
        context = super(ForgetPasswordChangePasswordView, self).get_context_data()
        context['uid'] = self.kwargs.get('uidb64')
        context['token'] = self.kwargs.get('token')
        return context

    def post(self, request, *args, **kwargs):

        uid = request.POST.get('uid')
        token = request.POST.get('token')
        passwd1 = request.POST.get('password1')
        passwd2 = request.POST.get('password2')

        if uid is not None and token is not None:
            if passwd1 == passwd2:
                try:
                    uid = force_str(urlsafe_base64_decode(uid))
                    user = User.objects.get(pk=uid)

                except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                    user = None

                if user is not None and default_token_generator.check_token(user, token):
                    user.set_password(passwd1)
                    user.save()
                    return redirect('forget_password_success')

                else:
                    messages.error(request, 'Invalid token or user ! Create new request to change password', extra_tags='danger')
                    return redirect('forget_pass_change', uid, token)

            else:
                messages.error(request, 'Password and confirm password should be same', extra_tags='danger')
                return redirect('forget_pass_change', uid, token)
        else:
            messages.error(request, 'Invalid token or user ! Create new request to change password', extra_tags='danger')
            return redirect('forget_pass_change', uid, token)


class ForgetPasswordSuccessView(TemplateView):
    """ Display success message  """

    template_name = 'account/forget_password_success.html'

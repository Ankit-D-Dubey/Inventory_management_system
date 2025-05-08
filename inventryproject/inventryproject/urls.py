from django.contrib import admin
from django.urls import path,include
from user import views as user_view
from user.forms import LoginForm, MyPasswordResetForm,MySetPasswordForm
from django.contrib.auth import views as auth_views  #yaha pe view ko ek naya name diya gaya hai aur ye login and logout ke liye use hots hao
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('register/',user_view.register,name='user-register'),
    path('profile/',user_view.profile,name='user-profile'),
    path('profile/update',user_view.profile_update,name='user-profile-update'),
    path('',auth_views.LoginView.as_view(template_name='user/login.html',authentication_form=LoginForm),name='user-login'),
    #yaha pe jo temp_name hai ye matlab form kaha render karna hai vo hai ye nahi doge to error dega
    path('logout/',auth_views.LogoutView.as_view(template_name="user/logout.html"),name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset.html',
    form_class=MyPasswordResetForm),name='password_reset'), 
    #form_class isse hum batate hai ki es view ke liye kon sa form use kiya jaye jo user ko show hoga jo tumne banaya hai
    #forms.py ka use karke
    #es view ke ander {'form':form} ye context likha hota hai 
    #aur es url me MyPasswordResetForm me se form ye pass ho raha hai password_reset.html 
    #template me tabhi hum us html page me form ye use kr pa rahe hai
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html')
         ,name='password_reset_done'),
    #path('password_reset_confirm/<uid64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password-reset-confirm'),
    # path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name=
        'user/password_reset_complete.html'),name='password_reset_complete'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    
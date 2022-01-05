from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
from .forms import SignUpForm, ProfileUpdateForm, UserUpdateForm


# Create your views here.

def index(request):
    return render(request, 'index.html', {})



def login_page(request):
    if request.method == 'POST':
        print('i am here')
        get_username = request.POST.get('get_username')
        get_Password = request.POST.get('get_Password')
        print('get_username')
        print(get_username)
        print(get_Password)

        user_vari = authenticate(username=get_username, password=get_Password)
        print('user_vari')
        print(user_vari)

        if user_vari is not None:
            login(request, user_vari)

            return redirect('profile')
        else:
            massage_for_wrong_info = 'your username or password are wrong !'
            contex = {'massage_for_wrong_info': massage_for_wrong_info}

            return render(request, "accounts/login.html", contex)

    return render(request, "accounts/login.html")

def login_redirect_from_logout(request):
    print('i am here')
    massage_log_out = 'you are successfully log out!'
    contex = {'massage_log_out':massage_log_out}
    logout(request)
    return render(request, "accounts/login.html", contex)

def logout_page(request):
    print('i am here')
    massage_log_out = 'you are successfully log out!'
    contex = {'massage_log_out':massage_log_out}
    logout(request)
    return render(request, "accounts/login.html", contex)






#########################
# SIGN UP VIEWS
#########################
def signup_view(request):
    if request.method == 'POST':
        print('sohel i am j')

        form = SignUpForm(request.POST)

        get_username_signup = request.POST.get('get_username_signup')
        get_email_signup = request.POST.get('get_email_signup')
        get_password_signup = request.POST.get('get_password_signup')
        get_con_password_signup = request.POST.get('get_con_password_signup')
        print(get_username_signup)
        print(get_email_signup)
        print(get_password_signup)
        print(get_con_password_signup)


        if get_password_signup == get_con_password_signup:
            d = User.objects.filter(username = get_username_signup)
            print('d')
            print(d)
            if d:
                print('ko')
                messages.warning(request, f'User name is already taken')
                return redirect('signup')
            else:
                print('save')
                myusr_vari = User.objects.create_user(get_username_signup, get_email_signup, get_password_signup)
                myusr_vari.save()

                messages.success(request, f'Account created for {get_username_signup}!')
                return redirect('login_page')
        else:
            messages.warning(request, f'your password dose not match')
            return redirect('signup')


        # if form.is_valid():
        #     user = form.save()
        #     login(request, user)
        #
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     # raw_password = form.cleaned_data.get('password1')
        #     # user = authenticate(username=username, password=raw_password)
        #     # log the user in
        #     # login(request, user)
        #     messages.success(request, f'Account created for {username}!')
        #     return redirect('login_page')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():  # and user is not None:
#             user = form.get_user()
#             login(request, user)
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'{username} logged in!')
#             # Redirect to a success page.
#             return redirect('profile_view')
#     else:
#         # Return an 'invalid login' error message.
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})


# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#     return redirect('accounts/logout.html')

#########################
#########################
# ACCOUNT VIEWS
#########################
#########################
@login_required
def account_detail_view(request):
    print('pppppppppppp')
    usr = request.user
    if request.user.is_authenticated:
        get_data = User.objects.get(username=usr)
        get_data_profile = Profile.objects.get(user=get_data)
        get_data_profile_social_info = urls_social.objects.filter(user_profile=get_data_profile)


    else:
        get_data= ''
        get_data_profile = ''
        get_data_profile_social_info = ''

    if request.method == 'POST':
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
        'p_form': p_form,
        'get_data':get_data,
        'get_data_profile':get_data_profile,
        'get_data_profile_social_info':get_data_profile_social_info
    }
    return render(request, "accounts/account_create.html", context)

#########################
#########################
#      -TEST_VIEWS-     #
#########################
#########################


def going_to_save_account(request):
    if request.user.is_authenticated:
        usr = request.user
        get_Profile = Profile.objects.get(user=usr)

        going_to_change_User_tabel_username = request.GET.get('going_to_change_User_tabel_username')
        going_to_change_User_tabel_email = request.GET.get('going_to_change_User_tabel_email')
        going_to_change_profile_tabel_name = request.GET.get('going_to_change_profile_tabel_name')
        going_to_change_profile_tabel_Perfered_payment = request.GET.get('going_to_change_profile_tabel_Perfered_payment')
        going_to_change_profile_tabel_Payment_account_detalls = request.GET.get('going_to_change_profile_tabel_Payment_account_detalls')

        inpt_link1 = request.GET.get('inpt_link1')
        select_name1 = request.GET.get('select_name1')
        inpt_link2 = request.GET.get('inpt_link2')
        select_name2 = request.GET.get('select_name2')
        inpt_link3 = request.GET.get('inpt_link3')
        select_name3 = request.GET.get('select_name3')
        inpt_link4 = request.GET.get('inpt_link4')
        select_name4 = request.GET.get('select_name4')
        inpt_link5 = request.GET.get('inpt_link5')
        select_name5 = request.GET.get('select_name5')
        inpt_link6 = request.GET.get('inpt_link6')
        select_name6 = request.GET.get('select_name6')
        inpt_link7 = request.GET.get('inpt_link7')
        select_name7 = request.GET.get('select_name7')
        inpt_link8 = request.GET.get('inpt_link8')
        select_name8 = request.GET.get('select_name8')


        print('inpt_link1inpt_link1')
        print(inpt_link1)
        print(inpt_link1)

        context = {
            'get_Profile':get_Profile,

            'going_to_change_User_tabel_username':going_to_change_User_tabel_username,
            'going_to_change_User_tabel_email':going_to_change_User_tabel_email,
            'going_to_change_profile_tabel_name':going_to_change_profile_tabel_name,
            'going_to_change_profile_tabel_Perfered_payment':going_to_change_profile_tabel_Perfered_payment,
            'going_to_change_profile_tabel_Payment_account_detalls':going_to_change_profile_tabel_Payment_account_detalls,

            'inpt_link1':inpt_link1,
            'select_name1':select_name1,
            'inpt_link2':inpt_link2,
            'select_name2':select_name2,
            'inpt_link3':inpt_link3,
            'select_name3':select_name3,
            'inpt_link4':inpt_link4,
            'select_name4':select_name4,
            'inpt_link5':inpt_link5,
            'select_name5':select_name5,
            'inpt_link6':inpt_link6,
            'select_name6':select_name6,
            'inpt_link7':inpt_link7,
            'select_name7':select_name7,
            'inpt_link8':inpt_link8,
            'select_name8':select_name8,
        }



        return render(request, 'accounts/video_and_bio.html', context)
    return redirect('login_page')


def going_to_save_all_info(request):
    if request.user.is_authenticated:
        upload_a_video = request.FILES.get('upload_a_video')

        upload_a_Bio = request.POST.get('upload_a_Bio')
        profile_pic_for_save = request.FILES.get('profile_pic_for_save')

        print('profile_pic_for_save')
        print('profile_pic_for_save')
        print(profile_pic_for_save)
        print(upload_a_Bio)

        #hidden value
        User_tabel_username = request.POST.get('User_tabel_username')
        User_tabel_email = request.POST.get('User_tabel_email')
        profile_tabel_name = request.POST.get('profile_tabel_name')
        profile_tabel_Perfered_payment = request.POST.get('profile_tabel_Perfered_payment')
        profile_tabel_Payment_account_detalls = request.POST.get('profile_tabel_Payment_account_detalls')
        inpt_link1 = request.POST.get('inpt_link1')
        select_name1 = request.POST.get('select_name1')
        inpt_link2 = request.POST.get('inpt_link2')
        select_name2 = request.POST.get('select_name2')
        inpt_link3 = request.POST.get('inpt_link3')
        select_name3 = request.POST.get('select_name3')
        inpt_link4 = request.POST.get('inpt_link4')
        select_name4 = request.POST.get('select_name4')
        inpt_link5 = request.POST.get('inpt_link5')
        select_name5 = request.POST.get('select_name5')
        inpt_link6 = request.POST.get('inpt_link6')
        select_name6 = request.POST.get('select_name6')
        inpt_link7 = request.POST.get('inpt_link7')
        select_name7 = request.POST.get('select_name7')
        inpt_link8 = request.POST.get('inpt_link8')
        select_name8 = request.POST.get('select_name8')


        print('inpt_link1')
        print('inpt_link1')
        print('inpt_link1')
        print('inpt_link1')
        print(inpt_link1)
        print(inpt_link1)
        print(inpt_link1)

        usr = request.user
        get_data_profile = Profile.objects.get(user=usr)
        if upload_a_video != None:
            get_data_profile.profile_video=upload_a_video
        if profile_pic_for_save != None:
            get_data_profile.profile_pic=profile_pic_for_save
        get_data_profile.bio=upload_a_Bio

        get_data_profile.name=profile_tabel_name
        get_data_profile.prefered_payment=profile_tabel_Perfered_payment
        get_data_profile.payment_account_details=profile_tabel_Payment_account_detalls

        get_data_profile.username = request.user.username
        get_data_profile.email = request.user.email

        get_data_profile.save()


        get_user_from_user_tabel=request.user
        get_user_from_user_tabel.username=User_tabel_username
        get_user_from_user_tabel.email=User_tabel_email
        get_user_from_user_tabel.save()


        print('select_name1')
        print('select_name1')
        print('select_name1')
        print(select_name1)
        print(select_name2)
        print(select_name3)
        print(select_name4)
        print(select_name5)
        print(select_name6)
        print(select_name7)
        print(select_name8)



        get_data_profile = Profile.objects.get(user=usr)

        if select_name1 != 'None' and select_name1 != '':
            get_urls_social = urls_social(user_profile =get_data_profile ,social_media_handles_name=select_name1, social_media_handles_url = inpt_link1)
            get_urls_social.save()
        if select_name2 != 'None' and select_name2 != '':
            get_urls_social = urls_social(user_profile=get_data_profile, social_media_handles_name=select_name2, social_media_handles_url=inpt_link2)
            get_urls_social.save()
        if select_name3 != 'None' and select_name3 != '':
            get_urls_social = urls_social(user_profile=get_data_profile, social_media_handles_name=select_name3, social_media_handles_url=inpt_link3)
            get_urls_social.save()
        if select_name4 != 'None' and select_name4 != '':
            get_urls_social = urls_social(user_profile=get_data_profile, social_media_handles_name=select_name4, social_media_handles_url=inpt_link4)
            get_urls_social.save()
        if select_name5 != 'None' and select_name5 != '':
            get_urls_social = urls_social(user_profile=get_data_profile, social_media_handles_name=select_name5, social_media_handles_url=inpt_link5)
            get_urls_social.save()
        if select_name6 != 'None' and select_name6 != '':
            get_urls_social = urls_social(user_profile=get_data_profile, social_media_handles_name=select_name6, social_media_handles_url=inpt_link6)
            get_urls_social.save()
        if select_name7 != 'None' and select_name7 != '':
            get_urls_social = urls_social(user_profile=get_data_profile, social_media_handles_name=select_name7, social_media_handles_url=inpt_link7)
            get_urls_social.save()
        if select_name8 != 'None' and select_name8 != '':
            get_urls_social = urls_social(user_profile=get_data_profile, social_media_handles_name=select_name8, social_media_handles_url=inpt_link8)
            get_urls_social.save()

        messages.success(request, 'your profile is update  successfully ')
        return redirect('profile')

    return redirect('login_page')


def delete_this(request, pk_id):
    get_info = urls_social.objects.get(id=pk_id)
    get_info.delete()
    return redirect('profile')

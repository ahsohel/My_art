from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtUploadForm, ArtworkDetail
from django.http import JsonResponse
from .models import Upload, ArtworkDetails as ArtworkDetailsModel


# Create your views here.
#########################
# DESIGN VIEWS
#########################
def designs_view(request):
    return render(request, "pages/designs.html")


@login_required
def art_upload_view(request):

    upload = Upload.objects.filter(user=request.user).last()
    u_form = ArtUploadForm(instance=upload)
    # print(u_form)
    artwork_details = ArtworkDetailsModel.objects.filter(
        user=request.user).last()
    artwork_details_form = ArtworkDetail(instance=artwork_details)
    context = {
        'u_form': u_form,
        'artwork_details_form': artwork_details_form,
        'upload_images': Upload.objects.filter(user=request.user, is_uploaded=True),
        "last_image": Upload.objects.filter(user=request.user).last(),
    }
    return render(request, "pages/design.html", context)


@login_required
def save_image(request):
    if request.method == "POST":
        if request.is_ajax():
            title = request.POST.get('title', None)
            image = request.FILES.get('image')
            print(title, image)
            # description = request.POST.get('up_description', None)
            if image:
                image = Upload.objects.create(
                    user=request.user, title=title, image=image)
                image.save()
                last_image = Upload.objects.filter(user=request.user).last()
                return JsonResponse({'title': last_image.title, 'last_img_url': last_image.image.url})
            else:
                return JsonResponse({'status': False})
        return JsonResponse({'status': True})


#
# @login_required
# def save_image_show_first(request):
#     if request.method == "POST":
#         if request.is_ajax():
#             print('hello boss')
#             print('hello boss')
#             print('hello boss')
#             print('hello boss')
#
#             image = request.FILES.get('image')
#             print(image)
#             # description = request.POST.get('up_description', None)
#             if image:
#                 image = Upload.objects.create(
#                     user=request.user, title=title, image=image)
#                 image.save()
#                 last_image = Upload.objects.filter(user=request.user).last()
#                 return JsonResponse({'title': last_image.title, 'last_img_url': last_image.image.url})
#             else:
#                 return JsonResponse({'status': False})
#         return JsonResponse({'status': True})
#

@login_required
def upload_at_work(request):
    print('sohel i am here 2')
    if request.method == "POST":
        category = request.POST.get('category', None)
        print('category')
        print(category)
        description = request.POST.get('description', None)
        title = request.POST.get("title", None)
        tag = request.POST.get("tag", None)

        print(tag)
        art_work = ArtworkDetailsModel.objects.filter(
            user=request.user).first()
        if art_work:
            art_work.category = category
            art_work.description = description
            art_work.title = title
            art_work.tag = tag
            # print(art_work)
            art_work.save()
            return JsonResponse({'status': "updated artwork.."})
        else:
            art = ArtworkDetailsModel.objects.create(
                user=request.user, title=title, tag=tag, category=category, description=description)
            art.save()
            return JsonResponse({'status': "created artwork.."})


# category: category,
# description: description,
# title: title,
# tag: tag,
# description: description,
# category: category


@login_required
def published_art_work(request):
    if request.method == "POST":

        is_uploaded = request.POST.get('is_uploaded', None)
        # print(is_uploaded.title())
        upload = Upload.objects.filter(user=request.user).last()
        if upload and is_uploaded:
            upload.is_uploaded = is_uploaded.title()
            upload.save()
            return redirect("design")

    # upload = Upload.objects.filter(user=request.user).last()
    # u_form = ArtUploadForm(instance=upload)
    # artwork_details = ArtworkDetailsModel.objects.filter(
    #     user=request.user).last()
    # artwork_details_form = ArtworkDetail(instance=artwork_details)
    # context = {
    #     'u_form': u_form,
    #     'artwork_details_form': artwork_details_form,
    #     'upload_images': Upload.objects.filter(user=request.user, is_uploaded=True),
    #     "last_image": Upload.objects.filter(user=request.user).last(),
    # }
    # return render(request, 'pages/ajax_reload_page.html', context)
    return JsonResponse({'status': "uploaded successfully.."})

# def artwork_details_view(request):
#     if request.method == 'POST':
#         artwork_details_form = ArtworkDetails(request.POST, request.FILES, instance=request.user.artwork_details)
#
#         if artwork_details_form.is_valid():
#             artwork_details_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('design')
#     else:
#         artwork_details_form = ArtworkDetails(instance=request.user.artwork_details)
#
#     context = {
#         'artwork_details_form': artwork_details_form
#     }
#     return render(request, "pages/designs.html", context)



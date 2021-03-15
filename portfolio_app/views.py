from PIL import ImageColor
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from _profile.forms import LayoutForm, ProfileForm
from _profile.models import Profile, Layout
from blog.models import Post
from dashboard.forms import TestimonialForm, SkillsForm
from dashboard.models import Testimonial, Skills, Service, Resume
from users.forms import ContactUserForm
from users.models import User
from dashboard.forms import ProjectForm, ProjectItemsForm
from dashboard.models import Project, ProjectItem

DEFAULT_REDIRECT_URL = settings.DEFAULT_REDIRECT_URL


def handler404(request, exception):
    response = render(request, '404.html', context={})
    response.status_code = 404
    return response


def handler500(request, exception):
    response = render(request, '500.html', context={})
    response.status_code = 500
    return response


def my_portfolio(request, username):
    print('the requsest get_raw_uri', request.get_raw_uri())
    print('this is the username', username)
    _username = User.objects.filter(username=username).first()
    if _username:
        project = Project.objects.filter(user__username=username)
        project_items = ProjectItem.objects.filter(user__username=username)
        profile = Profile.objects.filter(user__username=username).first()
        skills = Skills.objects.filter(user__username=username)
        testimonial = Testimonial.objects.filter(user__username=username)
        layout = Layout.objects.filter(user__username=username).first()
        service = Service.objects.filter(user__username=username)
        resume = Resume.objects.filter(user__username=username)
        post = Post.objects.filter(user__username=username)
        try:
            primary_color_nums = ImageColor.getrgb(layout.primary_color)
            secondary_color_nums = ImageColor.getrgb(layout.secondary_color)
            primary_color_1 = primary_color_nums[0]
            primary_color_2 = primary_color_nums[1]
            primary_color_3 = primary_color_nums[2]
            secondary_color_1 = secondary_color_nums[0]
            secondary_color_2 = secondary_color_nums[1]
            secondary_color_3 = secondary_color_nums[2]
            print('this is the project items', project_items)
            host_url = f"{profile.user.username}{settings.PARENT_HOST}",


        except Exception:
            primary_color_nums = None
            secondary_color_nums = None
            host_url = None
            primary_color_1 = None
            primary_color_2 = None
            primary_color_3 = None
            secondary_color_1 = None
            secondary_color_2 = None
            secondary_color_3 = None
    else:
        messages.warning(request, "the site does not exist")
        return HttpResponseRedirect(DEFAULT_REDIRECT_URL)
    context = {
        'project': project,
        'ProjectItem': project_items,
        'profile': profile,
        'skills': skills,
        'testimonial': testimonial,
        'layout': layout,
        'post': post,
        'service': service,
        'resume': resume,
        'media_url': DEFAULT_REDIRECT_URL,
        'host_url': host_url,
        'primary_color': {
            'primary_color_1': primary_color_1,
            'primary_color_2': primary_color_2,
            'primary_color_3': primary_color_3,
        },
        'secondary_color': {
            'secondary_color_1': secondary_color_1,
            'secondary_color_2': secondary_color_2,
            'secondary_color_3': secondary_color_3,
        },

        'contact_user_form': ContactUserForm(),
        'user': 'user',
        'layout_form': LayoutForm(),
        'profile_form': ProfileForm(),
        'testimonial_form': TestimonialForm(),
        'skills_form': SkillsForm(),
        'Project_form': ProjectForm(),
        'Project_items_form': ProjectItemsForm(),
        'domain': DEFAULT_REDIRECT_URL,

    }
    print(DEFAULT_REDIRECT_URL)
    if profile:
        try:
            return render(request,
                          f'portfolio/{layout.portfolio_version.portfolio_version}/{layout.portfolio_version.portfolio_version}.html',
                          context)
        except:
            print('except', layout.portfolio_version.portfolio_version)
            return render(request, 'portfolio/portfolio_v1/portfolio_v1.html', context)
    else:
        messages.warning(request, "the site does not exist")
        return HttpResponseRedirect(DEFAULT_REDIRECT_URL)


"""
        if layout.portfolio_version == 'portfolio_v1':
            return render(request, 'portfolio/portfolio_v1/base_v1.html', context)
        elif layout.portfolio_version == 'portfolio_v2':
            return render(request, 'portfolio/portfolio_v2/base_v2.html', context)
        elif layout.portfolio_version == 'portfolio_v3':
            return render(request, 'portfolio_v3/base_v3.html', context)
        elif layout.portfolio_version == 'portfolio_v4':
            return render(request, 'portfolio_v4/base_v4.html', context)
        else:
            messages.warning(request, "the site does not exist")
            return HttpResponseRedirect(DEFAULT_REDIRECT_URL)
"""

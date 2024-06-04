from django.shortcuts import render

# Create your views here.


def home(request, *args, **kwargs):
    context = {
        'title': 'public site',
        'name': 'home',
    }
    return render(
        request=request,
        template_name='website/index.html',
        context=context
        )


def about(request, *args, **kwargs):
    context = {
        'title': 'About Us',
        'name': 'about',
    }
    return render(
        request=request,
        template_name='website/about.html',
        context=context
        )


def contact_us(request, *args, **kwargs):
    context = {
        'title': 'Contact Us',
        'name': 'contact',
    }
    return render(
        request=request,
        template_name='website/contact.html',
        context=context
        )


def courses(request, *args, **kwargs):
    context = {
        'title': 'Our Courses',
        'name': 'courses',
    }
    return render(
        request=request,
        template_name='website/courses.html',
        context=context
        )


def pricing(request, *args, **kwargs):
    context = {
        'title': 'Fee ',
        'name': 'fee',
    }
    return render(
        request=request,
        template_name='website/pricing.html',
        context=context
        )


def teacher_view(request, *args, **kwargs):
    context = {
        'title': 'Our Teachers',
        'name': 'teacher',
    }
    return render(
        request=request,
        template_name='website/teacher.html',
        context=context
        )


def campus_maps(request, *args, **kwargs):
    context = {
        'title': 'Campus map',
        'name': 'maps',
    }
    return render(
        request=request,
        template_name='website/campus_map.html',
        context=context
        )

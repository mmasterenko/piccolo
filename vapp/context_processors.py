from pages.models import General


def general_info(req):
    info = General.objects.first()
    context = {
        'address': info.address,
        'phone': info.phone,
        'email': info.email
    }
    return context

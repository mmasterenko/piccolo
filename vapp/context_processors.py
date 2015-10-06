from pages.models import General


def general_info(req):
    info = General.objects.first()
    try:
        context = {
            'address': info.address,
            'phone': info.phone,
            'email': info.email
        }
    except AttributeError:
        context = {}
    return context

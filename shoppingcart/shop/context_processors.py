from .models import Category


def menu_links(request):
    """get menu links"""
    links = Category.objects.all()
    return dict(links=links)

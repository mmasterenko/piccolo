from vapp.models import Category, Assortiment
from django.core.urlresolvers import reverse


def get_assortiment_list(category_id, limit=None):
    if limit:
        assortiment_queryset = Assortiment.objects.filter(category_id=category_id).order_by('-id')[:limit]
    else:
        assortiment_queryset = Assortiment.objects.filter(category_id=category_id).order_by('-id')

    cookies, row, row_length = [], [], 3
    for assort in assortiment_queryset:
        d = {
            'img': assort.img.url,
            'name': assort.name.upper(),
            'pcs_weight': str(assort.weight).rstrip('0').rstrip('.'),
            'weight_units': assort.weight_units,
            'pcs_per_box': str(assort.pcs).rstrip('0').rstrip('.') if assort.pcs else '',
            'shelf_life': str(assort.days),
            'desc': assort.desc,
            'is_hit': assort.is_hit,
            'is_new': assort.is_new,
            'is_comingSoon': assort.is_comingSoon,
            'is_someFlag': assort.is_hit or assort.is_new or assort.is_comingSoon
        }
        row.append(d)
        if len(row) >= row_length:
            cookies.append(row)
            row = []
    if row:
        cookies.append(row)
    return cookies


def get_categories_list():
    category_queryset = Category.objects.order_by('order', 'id')
    return [dict(id=c.id, name=c.name.upper()) for c in category_queryset]


def get_news_url(n):
    return reverse('news', args=[n.url]) if n.url else reverse('news', args=[n.id])

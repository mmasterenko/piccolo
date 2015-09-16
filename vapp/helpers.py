from vapp.models import Category


def assortiment_queryset_to_structure(assortiment_queryset):
    cookies, row, row_length = [], [], 3
    for cookie in assortiment_queryset:
        d = {
            'img': cookie.img.url,
            'name': cookie.name.upper(),
            'pcs_weight': str(cookie.weight),
            'weight_units': cookie.weight_units,
            'pcs_per_box': str(cookie.pcs) if cookie.pcs else '--',
            'shelf_life': str(cookie.days)
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
    return [dict(id=c.id, name=c.name) for c in category_queryset]

from vapp.models import Category


def assortiment_queryset_to_structure(assortiment_queryset):
    cookies, row, row_length = [], [], 3
    for assort in assortiment_queryset:
        d = {
            'img': assort.img.url,
            'name': assort.name.upper(),
            'pcs_weight': str(assort.weight),
            'weight_units': assort.weight_units,
            'pcs_per_box': str(assort.pcs) if assort.pcs else '',
            'shelf_life': str(assort.days),
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

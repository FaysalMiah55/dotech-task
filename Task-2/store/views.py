from django.db.models import Sum, Count
from django.http import JsonResponse

from store.models import Category, Product


def get_top_categories(request):
    # Annotate categories with total_price and product_count
    annotated_categories = Category.objects.annotate(
        total_price=Sum('product__price'),
        product_count=Count('product')
    )

    # Filter and sort categories by total_price in descending order
    top_categories = annotated_categories.filter(total_price__isnull=False).order_by('-total_price')[:5]

    # Prepare result list of dictionaries
    result = [
        {"category_name": c.name, "total_price": c.total_price, "product_count": c.product_count}
        for c in top_categories
    ]
    context = {
        'top 5 categories': result
    }

    return JsonResponse(context)

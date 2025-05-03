from .models import Wishlist

def wishlist_counter(request):
    count = 0
    if request.user.is_authenticated:
        count = Wishlist.objects.filter(user=request.user).count()
    return dict(wishlist_count=count)

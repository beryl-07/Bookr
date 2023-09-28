from django.contrib.admin import AdminSite
from reviews.models import (Publisher, Contributor,
                            Book, BookContributor, Review)

class BookrAdminSite(AdminSite):
    site_header = 'Bookr Administration'
    site_title = 'Bookr Admin'
    index_title = 'Bookr Admin Home'

admin_site = BookrAdminSite(name='bookr')

# Register your models here.
admin_site.register(Publisher)
admin_site.register(Contributor)
admin_site.register(Book)
admin_site.register(BookContributor)
admin_site.register(Review)

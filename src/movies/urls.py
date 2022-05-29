from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewset)
router.register(r"directors", views.DirectorViewset)
router.register(r"movies", views.MovieViewset)

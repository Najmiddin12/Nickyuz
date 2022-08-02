from django.urls import path
from .views import home, SignUpModelView, SignInModelView, CreateAutoModelView, seller_kabinet, buyer_kabinet, buyer_detail, SigninModelView, autoday_gentra, autoday_nexia, autoday_malibu, autoday_equinox, autoday_trailblazer, autoday_traverse, nexia3_vs_gentra

urlpatterns = [
    path('', home, name="home"),
    path('autosale/signup/', SignUpModelView.as_view(), name="autosale-signup"),
    path('autosale/signup/signin', SigninModelView.as_view(), name="autosale-sign"),
    path('autosale/signin/', SignInModelView.as_view(), name="autosale-signin"),
    path('autosale/signin/buyer', buyer_kabinet, name="buyer-kabinet"),
    path('autosale/signin/buyer/<int:pk>/', buyer_detail, name="buyer-detail"),
    path('autosale/signin/create-auto/', CreateAutoModelView.as_view(), name="create-auto"),
    path('autosale/signin/create-auto/<int:pk>/', seller_kabinet, name="seller-kabinet"),
    path('autoday/gentra/', autoday_gentra, name="autoday-gentra"),
    path('autoday/nexia-3/', autoday_nexia, name="autoday-nexia"),
    path('autoday/malibu/', autoday_malibu, name="autoday-malibu"),
    path('autoday/equinox/', autoday_equinox, name="autoday-equinox"),
    path('autoday/trailblazer/', autoday_trailblazer, name="autoday-trailblazer"),
    path('autoday/traverse/', autoday_traverse, name="autoday-traverse"),
    path('autobattle/nexia3-vs-gentra/', nexia3_vs_gentra, name="nexia3-vs-gentra"),
]


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Cliphert Application API Documentation",
        default_version='v1',
        description="An online marketing site.",
        terms_of_service="",
        contact=openapi.Contact(email="shepardforsuh@gmail.com"),
        license=openapi.License(name="Software License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('', admin.site.urls),
    
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name="admin_password_reset"),
    
    path('admin/password_reset/done/', auth_views.PasswordChangeDoneView.as_view(), name="admin_password_reset_done"),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm',),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete',),

    path('api/', include('store.urls')),
    path('auth/', include('accounts.urls')),
    path('api/orders/', include('orders.urls')),
    
    url(r'^api_docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    url(r'^api_doc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

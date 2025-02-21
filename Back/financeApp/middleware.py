from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve

class DisableCSRFOnRegisterAndLoginMiddleware(MiddlewareMixin):
    def process_view(self, request, callback, callback_args, callback_kwargs): #Hace que el Token no sea requerio en estos endpoints
        resolved_path = resolve(request.path_info).route  # Obtiene la ruta sin el prefijo de la app
        if resolved_path in ['auth/login/', 'auth/register/'] and request.method == 'POST':
            setattr(request, '_dont_enforce_csrf_checks', True)
        return None
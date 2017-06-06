from django.shortcuts import render
from oauth2_provider.views import ProtectedResourceView, AuthorizationView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = "profile/profile.html"

    def get(self, request):
        user = request.user

        context = {
            "user": user
        }
        return render(
            request, self.template_name, context
        )


from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.request = request

        if self.request.user.is_authenticated():
            return super(LoginRequiredMixin, self).dispatch(self.request,
                                                                *args,
                                                                **kwargs)
        else:
            return super(LoginRequiredMixin, self).dispatch(
                request, *args, **kwargs)
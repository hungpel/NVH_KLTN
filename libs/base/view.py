class BaseViewMixin(object):
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

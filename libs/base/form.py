class BaseFormMixin(object):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

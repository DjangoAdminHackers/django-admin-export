import django.dispatch

pre_export = django.dispatch.Signal(providing_args=["queryset", ])

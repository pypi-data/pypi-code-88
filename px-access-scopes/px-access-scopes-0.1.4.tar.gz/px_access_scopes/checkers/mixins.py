class HasCallableMixin:
    def has(self, *a, **k) -> bool:
        raise NotImplemented('Implement `has` method. It\'s mandatory.')

    def __call__(self, *args, **kwargs) -> bool:
        return self.has(*args, **kwargs)

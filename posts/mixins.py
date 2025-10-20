class IsSuperUserMixin:
    def test_func(self) -> bool:
        return (
            self.request.user.is_superuser
        )
class MakeAllFieldsRequiredMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = True



class SearchFormMixin:
    query_param = "query"

    def get_context_data(
        self, *, object_list=None, **kwargs
    ):
        from common.forms import SearchForm

        kwargs.update(
            {
                "search_form": SearchForm(),
                "query": self.request.GET.get(self.query_param, ""),
            }
        )
        return super().get_context_data(object_list=object_list, **kwargs)


class IsSuperUserMixin:
    def test_func(self) -> bool:
        return (
            self.request.user.is_superuser
        )

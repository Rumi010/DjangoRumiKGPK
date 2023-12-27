class DataMixin:
    def get_user_context(self, **kwargs):
        """
        Метод для получения контекста данных, который вы хотите передать в шаблон.
        Здесь вы можете добавить любые данные, которые будут доступны в вашем шаблоне.
        """
        context = {
            'site_title': 'Мой сайт',
            'site_description': 'Описание моего сайта',
            **kwargs  # Вы можете передавать дополнительные аргументы в контекст
        }
        return context
from drivers import Context


class SubJob():

    def exec(self, context: Context):
        raise NotImplementedError

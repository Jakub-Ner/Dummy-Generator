class Stringify:
    @property
    def headers(self):
        ...

    def __str__(self):
        headers = self.headers.split(";")
        values = [getattr(self, header) for header in headers]
        acc = ""
        for value in values:
            acc += f"{value};"
        return acc[:-1]

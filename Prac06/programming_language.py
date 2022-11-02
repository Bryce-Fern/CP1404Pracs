class ProgrammingLanguage:

    def __init__(self, language="", dynamic="", reflection="", year=0):
        self.language = language
        self.dynamic = dynamic
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.dynamic == "Dynamic"

    def __str__(self):
        return f"{self.language}, {self.dynamic} Typing, Reflection={self.reflection}, First appeared in {self.year}"

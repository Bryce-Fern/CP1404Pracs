from Prac06.programming_language import ProgrammingLanguage
"""
Estimated time: 30m
Actual time: 40m
"""

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    print("The dynamic languages are:")
    languages = [python, ruby, visual_basic]
    for language in languages:
        if language.is_dynamic():
            print(language.language)


main()

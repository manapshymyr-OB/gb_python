"""3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}"""

def thesaurus(*names):
    results = {}
    for name in names:
        key = name[0].capitalize()
        if key not in results:
            results[key] = []
        results[key].append(name)
    return results

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
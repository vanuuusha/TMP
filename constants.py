CONSOLETEXT = 'Результат Ваших действий: '

DOCTOR_PROFESSIONS = ["Терапевт", "Окулист", "Ухо горло нос"]
DIAGNISIS = {
    DOCTOR_PROFESSIONS[0]: ['Диагноз 1', 'Диагноз 2'],
    DOCTOR_PROFESSIONS[1]: ['Диагноз 3', 'Диагноз 4'],
    DOCTOR_PROFESSIONS[2]: ['Диагноз 5', 'Диагноз 6'],
}

DIAGNISISLIST = []
for dig in DIAGNISIS.values():
    DIAGNISISLIST.extend(dig)

ADMINPASSWORD = '1'
MAXLENNAME = 20
MAXEXPERIENCE = 70
EXPLIST = [f'{i-10}-{i}' for i in range(10, MAXEXPERIENCE+10, 10)]
DEFAULTFONTCOLOR = "black"
DEFAULTFONT = "Arial 14"
DEFAULTBACKGROUNDCOLOR = 'blue'
DEFAULTHEIGHT = 3
DEFAULTKWARGSBUTTON = {'font': DEFAULTFONT, 'background': DEFAULTBACKGROUNDCOLOR, 'font_color': DEFAULTFONTCOLOR,
                       'height': DEFAULTHEIGHT}
DEFAULTKWARGSLABEL = {'font': DEFAULTFONT, 'font_color': DEFAULTFONTCOLOR, 'height': DEFAULTHEIGHT}
DEFAULTKWARGSENTRY = {'font': DEFAULTFONT, 'font_color': DEFAULTFONTCOLOR}
DEFAULTCOMBOBOX = {'font': DEFAULTFONT, 'font_color': DEFAULTFONTCOLOR}

CONSOLETEXT = 'Результат ваших действий: '

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
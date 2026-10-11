"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))
with open("students.csv", "rt") as f:
    next(f)

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)
    math_grades = 0
    python_grades = 0
    english_grades = 0
    students = 0
    best_student = None
    best_avr_grade = 0
    for line in f:
        line = line.strip().split(",")
        grades = [int(grade) for grade in line[1:]]
        name = line[0]


# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент
        math_grades += grades[0]
        python_grades += grades[1]
        english_grades += grades[2]
        students += 1
        average_grade = sum(grades)/len(grades)
        if average_grade > best_avr_grade:
            best_avr_grade = average_grade
            best_student = name
# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)
    math_average = math_grades / students
    python_average = python_grades / students
    english_average = english_grades / students



# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):

#     f.write("Середній бал по класу:\n")
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("Середній бал по класу:\n")
    f.write(f"math: {math_average:.1f}\n")
    f.write(f"python: {python_average:.1f}\n")
    f.write(f"english: {english_average:.1f}\n")
    f.write("\n")
    f.write(f"Найкращий студент: {best_student} ({best_avr_grade:.1f})\n")
print("Середній бал по класу:")
print(f"math: {math_average:.1f}")
print(f"python: {python_average:.1f}")
print(f"english: {english_average:.1f}")
print(f"Найкращий студент: {best_student} ({best_avr_grade:.1f})")


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.

import json
import os

ADOPT_FORMS_FILE = "database/adopt_forms.json"
MEET_FORMS_FILE = "database/meet_forms.json"

def save_form_data(filename: str, data: dict):
    forms = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                forms = json.load(f)
            except json.JSONDecodeError:
                pass
    forms.append(data)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(forms, f, ensure_ascii=False, indent=4)

def save_adopt_form(data: dict):
    save_form_data(ADOPT_FORMS_FILE, data)

def save_meet_form(data: dict):
    save_form_data(MEET_FORMS_FILE, data)

if __name__ == '__main__':
    # Приклад використання
    save_adopt_form({"name": "Іван", "contact": "+380...", "agreement": "Так"})
    save_meet_form({"animal": "Мурчик", "contact": "Telegram: @...", "time": "Завтра"})
    print("Дані форм збережено.")
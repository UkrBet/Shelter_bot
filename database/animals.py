import json

DATABASE_FILE = "database/animals.json"

def get_all_animals():
    try:
        with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('animals', [])
    except FileNotFoundError:
        print(f"Помилка: Файл {DATABASE_FILE} не знайдено.")
        return []
    except json.JSONDecodeError:
        print(f"Помилка: Не вдалося декодувати JSON з файлу {DATABASE_FILE}.")
        return []

def get_filtered_animals(filters: dict):
    animals = get_all_animals()
    filtered = []
    for animal in animals:
        match = True
        for key, value in filters.items():
            if key == 'vaccinated':
                if value == 'true' and not animal.get('vaccinated', False):
                    match = False
                    break
                elif value == 'false' and animal.get('vaccinated', False):
                    match = False
                    break
            elif key == 'sterilized':
                if value == 'true' and not animal.get('sterilized', False):
                    match = False
                    break
                elif value == 'false' and animal.get('sterilized', False):
                    match = False
                    break
            elif animal.get(key) != value:
                match = False
                break
        if match:
            filtered.append(animal)
    return filtered

if __name__ == '__main__':
    # Приклад використання (потрібно створити animals.json)
    # з таким форматом: {"animals": [{"id": 1, "name": "...", ...}, {...}]}
    all_animals = get_all_animals()
    print("Усі тварини:", all_animals)

    filtered = get_filtered_animals({"type": "Кіт", "vaccinated": "true"})
    print("Відфільтровані коти (вакциновані):", filtered)
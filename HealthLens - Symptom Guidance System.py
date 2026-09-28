# HealthLens - Symptom Guidance System

import os

# list of symptoms 
symptoms = [
    "Cough", "Runny nose", "Sneezing", "Sore throat", "Fever",
    "Headache", "Body ache", "Fatigue", "Chills",
    "Nausea", "Vomiting", "Diarrhea", "Stomach pain", "Loss of appetite",
    "Itchy eyes", "Watery eyes", "Red eyes",
    "Skin rash", "Itchy skin",
    "Joint pain", "Muscle pain", "Stiffness",
    "Frequent urination", "Burning urination",
    "Dizziness", "Loss of smell", "Loss of taste", "Severe chest pain", "Trouble breathing", "Fainting", "Severe allergic reaction"
    
]

# to group similar sympptoms
symptom_category = {
    "Cough": "Respiratory", "Runny nose": "Respiratory", "Sneezing": "Respiratory",
    "Sore throat": "Respiratory", "Fever": "General", "Headache": "General",
    "Body ache": "General", "Fatigue": "General", "Chills": "General",
    "Nausea": "Digestive", "Vomiting": "Digestive", "Diarrhea": "Digestive",
    "Stomach pain": "Digestive", "Loss of appetite": "Digestive",
    "Itchy eyes": "Eye", "Watery eyes": "Eye", "Red eyes": "Eye",
    "Skin rash": "Skin", "Itchy skin": "Skin",
    "Joint pain": "Muscle/Joint", "Muscle pain": "Muscle/Joint", "Stiffness": "Muscle/Joint",
    "Frequent urination": "Urinary", "Burning urination": "Urinary",
    "Dizziness": "General", "Loss of smell": "General", "Loss of taste": "General",
}

# serious symptoms
serious_symptoms = [
    "Severe chest pain", "Trouble breathing", "Fainting", "Severe allergic reaction"
]



conditions = {
    "COMMON COLD": {
        "category": "Respiratory",
        "symptoms": ["Cough", "Runny nose", "Sneezing", "Sore throat", "Fatigue"],
        "description": "A mild viral infection of the nose and throat.",
        "advice": "Drink fluids and rest. Usually goes away in about a week.",
    },
    "FLU": {
        "category": "Respiratory",
        "symptoms": ["Fever", "Body ache", "Chills", "Fatigue", "Cough", "Headache"],
        "description": "A viral infection that affects the whole body.",
        "advice": "Rest, drink fluids, and see a doctor if it gets worse.",
    },
    "ALLERGY": {
        "category": "Respiratory",
        "symptoms": ["Sneezing", "Runny nose", "Itchy eyes", "Watery eyes"],
        "description": "Reaction to dust, pollen, or other allergens.",
        "advice": "Avoid the allergen if you know what it is. Antihistamines can help.",
    },
    "SINUS INFECTION": {
        "category": "Respiratory",
        "symptoms": ["Headache", "Runny nose", "Fatigue", "Cough"],
        "description": "Swelling of the sinuses, often after a cold.",
        "advice": "Steam and rest usually help. See a doctor if it lasts long.",
    },
    "MIGRAINE": {
        "category": "General",
        "symptoms": ["Headache", "Nausea", "Dizziness"],
        "description": "A strong headache, sometimes with nausea and light sensitivity.",
        "advice": "Rest in a dark quiet room. See a doctor if migraines happen often.",
    },
    "DEHYDRATION": {
        "category": "General",
        "symptoms": ["Headache", "Dizziness", "Fatigue"],
        "description": "Not enough water in the body.",
        "advice": "Drink water and electrolytes.",
    },
    "FOOD POISIONING": {
        "category": "Digestive",
        "symptoms": ["Nausea", "Vomiting", "Diarrhea", "Stomach pain", "Fever"],
        "description": "Illness caused by eating contaminated food.",
        "advice": "Drink fluids to avoid dehydration. See a doctor if it does not improve.",
    },
    "INDIGESTION": {
        "category": "Digestive",
        "symptoms": ["Stomach pain", "Nausea", "Loss of appetite"],
        "description": "Discomfort in the stomach, usually after eating.",
        "advice": "Eat smaller meals and avoid oily food.",
    },
    "GASTROENTERITIS": {
        "category": "Digestive",
        "symptoms": ["Diarrhea", "Vomiting", "Stomach pain", "Fever"],
        "description": "Infection of the stomach and intestines.",
        "advice": "Drink fluids. See a doctor if symptoms are severe.",
    },
    "CONJUCTIVITIES (PINK EYE)": {
        "category": "Eye",
        "symptoms": ["Red eyes", "Itchy eyes", "Watery eyes"],
        "description": "Infection or irritation of the eye surface.",
        "advice": "Keep hands away from eyes and keep them clean.",
    },
    "SKIN ALLERGY": {
        "category": "Skin",
        "symptoms": ["Skin rash", "Itchy skin"],
        "description": "Skin reaction to something that touched it.",
        "advice": "Avoid the trigger and keep the skin moisturized.",
    },
    "MUSCLE STRAIN": {
        "category": "Muscle/Joint",
        "symptoms": ["Muscle pain", "Stiffness", "Joint pain"],
        "description": "Overuse or stretching of a muscle.",
        "advice": "Rest the area and use ice if it is swollen.",
    },
    "URINARY TRACT INFECTION": {
        "category": "Urinary",
        "symptoms": ["Frequent urination", "Burning urination", "Fever", "Stomach pain"],
        "description": "Infection in the urinary tract, usually bacterial.",
        "advice": "See a doctor, this usually needs medicine to treat.",
    },
    "COVID LIKE ILLNESS": {
        "category": "Respiratory",
        "symptoms": ["Fever", "Cough", "Fatigue", "Loss of smell", "Loss of taste"],
        "description": "A viral illness with a wide range of symptoms.",
        "advice": "Rest, isolate if possible, and monitor your symptoms.",
    },
}


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    print("=" * 50)
    print("          🩺  HEALTHLENS - Symptom Checker")
    print("=" * 50)
    print()


def show_menu():
    print("1. Check Symptoms")
    print("2. Browse Symptom List")
    print("3. Condition Info")
    print("4. About")
    print("5. Exit")


def get_choice(low, high):
    while True:
        value = input("Enter your choice: ")
        if value.isdigit() and low <= int(value) <= high:
            return int(value)
        print("Invalid input, please enter a number between", low, "and", high)


def print_symptom_list():
    for i in range(len(symptoms)):
        print(str(i + 1) + ". " + symptoms[i])


def select_symptoms():
    print("\nHere is the list of symptoms:\n")
    print_symptom_list()
    print("\nEnter the numbers of the symptoms you have, separated by commas")
    print("Example: 1,4,6")

    user_input = input("Your symptoms: ")
    parts = user_input.split(",")

    chosen = []
    for part in parts:
        part = part.strip()
        if part.isdigit():
            num = int(part)
            if 1 <= num <= len(symptoms):
                name = symptoms[num - 1]
                if name not in chosen:
                    chosen.append(name)
            else:
                print("Skipping " + part + ", not a valid number")
        else:
            if part != "":
                print("Skipping " + part + ", not a number")

    return chosen


# counts how many symptoms match between user list and condition list
def count_matches(user_symptoms, condition_symptoms):
    count = 0
    for s in user_symptoms:
        if s in condition_symptoms:
            count += 1
    return count


def check_symptoms():
    chosen = select_symptoms()

    if len(chosen) == 0:
        print("No symptoms selected.")
        return

    print("\nYou selected:")
    for s in chosen:
        print("- " + s)

    # check for serious symptoms first
    for s in chosen:
        if s in serious_symptoms:
            print("\n*** WARNING ***")
            print("You selected a serious symptom:", s)
            print("Please see a doctor immediately, this program cannot help with that.")

    print("\nAnalyzing your symptoms...\n")

    results = []
    for name in conditions:
        info = conditions[name]
        matched = count_matches(chosen, info["symptoms"])
        total = len(info["symptoms"])

        if matched >= 2:
            percent = (matched / total) * 100
            results.append((name, matched, total, percent))

    
    results.sort(key=lambda x: x[3], reverse=True)

    if len(results) == 0:
        print("No good match found in the database.")
        print("If symptoms continue, please consult a doctor.")
    else:
        for r in results:
            name, matched, total, percent = r
            if percent >= 70:
                level = "High"
            elif percent >= 40:
                level = "Medium"
            else:
                level = "Low"

            print(name + " -> matched " + str(matched) + "/" + str(total) +
                  " symptoms (" + level + " match)")

        print("\nNote: This is only a possible match based on symptoms.")
        print("It is NOT a diagnosis. Please consult a doctor for anything serious.")


def browse_symptoms():
    categories = {}
    for s in symptoms:
        cat = symptom_category[s]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(s)

    for cat in categories:
        print("\n" + cat + ":")
        for s in categories[cat]:
            print("  - " + s)


def condition_info():
    names = list(conditions.keys())
    print()
    for i in range(len(names)):
        print(str(i + 1) + ". " + names[i])

    choice = get_choice(1, len(names))
    name = names[choice - 1]
    info = conditions[name]

    print("\n" + name)
    print("Category: " + info["category"])
    print("Description: " + info["description"])
    print("Symptoms: " + ", ".join(info["symptoms"]))
    print("Advice: " + info["advice"])


def about():
    print("\nHealthLens - Symptom Guidance System")
    print("A simple college project made in Python.")
    print("It compares the symptoms you enter with a small built-in")
    print("database of common conditions and shows how many symptoms match.")
    print("This is only for learning purposes and is NOT a medical tool.")


def main():
    while True:
        clear_screen()
        show_banner()
        show_menu()
        choice = get_choice(1, 5)
        print()

        if choice == 1:
            check_symptoms()
        elif choice == 2:
            browse_symptoms()
        elif choice == 3:
            condition_info()
        elif choice == 4:
            about()
        elif choice == 5:
            print('Wishing you good health and a speedy recovery. Stay Well!')
            print("Thank You for using HealthLens.")
            break

        input("\nPress Enter to go back to menu...")


if __name__ == "__main__":
    main()
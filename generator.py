import json
import argparse
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent / "templates"

def load_templates():
    templates = {}
    for file in TEMPLATES_DIR.glob("*.json"):
        with file.open("r", encoding="utf-8") as f:
            data = json.load(f)
            for scenario in data.get("scenarios", []):
                key = f"{file.stem}:{scenario['id']}"
                templates[key] = scenario
    return templates

def list_scenarios(templates):
    for key, scenario in templates.items():
        name_zh = scenario["name"].get("zh", "")
        name_en = scenario["name"].get("en", "")
        name_fr = scenario["name"].get("fr", "")
        print(f"{key} | 中文: {name_zh} | EN: {name_en} | FR: {name_fr}")

def generate_reply(templates, scenario_key, lang):
    if scenario_key not in templates:
        print(f"Scenario '{scenario_key}' not found.")
        return
    scenario = templates[scenario_key]
    template = scenario["templates"].get(lang)
    if not template:
        print(f"No template for language '{lang}' in scenario '{scenario_key}'.")
        return
    print(template)

def main():
    parser = argparse.ArgumentParser(description="Multi-language CS reply generator for QSR/retail.")
    parser.add_argument("--list", action="store_true", help="List all available scenarios.")
    parser.add_argument("--scenario", type=str, help="Scenario key, e.g. 'complaints:late_order'.")
    parser.add_argument("--lang", type=str, choices=["zh", "en", "fr"], help="Language: zh/en/fr.")
    args = parser.parse_args()

    templates = load_templates()

    if args.list:
        list_scenarios(templates)
        return

    if not args.scenario or not args.lang:
        print("Usage examples:")
        print("  python generator.py --list")
        print("  python generator.py --scenario complaints:late_order --lang zh")
        return

    generate_reply(templates, args.scenario, args.lang)

if __name__ == "__main__":
    main()

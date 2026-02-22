import json
from difflib import get_close_matches

with open("addresses.json", "r", encoding="utf-8") as f:
    DB = json.load(f)

def validate_address(city, zip_code):
    if city not in DB:
        suggestions = get_close_matches(city, DB.keys(), n=3, cutoff=0.6)
        return {
            "valid": False,
            "reason": "Unknown city",
            "suggestions": suggestions
        }

    if zip_code not in DB[city]:
        return {
            "valid": False,
            "reason": "ZIP does not match city",
            "suggestions": DB[city]
        }

    return {"valid": True, "reason": "OK"}

# quick test
if __name__ == "__main__":
    print(validate_address("Jihlvaa", "58601"))
    print(validate_address("Jihlava", "99999"))
    print(validate_address("Žďár nad Sázavou", "59101"))

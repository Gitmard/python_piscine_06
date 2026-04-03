#!/usr/bin/python3

from alchemy.grimoire import light_spell_record

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    light_spell_recor_result = light_spell_record(
        "Fantasy",
        "earth air fire"
    )

    print(
        f"Testing record light spell: {light_spell_recor_result}"
    )

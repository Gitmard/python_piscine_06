#!/usr/bin/python3

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    import alchemy.grimoire.dark_spellbook
    light_spell_recor_result = (
        alchemy.grimoire.dark_spellbook.dark_spell_record(
            "Aweful",
            "eyeball"
        )
    )

    print(
        f"Testing record light spell: {light_spell_recor_result}"
    )

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid: bool

    for ingredient in ingredients.split():
        if ingredient in dark_spell_allowed_ingredients():
            valid = True
        else:
            valid = False
            break

    return (
        f"{ingredients}: VALID"
        if valid
        else f"{ingredients} INVALID"
    )

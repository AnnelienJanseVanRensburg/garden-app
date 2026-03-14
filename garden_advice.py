def get_user_input():
    """Prompt the user for season and plant type, and return both values."""
    season = input("Enter the season: ")
    plant_type = input("Enter the type of plant (flower or vegetable): ")
    return season, plant_type


def get_season_advice(season):
    """Return gardening advice based on the given season."""
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
    }
    return season_advice.get(season, "No advice for this season.")


def get_plant_advice(plant_type):
    """Return gardening advice based on the given plant type."""
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
    }
    return plant_advice.get(plant_type, "No advice for this type of plant.")


def generate_advice(season, plant_type):
    """Combine season and plant type advice into a single message."""
    season_advice = get_season_advice(season)
    plant_advice = get_plant_advice(plant_type)
    return f"{season_advice}\n{plant_advice}"


def main():
    """Main entry point: collect input, generate advice, and display it."""
    season, plant_type = get_user_input()
    advice = generate_advice(season, plant_type)
    print(advice)


main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.

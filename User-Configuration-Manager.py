test_settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}


def add_setting(settings, new_setting):
    # Basic validation
    if not isinstance(settings, dict):
        raise TypeError("settings must be a dict")
    if not (isinstance(new_setting, tuple) and len(new_setting) == 2):
        raise TypeError("new_setting must be a 2-item tuple (key, value)")

    key = str(new_setting[0]).lower()
    value = str(new_setting[1]).lower()

    if any(existing_key.lower() == key for existing_key in settings.keys()):
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, updated_setting):
    key = str(updated_setting[0]).lower()
    value = str(updated_setting[1]).lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, setting_key):
    key = str(setting_key).lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")
    return "\n".join(lines) + "\n"

print(view_settings({}))
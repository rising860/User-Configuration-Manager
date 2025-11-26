# User-Configuration-Manager

User Configuration Manager that allows users to manage their settings such as theme, language, and notifications.

This repository provides a small Python module that implements helper functions for managing user settings.

Implemented functions

- `add_setting(settings, new_setting)`

  - Adds a new setting (key, value) pair to `settings` (a dict).
  - Both key and value are converted to lowercase strings before storing.
  - If the key already exists (case-insensitive), the function returns the message:
    - `Setting '[key]' already exists! Cannot add a new setting with this name.`
  - If the key does not exist, it stores the key/value (lowercased) and returns:
    - `Setting '[key]' added with value '[value]' successfully!`

- `update_setting(settings, updated_setting)`

  - Updates an existing setting. Key/value are converted to lowercase before updating.
  - Returns a success or an informative failure message.

- `delete_setting(settings, setting_key)`

  - Deletes a setting by key (case-insensitive). Returns a success message or `Setting not found!`.

- `view_settings(settings)`
  - Returns a formatted view of current settings.
  - If the dictionary is empty, it returns exactly: `No settings available.`

Example usage

```python
from User_Configuration_Manager import add_setting, update_setting, delete_setting, view_settings

settings = {"theme": "light"}

print(add_setting(settings, ("Theme", "Dark")))
# -> "Setting 'theme' already exists! Cannot add a new setting with this name."

print(add_setting(settings, ("font_size", 12)))
# -> "Setting 'font_size' added with value '12' successfully!"

print(view_settings(settings))
# -> Displays the keys and values (or 'No settings available.' when empty)
```

Notes

- Keys and values are stored as lowercase strings by the current implementation.
- The module file includes a small demo / self-check when run directly.

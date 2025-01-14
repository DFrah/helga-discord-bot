import json
import os
from typing import List

# Config path
_config_path = 'config/config.json'

# Config object
_config = {}
_config_default = {
  "Games": [
    {
      "Game": "Ratchet: Deadlocked",
      "Color": "0xFF0000",
      "Filters": [
        "#ratchetdeadlocked",
        "Deadlocked"
      ]
    },
    {
      "Game": "Ratchet and Clank: Up Your Arsenal",
      "Color": "0xFFFF00",
      "Filters": [
        "UYA",
        "Up Your Arsenal"
      ]
    }
  ],
  "Stats": {
    "GuildIds": []
  },
  "TipOfTheDay": {
    "Path": "tipoftheday.txt",
    "ChannelId": 0,
    "Color": "0xAA0000",
    "Thumbnail": None
  },
  "Smoke": [
    {
      "Enabled": False,
      "Name": None,
      "ChannelId": 0,
      "MessageId": 0,
      "Thumbnail": None,
      "Color": None,
      "API": "",
      "AppIds": {},
      "Servers": [],
      "Interval": 10,
      "Rulesets": {},
      "Levels": {},
      "Icons": [
        {
          "Field": "GenericField6",
          "Mask": 0,
          "Emoji": None
        }
      ],
      "SubIcons": [
        {
          "Field": "GenericField6",
          "Mask": 0,
          "Emoji": None
        }
      ]
    }
  ]
}

# loads configuration from the config file
def config_load():
  global _config
  global _config_default

  # initialize with defaults
  _config.update(_config_default.copy())

  # if config file doesn't exist, create new with defaults
  if os.path.exists(_config_path):
    print("Found a config file!!! ")
    with open(_config_path, 'r') as f:
      _config.update(json.load(f))
  else:
    print("No config found!")
    config_save()

# saves configuration to config file
def config_save():
  global _config
  global _config_default

  config_json = json.dumps(_config, indent=4)
  if not os.path.exists('./config'):
    os.makedirs('./config')
  with open(_config_path, 'w') as w:
    w.write(config_json)

# returns the config value at path
def config_get(path: List[str]):
  global _config
  global _config_default

  item = _config
  for field in path:
    if field not in item:
      return None
    item = item[field]

  return item

def config_get_full():
  global _config
  return _config
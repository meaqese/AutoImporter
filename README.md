# AutoImporter [![Codacy Badge](https://api.codacy.com/project/badge/Grade/7cc3b5746b3d4c2b8bfe964dfbe47c14)](https://app.codacy.com/manual/meaqese/AutoImporter?utm_source=github.com&utm_medium=referral&utm_content=meaqese/AutoImporter&utm_campaign=Badge_Grade_Dashboard) [![Build Status](https://travis-ci.com/meaqese/AutoImporter.svg?branch=master)](https://travis-ci.com/meaqese/AutoImporter)
## What is it?
Tool that can import all preprocessor files to single file.

## How to use?
### Syntax
```python autoimporter.py path_to_config```

**path_to_config** - YAML file there are import settings

### How to create config file?
1. Create any file with .yaml extension (e.g.: config.yaml (logical))
2. Configurate this config file.  
  **import** (list) - less file paths which need to import to styles.  
  **destination** (str) - preprocessor styles file, where will be all imports
3. That's all! Congratulations 🎉

### Example
#### Config file (in sandbox/config.yaml)
```
import: [blocks/*/**, blocks/*] 
destination: styles.scss
```
#### Command 
```python autoimporter.py sandbox/config.yaml```
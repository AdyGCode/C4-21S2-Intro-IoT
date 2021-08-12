# Session 05

Session 5 content summary

## Requirements

Any requirements for this session

## Adding Plugins to Pycharm

The lecturers use a variety of plugins with PyCharm. These include the following:

| Plugin Name | Purpose |
|-------------|-----------------------------------------|
| .ignore | Used to create "ignore" files for Git and other systems. |
| Atom Material Icons | Adds more meaningful icons to the project and file navigation areas |
| CSV | Used to easing work with Comma Separated Variable files |
| Material Theme UI Lite | A Theming system with many customisation options |
| Extra Icons | Additional icons for use with file types and more |
| .env | For working with `.env` files |
| Rainbow Brackets | Highlights brackets in colour |
| Requirements | USed for working with `requirements.txt` files |


## Adding a standardised heading to Python files

- Open PyCharm (Community or professional) and open any PyCharm project.
- Press CTRL+ALT+S to open the settings for PyCharm
- Locate the **Editor** item and expand it in the side-bar (the triangle/plus/or similar symbol)
- Click on **File and Code Templates**
- Click on **Includes** tab (by default no files will be shown)
- Click on the **+** to add a new file
- Type in the name of the file, in this case `header`
- Now paste in the following code: 
```python
# ---------------------------------------------------------------------
# Filename      : ${FILE_NAME}
# Location      : ./${DIR_PATH}
# Project       : ${PROJECT_NAME}
# Author        : YOUR NAME <YOUR EMAIL ADDRESS>
# Created       : ${DATE}
# Version       : 0.1
# Description   :
#   This is a description of what the file is for
#
# ---------------------------------------------------------------------
```
- Click Apply
- Now click the **Files** tab
- Select the Python Script option and add the following code
```python
#parse("header.py") 
```
- Click Apply and then OK

Now every file you create will have a standardised heading.

**Aside:** *You may add the parse line as the first line in the Python Stub, Python Unit Test and Flask Main options if you wish.*

# Session 05

Session 5 content summary

## Requirements

Any requirements for this session

## ...

Add headings and content as required

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

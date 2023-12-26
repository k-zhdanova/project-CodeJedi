# CodeJedi project

**Welcome to the Galactic Address Book, your guide in the vast universe of contacts.
💫 May the Force be with you.**

1. **Installation**

To install the Galactic Address Book directly from the local path, follow these steps:
Navigate to the project's root directory and run:


```bash
pip3 install /path/to/your/project
```

Replace `/path/to/your/project` with the actual path to your project directory, for example, `/Users/go_it/python/final_project`.

This command installs the package including any dependencies listed in setup.py.

2. **Running**
After installation you can launch the app from any place using the command:

```bash
python3 -m codejedi.main
```

3. **Development**

Initiate local virtual environment:
```bash
python3 -m venv .env
```
    
Install dependencies:
    
```bash
pip install -r requirements.txt
```

To activate, run:

```
source .env/bin/activate
```
4. **Menu**

```
 - 🌟 hello: Greet the bot
 - 🌟 all: Get all contacts
 - 🌟 add: Add a new contact
 - 🌟 add_phone: Add a new phone
 - 🌟 add_tag: Add a new tag
 - 🌟 edit: Editing existing contacts
 - 🌟 delete: Delete an existing contact
 - 🌟 show-birthday: Shows upcoming birthdays for given period
 - 🌟 birthdays: Show contacts with birthdays next period
 - 🌟 help: Show all available commands
 - 🌟 exit: Exit the assistant bot
 - 🌟 close: Exit the assistant bot
 - 🌟 bye: Exit the assistant bot
```
5. **Usage:**

    Type a command from Menu:
  
  ```
  all, add, add_phone, add_tag, edit, delete, help, exit, close, bye
  ```
  
  **all:**  No aditional actions required
  
  **add:** User will be prompted to input:
  
  - name [required field]
  
  - phone [required field]
  
  - address [optional field]
  
  - email [optional field]
  
  - birthday [optional field]
  
  **add_phone:** Phone number ir required
  
  **add_tag:** Tag is required
  
  **edit:** User will be prompted to input:
  - field to edit
  - new value
  
 
 if _field to edit_ is phone: 
  - old phone 
  - new value
  
  **delete:** User will be prompted to input:
  - name [required]

  **show-birthday:** User will be prompted to input:
  - name [required]

  **birthdays:**
  - days [required]

**help:** No aditional actions required

**exit:** No aditional actions required

**close:** No aditional actions required

**bye:** No aditional actions required  

---
  
**💫 Farewell, and may the Force be with you always.**
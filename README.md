# Commit Complimenter 

_adds positivity to commits._

This project provides a simple Python script designed to run as a Git hook on Windows. It checks your commit message for signs of potential frustration or negativity (by looking for specific keywords) and, if detected, automatically appends a random compliment or positive message before the commit is finalized.

I got really bored at night and made this

## Features

* Analyzes commit messages for configurable "negative" keywords.
* Appends a random compliment from a list when triggered.
* Runs automatically as a `commit-msg` Git hook.
* Easy to customize the compliments and trigger keywords.
* Specifically set up for Windows environments.

## Prerequisites

* **Git:** You need Git installed on your Windows machine.
* **Python:** You need Python installed on your Windows machine and added to your system's PATH. You can verify this by typing `python --version` in Command Prompt.
* **A Git Repository:** You need a local Git repository where you want to install this hook.

## Installation (Windows)

Follow these steps to install the Commit Complimenter in a specific Git repository:

1.  **Save the Python Script:**
    * Download the `commit_complimenter.py` file from this repository.
    * Save this file to a **permanent** location on your computer. This location should **not** be inside the `.git` folder of your repository, as `.git` contents are not typically meant for user scripts and are not part of the repository's tracked files. A good place might be a dedicated scripts folder like `C:\Users\YourUsername\Scripts\CommitComplimenter\`.
    * **Make a note of the full path** to where you saved `commit_complimenter.py`.

2.  **Navigate to Your Repository's Hooks Directory:**
    * Open Command Prompt or File Explorer and go to the root directory of your Git repository.
    * Navigate into the hidden `.git` folder, and then into the `hooks` folder. For example, `C:\Path\To\Your\Repo\.git\hooks`.

3.  **Create the Git Hook File:**
    * Inside the `.git\hooks` folder, create a new text file named `commit-msg.bat`. **It's important to use the `.bat` extension on Windows for reliable execution across different command line environments (CMD, PowerShell, Git Bash).**

4.  **Edit the Hook File:**
    * Open the `commit-msg.bat` file in a text editor (like Notepad, VS Code, etc.).
    * Add the following line to the file:

    ```batch
    @echo off
    "C:\Path\To\Your\script\commit_complimenter.py" %1
    ```

    * **Replace `"C:\Path\To\Your\script\commit_complimenter.py"`** with the **actual, full path** to the `commit_complimenter.py` file you saved in Step 1. Make sure the path is enclosed in double quotes if it contains spaces.
    * `%1` is a placeholder that Git automatically replaces with the path to the temporary commit message file when the hook runs.

5.  **Permissions (Usually Automatic):**
    * On Windows, `.bat` files are executable by default, so you typically don't need to manually set permissions.

6.  **You're Done!**
    * The hook is now active for this specific Git repository.

## Usage

1.  Make changes to files in your repository.
2.  Stage your changes (`git add .`).
3.  Start a commit (`git commit`). This will open your default Git commit message editor.
4.  Write your commit message. If your message includes any of the keywords defined in the `negative_keywords` list in the Python script (like "fix", "bug", "failed", etc. - case-insensitive), the hook will trigger.
5.  Save and close the editor.

If triggered, the script will append a random compliment to your message before the commit is finalized. You can verify this by looking at the commit log (`git log`).

## Customization

You can easily customize the script:

1.  Open the `commit_complimenter.py` file in a text editor (the file you saved in Step 1).
2.  Modify the `compliments` list to add, remove, or change the compliments.
3.  Modify the `negative_keywords` list to change the words that trigger a compliment (remember to use lowercase).
4.  You can also adjust the separator string (`"✨ Commit Complimenter Says: "`) if you like.
5.  Save the `commit_complimenter.py` file. Changes will take effect on your next commit in any repository where the hook is installed.

## Uninstallation

To remove the Commit Complimenter from a repository:

1.  Navigate to the `.git\hooks` directory of that repository.
2.  Delete the `commit-msg.bat` file.

The hook is now inactive for that repository.

## Contributing

Ideas for improvement, more compliments, better keyword detection, or just fixing typos are welcome, I really dont care. Feel free to fork the repository and open a pull request.

# HealthLens - Symptom Guidance System

## Overview
HealthLens is a simple Python console program made as a college mini
project. The user picks the symptoms they are feeling from a list, and
the program compares them with a small built-in database of common
conditions to show how many symptoms match.

This project is only for learning purposes. It does **not** give a real
diagnosis.

## Problem Statement
Sometimes people have a few symptoms and just want a quick idea of what
it could be related to (like a cold, allergy, or upset stomach) before
deciding if they should see a doctor. HealthLens is a basic version of
that idea, built using simple Python logic.

## Objectives
- Practice using lists, dictionaries, and loops in Python
- Practice writing functions and splitting a program into parts
- Practice taking and validating user input
- Build something that runs fully in the terminal

## Features
- Check Symptoms: pick multiple symptoms and see which conditions match
- Browse Symptom List: view all symptoms grouped by category
- Condition Info: pick a condition and read more about it
- About section
- Warns the user if a serious symptom is selected
- Handles wrong input (letters, out of range numbers, etc.) without crashing

## Technology Used
Python 3 (only the built-in `os` module, nothing else needed)

## How the Matching Works
1. Each condition in the `conditions` dictionary has its own list of
   symptoms.
2. When the user picks their symptoms, the program checks how many of
   them are also in a condition's symptom list using `count_matches()`.
3. If at least 2 symptoms match, it calculates a percentage:
   `matched symptoms / total symptoms of that condition * 100`
4. Based on the percentage, it labels the result High, Medium, or Low
   match.
5. All matching conditions are shown, sorted from highest to lowest
   match percentage.
6. If nothing matches well, it tells the user no good match was found.

## How to Run
1. Make sure Python 3 is installed.
2. Run this command in the terminal:
   ```
   python3 healthlens.py
   ```
3. Use the menu numbers to navigate.

## Example
```
Choose: 1 (Check Symptoms)
Enter: 1,3,4,8   (Cough, Sneezing, Sore throat, Fatigue)

Output:
Common Cold -> matched 4/5 symptoms (High match)
Allergy -> matched 2/4 symptoms (Medium match)
```

## Limitations
- The condition list is small and only for common, everyday illnesses
- It only checks symptom overlap, it does not know about severity, age,
  or medical history
- Not accurate enough for real medical use

## Disclaimer
HealthLens is a college project for practicing Python. It is not a
medical tool and should not be used to actually diagnose or treat
anything. Please see a real doctor for any health concerns.

## Future Improvements
- Add more conditions and symptoms
- Save results to a file
- Maybe add a simple GUI later



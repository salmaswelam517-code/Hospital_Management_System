# Hospital Management System

A simple system built with Python and a modern GUI using `customtkinter` to manage hospital operations efficiently and in an organized manner.

## Project Idea
Building a simple system for hospital management to organize and structure each patient's data individually for easy medical follow-up and to prevent crowding and scheduling conflicts.

## Key Features & Characteristics
* **Patient Data Management:** Storing and organizing patient details (Name, Age, Disease, ID, assigned Doctor, and number of visits) using Python Dictionaries.
* **Patient-Doctor Linking:** Connecting patients with their respective doctors to facilitate medical follow-up and track health stability.
* **New Patient Registration:** System protection against errors, preventing data conflicts or duplication by checking if the ID already exists using `try / except` blocks.
* **Search Engine:** Quick search functionality to find patients easily using either their Name or ID.
* **Appointment Scheduling:** Precise scheduling to avoid overlaps and crowding.
* **Data Persistence:** Automatic saving and loading of patient data using `JSON` format.
* **Graphical User Interface (GUI):** A modern and user-friendly interface built with `customtkinter`.

## How to Run
1. Make sure Python is installed on your device.
2. Install the required libraries via the Terminal using the following command:
   ```bash
   pip install -r requirements.txt
3. Run the project using the main execution file:
   ```bash
   python main.py
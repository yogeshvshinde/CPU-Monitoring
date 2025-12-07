Steps to perform
===================================

Create a python virtual environment
command : python3 -m venv .venv

install psutil utility ( direct installtion)

command : pip install -r requirements.txt (Using requirements.txt file )

Command to install the psutil python library 

command: pip install psutil

====================================
How it works:

1. psutil.cpu_percent(interval=1)

Measures CPU usage over 1 second

Returns value like 45.3 or 92.0

2. Infinite loop (while True:)

Keeps checking CPU usage continuously until you stop it manually.

3. Threshold check

If CPU usage goes above 80%, it prints an alert.

4. Error Handling

KeyboardInterrupt → Gracefully exits when you press Ctrl + C

General Exception → Catches unexpected errors and prints them

==========================================================

Output Screenshot

<img width="518" height="115" alt="image" src="https://github.com/user-attachments/assets/09993a62-e8e5-4b70-9ba3-3ba8e9c50fc2" />







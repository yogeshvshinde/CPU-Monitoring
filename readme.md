How the Program Works
===================================

install psutil utility ( direct installtion)

pip install -r .\requirements.txt (Using requirements.txt file )

Command to install the psutil python library 

pip install psutil

====================================
code:

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




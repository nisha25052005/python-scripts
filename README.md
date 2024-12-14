## System Health Monitoring Script
### Description
This script monitors the health of the system by checking CPU, memory, and disk usage. If any of these metrics exceed defined thresholds, an alert message is printed. The script continuously monitors the system health every 10 seconds.

#### Prerequisites
Python: Ensure you have Python installed.
psutil library: Install the psutil library for accessing system metrics.

`pip install psutil`
##### Usage
Download the Script: Copy and save the script as system_health_monitor.py.
Set Thresholds (Optional): Adjust CPU_THRESHOLD, MEMORY_THRESHOLD, and DISK_THRESHOLD values to desired levels.

###### Run the Script:
Open a terminal in the directory containing system_health_monitor.py.

Run the script:
`python system_health_monitor.py`

##### Monitoring: 
The script will output system health information every 10 seconds, displaying alerts if usage exceeds the set thresholds.

##### Script Details
CPU Usage: Checks current CPU usage and alerts if it exceeds CPU_THRESHOLD.
Memory Usage: Checks memory usage and alerts if it exceeds MEMORY_THRESHOLD.
Disk Usage: Checks disk usage on the root directory (/) and alerts if it exceeds DISK_THRESHOLD.


===================================================================================


# Application Health Checker Script
# Description
This script checks if an application or website is available and functioning properly by sending HTTP requests to a given URL. If the application responds with a 200 status code, it is considered "up"; otherwise, it is marked as "down."

## Prerequisites
Python: Ensure you have Python installed.
requests library: Install the requests library for sending HTTP requests.

`pip install requests`

### Usage
Download the Script: Copy and save the script as application_health_checker.py.
Set the URL: Replace "https://www.google.com" with the URL of the application you want to monitor in the app_url variable.

#### Run the Script:
Open a terminal in the directory containing application_health_checker.py.
Run the script:

`python health_checker.py`

##### Output
 The script will print whether the application is "UP" or "DOWN" based on the HTTP status code.

###### Script Details
UP Status: If the application returns a 200 status code, it is considered "UP."
DOWN Status: If the application returns any other status code or is unreachable, it is considered "DOWN."


===================================================================================
# Backup Script with Remote Transfer

## What This Script Will Do

This Python script automates the process of creating a zip backup of a specified folder, transferring the backup to a remote server using SFTP, and logging the results. The script simplifies routine backup operations by performing the following tasks:

1. **Create a Zip Backup:** Compresses the contents of the specified folder into a zip file.
2. **Transfer Backup to Remote Server:** Uses SSH and SFTP to securely transfer the zip file to a designated folder on a remote server.
3. **Generate a Backup Report:** Logs the success or failure of the backup operation in a report file for easy reference.
4. **Clean Up Local Backup:** Optionally deletes the local backup file after a successful transfer.

## Prerequisites

1. **Python Installation:**
   - Ensure that Python 3.x is installed on your system.
   - You can download Python from [python.org](https://www.python.org/downloads/).

2. **Required Libraries:**
   - Install the required Python libraries by running the following command in your terminal:
     ```
     pip install paramiko
     ```

3. **SSH Setup:**
   - Generate an SSH key pair (if not already created) to connect to the remote server:
     ```
     ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
     ```
   - Add the public key (`id_rsa.pub`) to the `~/.ssh/authorized_keys` file on your remote server.

4. **Remote Server Access:**
   - Ensure you have the correct IP address, username, and SSH private key path for your remote server.

## Configuration

Update the following constants in the script to match your environment:

- `FOLDER_TO_BACKUP`: Path of the folder to be backed up.
- `REMOTE_HOST`: IP address or hostname of your remote server.
- `REMOTE_PORT`: SSH port (default is `22`).
- `REMOTE_USERNAME`: SSH username for the remote server.
- `REMOTE_KEY_PATH`: Path to your private SSH key file.
- `REMOTE_BACKUP_PATH`: Path on the remote server where backups will be stored.

## Usage Instructions

### 1. Clone or Copy the Script

Save the script to your local machine as `backup_script.py`.

### 2. Open the Script in VS Code

- Open Visual Studio Code (VS Code).
- Navigate to the location of the script.
- Open the script file (`backup_script.py`) in VS Code.

### 3. Run the Script

To run the script, follow these steps:

1. Open the terminal in VS Code (`Ctrl+` \`).
2. Navigate to the directory containing the script.
3. Execute the script using the following command:
   ```bash
   python backup_script.py
   ```

### 4. Monitor Output

- The script will:
  1. Create a zip backup of the specified folder.
  2. Transfer the backup to the remote server using SFTP.
  3. Log the operation status in a report file (`backup_report.txt`).

- Any errors or successes will be displayed in the terminal.

## Log and Report Files

1. **Paramiko Log:**
   - The script generates a `paramiko.log` file to log SSH operations for debugging.

2. **Backup Report:**
   - The script appends the backup status and details to `backup_report.txt`.

## Cleanup

If the backup is successfully transferred to the remote server, the script will automatically delete the local backup zip file.

## Troubleshooting

1. **SSH Connection Issues:**
   - Verify the correctness of `REMOTE_HOST`, `REMOTE_PORT`, `REMOTE_USERNAME`, and `REMOTE_KEY_PATH`.
   - Check if the remote server allows SSH connections and if the public key is correctly set up.

2. **Permission Issues:**
   - Ensure you have read/write permissions for the specified folders and files.

3. **Dependency Errors:**
   - Run the following command to ensure all dependencies are installed:
     ```
     pip install -r requirements.txt
     ```





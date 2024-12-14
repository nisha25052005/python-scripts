import os
import zipfile
import paramiko
import logging
from datetime import datetime

# Configuration
FOLDER_TO_BACKUP = r'C:\Users\NISHANTHI SHRI\OneDrive\testing'  # Replace with the folder you want to back up
REMOTE_HOST = '127.0.0.1'         # Replace with the IP or hostname of your remote server
REMOTE_PORT = 22                  # SSH port, usually 22
REMOTE_USERNAME = 'NISHANTHI SHRI'  # Your SSH username (ensure this is correct)
REMOTE_KEY_PATH = r'C:\Users\NISHANTHI SHRI\.ssh\id_rsa'  # Path to your private SSH key file
REMOTE_BACKUP_PATH = r'C:\Users\NISHANTHI SHRI\OneDrive\Documents'  # Path on the remote server to store backups

# Enable Paramiko logging for debugging
paramiko.util.log_to_file("paramiko.log")
logging.basicConfig(level=logging.DEBUG)

def create_backup_zip(folder_path):
    """Create a zip file of the specified folder."""
    backup_filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    backup_path = os.path.join(os.getcwd(), backup_filename)
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                backup_zip.write(file_path, os.path.relpath(file_path, folder_path))
    print(f"Backup created at {backup_path}")
    return backup_path

def transfer_backup(backup_path):
    """Transfer the backup zip file to the remote server."""
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load the private key explicitly as an RSA key
        private_key = paramiko.RSAKey.from_private_key_file(REMOTE_KEY_PATH)

        # Connect to the remote server using the SSH client with the RSA key
        ssh.connect(REMOTE_HOST, port=REMOTE_PORT, username=REMOTE_USERNAME, pkey=private_key)

        # Use SFTP to transfer the file
        sftp = ssh.open_sftp()
        remote_file_path = os.path.join(REMOTE_BACKUP_PATH, os.path.basename(backup_path)).replace("\\", "/")
        sftp.put(backup_path, remote_file_path)
        sftp.close()
        ssh.close()
        print(f"Backup transferred to {REMOTE_HOST}:{remote_file_path}")
        return True
    except Exception as e:
        print(f"Failed to transfer backup: {e}")
        return False

def generate_report(status, backup_path):
    """Generate a report of the backup operation."""
    report_path = 'backup_report.txt'
    with open(report_path, 'a') as report_file:
        report_file.write(f"{datetime.now()}: Backup {'succeeded' if status else 'failed'} - {backup_path}\n")
    print(f"Report updated at {report_path}")

def main():
    # Step 1: Create a zip backup of the folder
    backup_path = create_backup_zip(FOLDER_TO_BACKUP)
    
    # Step 2: Transfer the backup to the remote server
    backup_status = transfer_backup(backup_path)
    
    # Step 3: Generate a report of the backup process
    generate_report(backup_status, backup_path)

    # Optionally: Delete the local backup file after successful transfer
    if backup_status:
        os.remove(backup_path)
        print(f"Local backup file {backup_path} deleted.")

if __name__ == "__main__":
    main()

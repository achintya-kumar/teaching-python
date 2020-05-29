import os
import time


# Function to wrap our custom file-modification requirements
# If some operation is done repeatedly, it's better to wrap it inside a function
def truncate_file(file_path):
    with open(file_path, "a") as file:
        file.truncate(0)
        file.write("Go to hell!")


# Relative path to the file we are monitoring
target_file_path = "file-to-monitor.txt"
# Let's truncate the file in the beginning once
truncate_file(target_file_path)
# We shall use the time below as reference to detect if the file was modified
original_last_modification_time = os.path.getmtime(target_file_path)

# Infinite loop - you know, to run the program indefinitely, until we decide to stop it
while True:
    # Extracting the time when the file was last modified
    last_modification_time_inside_loop = os.path.getmtime(target_file_path)
    # Checking every second if the modification-time of the file has changed since the launch of the program
    if last_modification_time_inside_loop > original_last_modification_time:
        # Looks like the above is true, i.e. the file was modified recently - must edit the file now!
        truncate_file(target_file_path)
        # The file was changed by us. It's last-modified-time has changed again.
        # We should now look for changes after we have modified the file
        new_last_modification_time = os.path.getmtime(target_file_path)
        # Let's reassign the original modification time and use this new time for the future
        original_last_modification_time = new_last_modification_time

    # Let the main thread sleep for 1s. After that, the we repeat the above indefinitely
    time.sleep(1)

import subprocess

# raise exception
output = subprocess.check_output("ls -l", shell=True)
print(output)          # raw bytes
print(output.decode()) # human-readable string

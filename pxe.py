import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_command(cmd):
    """Function to execute a command in the shell."""
    try:
        # Execute command and capture output
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return (cmd, result.stdout.decode('utf-8'), result.stderr.decode('utf-8'), result.returncode)
    except subprocess.CalledProcessError as e:
        return (cmd, e.stdout.decode('utf-8'), e.stderr.decode('utf-8'), e.returncode)

def main():
    # Default to the number of available CPU cores
    num_workers = int(os.getenv('NUM_EXECUTORS', os.cpu_count()))

    # Read commands from stdin
    commands = sys.stdin.read().strip().split('\n')

    # Execute commands in parallel
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        future_to_cmd = {executor.submit(run_command, cmd): cmd for cmd in commands}
        for future in as_completed(future_to_cmd):
            cmd, stdout, stderr, returncode = future.result()
            if stdout:
                print(f"{stdout}")
            if stderr:
                print(f"{stderr}", file=sys.stderr)

if __name__ == "__main__":
    main()

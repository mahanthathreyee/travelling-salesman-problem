import subprocess

# Define the options for each argument
h_options = ['zero', 'prims_mst']

# Path to the input file
input_file = 'data/input/tsp-problem-10-30-75-25-1.txt'

# Output file to store the results
output_file = 'execution_results.txt'

# Open the output file
with open(output_file, 'w') as outfile:
    # Iterate through all combinations of options
    for h_option in h_options:
        # Construct the command to execute
        command = ['python3', 'main.py', input_file, 'heuristic', '-h', h_option]
        
        # Execute the command and capture the output
        print(command)
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Write the command and its output to the file
        outfile.write(f"Command: {' '.join(command)}\n")
        outfile.write(f"Output:\n{result.stdout}\n")
        if result.stderr:
            outfile.write(f"Errors:\n{result.stderr}\n")
        outfile.write("-" * 80 + "\n")

print(f"Execution results have been saved to {output_file}.")

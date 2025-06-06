import re
from os import getcwd
def parse_input(input_text):
    # Regular expression to extract time in format like "07:30 PM" or "8:00pm"
    time_regex = r'(\d{1,2}:\d{2} ?(?:AM|PM|am|pm))'
    
    # Find all matches of time in the input text
    times = re.findall(time_regex, input_text)
    
    if times:
        # Assuming the first time found is the intended time
        time_match = times[0]

        # Normalize the time format to "hh:mmAM/PM"
        formatted_time = time_match.strip().replace(" ", "").upper()
        updated_input_text = input_text.replace(time_match, "").replace("at", "").replace("remind me", "").replace("Remind me", "").replace("to", "").strip()
        
        # Combine formatted time with command
        formatted_output = f"{formatted_time} = Sir this is Your {updated_input_text} time"
        
        return formatted_output, formatted_time
    else:
        return "No valid time found in input", None

def save_to_file1(output_text, time, filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    time_found = False
    with open(filename, 'w') as file:
        for line in lines:
            if line.startswith(time):
                file.write(output_text + '\n')
                time_found = True
            else:
                file.write(line)
        if not time_found:
            file.write(output_text + '\n')

# Example usage:
def input_manage(input_text):
        output, time = parse_input(input_text)

        if output != "No valid time found in input":
            save_to_file1(output, time, r'C:\Users\Ashish Kumar\OneDrive\Desktop\Aksh\schedule.txt')
        else:
            print(output)




def parse_input_Alarm(input_text):
    # Regular expression to extract time in format like "07:30 PM" or "8:00pm"
    time_regex = r'(\d{1,2}:\d{2} ?(?:AM|PM|am|pm))'
    
    # Find all matches of time in the input text
    times = re.findall(time_regex, input_text)
    
    if times:
        # Assuming the first time found is the intended time
        time_match = times[0]

        # Normalize the time format to "hh:mmAM/PM"
        formatted_time = time_match.strip().replace(" ", "").upper()
        
        
        return formatted_time
    else:
        return "No valid time found in input", None

def save_to_file(time, filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    time_found = False
    with open(filename, 'w') as file:
        for line in lines:
            if line.startswith(time):
                file.write(time + '\n')
                time_found = True
            else:
                file.write(line)
        if not time_found:
            file.write(time + '\n')


def input_manage_Alarm(input_text):
        time = parse_input_Alarm(input_text)

        if time != "No valid time found in input":
            save_to_file(time, r'C:\Users\Ashish Kumar\OneDrive\Desktop\Aksh\Alam_data.txt')
        else:
            print("pass")  

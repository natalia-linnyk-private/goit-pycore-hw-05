from pathlib import Path

available_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']

def parse_input_data(input_data: str) -> tuple:
    user_data = input_data.split()

    if(len(user_data) < 1 or len(user_data) > 2):
        raise ValueError("Invalid input format. Please provide a file path and an optional log level filter.")
    
    if(len(user_data) == 2): # Specific level filter is provided
        file_path = user_data[0].strip()
        level_filter = user_data[1].lower()  # The rest is the level filter
    else: # In this case, no specific level filter is provided
        file_path = user_data[0] 
        level_filter = None

    return file_path, level_filter

def validate_input_data(file_path: str, level_filter: str):
    #check if file_path exists
    path_obj = Path(file_path)
    if not path_obj.is_file():
        raise FileNotFoundError(f"The file at path '{file_path}' does not exist.")
    #check if level_filter is valid
    if level_filter is not None and level_filter.upper() not in available_levels:
        raise ValueError(f"Invalid log level filter '{level_filter}'. Available levels are: {', '.join(available_levels)}")
from collections import defaultdict

def load_logs(file_path: str) -> list:
    result = []
    with open(file_path, mode="r", encoding="UTF-8") as file_object:
        all_logs = [line.strip() for line in file_object.readlines()]
        
        for log_line in all_logs:
            log_data = parse_log_line(log_line)
            if log_data is not None: # skip invalid lines
                result.append(log_data)
    return result

def parse_log_line(line: str) -> dict:
    log_data = line.split(' ')
    
    if(len(log_data) < 4):
        return None
    
    log_line = {
        "date": log_data[0],
        "time": log_data[1],
        "level": log_data[2],
        "message": ' '.join(log_data[3::])
    }
    return log_line

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_list = [log for log in logs if log['level'] == level]
    return filtered_list

def count_logs_by_level(logs: list) -> dict:
    level_counted = defaultdict(int)
    
    for item in logs:
        level_value = item['level']
        level_counted[level_value] += 1

    return level_counted

def display_log_counts(counts: dict) -> str:
    lines = []
    lines.append("Log level | Count")
    lines.append("----------|-------")
    
    for level, count in counts.items():
         lines.append(f"{level:<9} | {count:>3}")

    return "\n".join(lines)
from logs_analyzer import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts
from input_processor import parse_input_data, validate_input_data

def main():
    while True:
        try:
            user_input = input("Enter file path and/or log level filter or type 'exit' to quit): ")
            
            if user_input.lower() == 'exit':
                print("Exiting the program")
                break

            file_path, level_filter = parse_input_data(user_input)
            validate_input_data(file_path, level_filter)

            logs = load_logs(file_path)
            log_counts = count_logs_by_level(logs)
            print(display_log_counts(log_counts))

            if level_filter is not None:
                filtered_logs = filter_logs_by_level(logs, level_filter.upper())
                print(f"Logs details for level '{level_filter.upper()}':")
                for log in filtered_logs:
                    print(f"{log['date']} {log['time']} - {log['message']}")

        except Exception as err:
            print(err)

if __name__ == "__main__":
    main()
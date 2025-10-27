from calculation_logic import sum_profit, generator_numbers

def main():
    try:
        text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
        total_income = sum_profit(text, generator_numbers)
        print(f"Загальний дохід: {total_income}")
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()
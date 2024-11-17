from data_processing import load_dataset

def summarize_performance(data):
    """
    Summarize student performance metrics.
    Args:
        data (pd.DataFrame): Student dataset.
    Returns:
        dict: Summary statistics.
    """
    summary = data.describe(include='all')
    print("Performance Summary:")
    print(summary)
    return summary

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to student data CSV")
    args = parser.parse_args()
    data = load_dataset(args.input)
    if data is not None:
        summarize_performance(data)


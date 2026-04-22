from src.pipeline import load_data, process_data
from src.insights import InsightGenerator

def run():
    df = load_data("data/sample_data.csv")
    campaigns = process_data(df)

    insights = InsightGenerator(campaigns)
    result = insights.summary()

    print("=== Campaign Insights ===")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    run()
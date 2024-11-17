from transformers import pipeline
from data_processing import load_dataset

def generate_feedback(student_data):
    """
    Generate feedback for each student in the dataset.
    Args:
        student_data (pd.DataFrame): Student dataset.
    """
    generator = pipeline("text-generation", model="gpt-3.5-turbo", max_length=100)
    for _, student in student_data.iterrows():
        feedback_prompt = (
            f"Student Name: {student['Name']}, "
            f"Score: {student['Score']}, "
            f"Attendance: {student['Attendance']}, "
            f"Engagement: {student['Engagement']}. "
            f"Provide personalized feedback for the student."
        )
        feedback = generator(feedback_prompt)[0]['generated_text']
        print(f"Feedback for {student['Name']}: {feedback}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to student data CSV")
    args = parser.parse_args()
    data = load_dataset(args.input)
    if data is not None:
        generate_feedback(data)


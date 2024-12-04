import config
from flask import render_template, request
from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)

def configure_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            # Retrieve user inputs
            adjective1 = request.form.get("adjective1")
            noun1 = request.form.get("noun1")
            verb1 = request.form.get("verb1")
            adjective2 = request.form.get("adjective2")
            noun2 = request.form.get("noun2")
            verb2 = request.form.get("verb2")

            # Create a prompt using user inputs
            prompt = (
                f"Write a whimsical 4-sentence story using these inputs:\n"
                f"- Adjective1: {adjective1}\n"
                f"- Noun1: {noun1}\n"
                f"- Verb1: {verb1}\n"
                f"- Adjective2: {adjective2}\n"
                f"- Noun2: {noun2}\n"
                f"- Verb2: {verb2}\n"
                "Ensure the story is fun and imaginative."
            )

            try:
                # Call ChatGPT API to generate the story
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a whimsical and imaginative storyteller. Your goal is to create a funny light hearted story."},
                        {"role": "user", "content": prompt}
                    ]
                )
                # Access the content using dot notation
                story = response.choices[0].message.content.strip()
            except Exception as e:
                story = f"An error occurred: {e}"

            # Render the result page with the story
            return render_template("result.html", story=story)

        return render_template("index.html")

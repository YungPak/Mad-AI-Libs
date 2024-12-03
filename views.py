from flask import render_template, request, redirect, url_for

def configure_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            # Retrieve form data
            adjective = request.form.get("adjective")
            noun = request.form.get("noun")
            verb = request.form.get("verb")
            
            # Generate a simple Mad Libs story
            story = f"Once upon a time, a {adjective} {noun} decided to {verb} all day long!"
            
            # Redirect to result page with the story
            return render_template("result.html", story=story)
        
        return render_template("index.html")

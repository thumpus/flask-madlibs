from flask import Flask, request, render_template
app = Flask(__name__)
from stories import Story
@app.route('/')
def show_form():
    """return the form to submit mad libs terms"""
    return render_template("form.html")

@app.route('/story')
def show_story():
    """return the story with the user's inputted terms"""
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")
    story = Story(["place", "noun", "verb", "adjective", "plural_noun"], "Once upon a time in {place}, there lived a {adjective} {noun} who loved to {verb} {plural_noun}")
    story2 = story.generate({"place": place, "noun": noun, "verb": verb, "adjective": adjective, "plural_noun": plural_noun})
    return render_template("story.html", story = story2)
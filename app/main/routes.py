from flask import render_template, request, Blueprint
from app.models import Post
import json
import requests

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home", methods=['GET'])
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data = json.loads(req.content)
    return render_template('home.html', posts=posts, data=data)



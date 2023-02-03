from flask import Flask, jsonify

from .tweet import tweet_by_id, tweets_by_user, user_by_username, user_info

app = Flask(__name__)


@app.route('/')
def main():
    return jsonify({
        'message': 'Welcome'
    })


@app.route('/twttr/tweets/<id>', methods=['GET'])
def get_tweet_by_id(id: str):
    res = tweet_by_id(id)
    return jsonify(res)


@app.route('/twttr/users/<id>', methods=['GET'])
def get_user_info(id: str):
    info = user_info(id)
    return jsonify(info)


@app.route('/twttr/users/username/<username>', methods=['GET'])
def get_user_info_username(username: str):
    user = user_by_username(username)
    # info = user_info(user["id"])
    return jsonify(user)


@app.route('/twttr/users/<username>/tweets', methods=['GET'])
def get_user_tweets(username: str):
    print(username)
    tweets = tweets_by_user(username)
    return jsonify(tweets)

#
# Error Handling
#


@app.errorhandler(Exception)
def handle_error(error):
    """ Default error handler """
    print(error)
    error = error or {}
    if type(error) is object:
        response = jsonify(error)
    else:
        response = str(error)

    return jsonify({'error': response, 'message': 'An error occurred.'}), 500


def run(port=5000, debug=False):
    """ """
    print('Running server on port ' + str(port))
    app.run(port=port, debug=debug)

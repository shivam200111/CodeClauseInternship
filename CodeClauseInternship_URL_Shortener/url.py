from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

shortened_urls = {}

@app.route('/')
def index():
    return render_template_string('''
        <form action="/shorten" method="POST">
            <label for="url">Enter your URL:</label>
            <input type="text" name="url" required>
            <input type="submit" value="Shorten">
        </form>
    ''')

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    short_code = str(len(shortened_urls) + 1)
    shortened_urls[short_code] = url
    return f'Shortened URL: {request.host_url}{short_code}'

@app.route('/<short_code>')
def redirect_to_original_url(short_code):
    if short_code in shortened_urls:
        return redirect(shortened_urls[short_code])
    else:
        return 'URL not found.'

if __name__ == '__main__':
    app.run()



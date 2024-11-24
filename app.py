from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Dictionary to store host links
host_links = {
    'example.com': 'https://example.com/link',
    'sample.com': 'https://sample.com/link'
}

# Function to save unknown host names
def save_unknown_host(host_name):
    with open("unknown_hosts.txt", "a") as file:
        file.write(host_name + "\n")

# Function to save host links to a file
def save_host_links():
    with open("host_links.txt", "w") as file:
        for host, link in host_links.items():
            file.write(f"{host},{link}\n")

# Load host links from file (if exists)
try:
    with open("host_links.txt", "r") as file:
        for line in file:
            host, link = line.strip().split(",", 1)
            host_links[host] = link
except FileNotFoundError:
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_link():
    data = request.get_json()
    host_name = data.get('hostName', '').lower()

    # Normalize the host name
    normalized_host_name = re.sub(r'^https?://', '', host_name)

    if normalized_host_name in host_links:
        link = host_links[normalized_host_name]
        return jsonify({'success': True, 'link': link})
    else:
        # Save unknown host name
        save_unknown_host(normalized_host_name)
        return jsonify({'success': False, 'error': 'Host not found'})

@app.route('/add_links', methods=['GET', 'POST'])
def add_links():
    if request.method == 'POST':
        # Get data from the form
        host_name = request.form.get('host_name').lower()
        link = request.form.get('link')

        # Add to host_links dictionary
        host_links[host_name] = link

        # Save to file
        save_host_links()

        return jsonify({'success': True, 'message': 'Host and link added successfully!'})

    return render_template('add_links.html')

if __name__ == '__main__':
    app.run(debug=True)

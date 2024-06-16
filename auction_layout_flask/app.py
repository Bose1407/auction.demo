from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "poda"

# Sample data - replace with a database in a real application
auction_items = [
    {"id": 1, "name": "Item 1", "description": "Description of Item 1", "current_bid": 10},
    {"id": 2, "name": "Item 2", "description": "Description of Item 2", "current_bid": 15},
]

@app.route('/')
def index():
    return render_template('index.html', items=auction_items)

@app.route('/auction/<int:item_id>', methods=['GET', 'POST'])
def auction(item_id):
    item = next((item for item in auction_items if item['id'] == item_id), None)
    if not item:
        flash("Item not found.")
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        new_bid = int(request.form['bid'])
        if new_bid > item['current_bid']:
            item['current_bid'] = new_bid
            flash(f"Bid placed successfully for {item['name']} at ${new_bid}")
        else:
            flash("Bid must be higher than the current bid.")
        return redirect(url_for('index'))
    
    return render_template('auction.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)

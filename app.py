from flask import Flask, render_template

from datetime import datetime
import foo




app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    the_quakes = foo.get_quake_data();

    # iterate through each quake, give them a "latlng" attribute
    # and then a separate Google Map URL
    for q in the_quakes:
        q['latlng'] = q['latitude'] + ',' + q['longitude']
        q['gmap_url'] = foo.prepare_static_gmap_url(q['latlng'],
                                                widthheight='200x200',
                                                zoom=5)

    # get all the locations from each marker as a single list of lat,lng strings
    locs = [q['latlng'] for q in the_quakes]
    world_map_url = foo.prepare_static_gmap_url(locs, widthheight='800x300')

    html = render_template('homepagenew.html',
                            time=the_time, quakes=the_quakes,
                            world_map_url=world_map_url)
    return html




#new area
@app.route('/contact')
def contact():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    the_quakes = foo.get_quake_data();

    # iterate through each quake, give them a "latlng" attribute
    # and then a separate Google Map URL
    for q in the_quakes:
        q['latlng'] = q['latitude'] + ',' + q['longitude']
        q['gmap_url'] = foo.prepare_static_gmap_url(q['latlng'],
                                                widthheight='200x200',
                                                zoom=5)

    # get all the locations from each marker as a single list of lat,lng strings
    locs = [q['latlng'] for q in the_quakes]
    world_map_url = foo.prepare_static_gmap_url(locs, widthheight='800x300')

    html = render_template('contactnew.html',
                            time=the_time, quakes=the_quakes,
                            world_map_url=world_map_url)
    return html


@app.route('/books')
def books():


       
    return render_template('books.html', title=contact)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
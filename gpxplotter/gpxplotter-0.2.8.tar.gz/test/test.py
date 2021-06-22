from gpxplotter import read_gpx_file, create_folium_map, add_segment_to_map


from gpxplotter import read_gpx_file
from gpxplotter.mplplotting import plot_elevation_hr_multi_dist, save_fig
from matplotlib import pyplot as plt
plt.style.use('seaborn-poster')


for track in read_gpx_file('activity_4655257586.gpx'):
    for i, segment in enumerate(track['segments']):
        fig = plot_elevation_hr_multi_dist(track, segment)
        save_fig(fig, 'test-{}.png'.format(i))

#plt.show()

from gpxplotter import read_gpx_file
from gpxplotter.mplplotting import plot_map, save_map


for track in read_gpx_file('activity_4655257586.gpx'):
    for i, segment in enumerate(track['segments']):
        fig = plot_map(track, segment, zcolor='pulse')
        save_map(fig, 'test-{}.html'.format(i))

the_map = create_folium_map()

from folium.features import ColorLine, PolyLine
import branca.colormap
import numpy as np

for track in read_gpx_file('activity_4655257586.gpx'):
    print(track.keys())
    for i, segment in enumerate(track['segments']):
        #latlon = [(lat, lon) for lat, lon in zip(segment['lat'], segment['lon'])]
        print(i, segment.keys())
        #z = [0 for _ in latlon[:-1]]
        #c = ['b' for _ in latlon[:-1]]
        #color_line = ColorLine(latlon, z, c, opacity=1)

        #line_options = {'weight': 6}
        #add_segment_to_map(the_map, segment, line_options=line_options)

        minp = min(segment['pulse'])
        maxp = max(segment['pulse'])

        colors = [i for i in segment['pulse'][:-1]] 

        print(len(segment['latlon']), len(colors))
        #colormap = branca.colormap.linear.YlOrRd_09.scale(minp, maxp).to_step(6)
        #line = ColorLine(segment['latlon'], colors=colors, colormap=colormap, weight=5)
        #line.add_to(the_map)


        speed = [50, 51, 52, 56, 55, 54, 53]
        longitudes = [10.415180, 10.415179, 10.415180, 10.415187, 10.415201, 10.415224, 10.415251, 10.415282]
        latitudes = [51.919775, 51.919765, 51.919759, 51.919749, 51.919727, 51.919694, 51.919654, 51.919607]
        route = [(lat, lon) for lat, lon in zip(latitudes, longitudes)]

        colormap = branca.colormap.linear.YlOrRd_09.scale(50,56).to_step(6)

        ColorLine(positions=route, colormap=colormap, weight=10, colors=speed, tooltip=[str(i) for i in speed]).add_to(the_map)


        #the_map.location = list(np.mean(latlon, axis=0))
        #the_map.options['zoom'] = 15
        #line = PolyLine(latlon, tooltip='Test', weight=5)
        #the_map.add_child(line)
        
the_map.save('test-0.html')
#root = the_map.get_root()
#print(root.render())

#plt.show()

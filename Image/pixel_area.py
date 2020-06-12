import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Displays the decreasing area covered by a single pixel at
# higher latitudes using the Image.pixelArea() function.

# Create an image in which the value of each pixel is its area.
img = ee.Image.pixelArea()
Map.setCenter(0, 0, 3)
Map.addLayer(img, {'min': 2e8, 'max': 4e8, 'opacity': 0.85}, 'pixel area')

# Display the map.
Map

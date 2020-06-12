
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# This function masks the input with a threshold on the simple cloud score.


def cloudMask(img):
    cloudscore = ee.Algorithms.Landsat.simpleCloudScore(img).select('cloud')
    return img.updateMask(cloudscore.lt(50))


# Load a Landsat 5 image collection.
collection = ee.ImageCollection('LANDSAT/LT5_L1T_TOA') \
    .filterDate('2008-04-01', '2010-04-01') \
    .filterBounds(ee.Geometry.Point(-122.2627, 37.8735)) \
    .map(cloudMask) \
    .select(['B4', 'B3']) \
    .sort('system:time_start', True)  #Sort the collection in chronological order.

print(collection.size().getInfo())

first = collection.first().get('system:id')
print(first.getInfo())
# Display the map.
Map

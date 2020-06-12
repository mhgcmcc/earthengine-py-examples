import os, ee, datetime, csv, time



startTime = datetime.datetime(2001, 1, 1)
endTime = datetime.datetime(2001, 2, 1)

lst = ee.ImageCollection('FORA0125_H002').filterDate(startTime, endTime)

# Get the time series at these points.
points = [ee.Geometry.Point(-85.16516, 30.850000000000001)]
collection = ee.FeatureCollection(points)


# Extract the values by running reduceRegions over each image in the image collection.
def myfunction(i):
    return i.reduceRegions(collection, 'first')


values = '{"type":"CompoundValue","scope":[["0",{"type":"Invocation","arguments":{"id":"USDA/NAIP/DOQQ"},"functionName":"ImageCollection.load"}],["1",{"type":"Invocation","arguments":{"tableId":"USGS/WBD/2017/HUC10"},"functionName":"Collection.loadTable"}],["2",{"type":"Invocation","arguments":{"leftField":"huc10","rightValue":"0701020402"},"functionName":"Filter.equals"}],["3",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"1"},"filter":{"type":"ValueRef","value":"2"}},"functionName":"Collection.filter"}],["4",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"3"}},"functionName":"Collection.geometry"}],["5",{"type":"Invocation","arguments":{"geometry":{"type":"ValueRef","value":"4"}},"functionName":"Feature"}],["6",{"type":"Invocation","arguments":{"leftField":".all","rightValue":{"type":"ValueRef","value":"5"}},"functionName":"Filter.intersects"}],["7",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"0"},"filter":{"type":"ValueRef","value":"6"}},"functionName":"Collection.filter"}],["8",{"type":"Invocation","arguments":{"start":"2009-01-01","end":"2017-12-31"},"functionName":"DateRange"}],["9",{"type":"Invocation","arguments":{"rightField":"system:time_start","leftValue":{"type":"ValueRef","value":"8"}},"functionName":"Filter.dateRangeContains"}],["10",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"7"},"filter":{"type":"ValueRef","value":"9"}},"functionName":"Collection.filter"}],["11",{"type":"Invocation","arguments":{"leftField":"system:band_names","rightValue":"N"},"functionName":"Filter.listContains"}],["12",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"10"},"filter":{"type":"ValueRef","value":"11"}},"functionName":"Collection.filter"}],["13",["system:time_start"]],["14",{"type":"Invocation","arguments":{"paths":{"type":"ValueRef","value":"13"}},"functionName":"SelectorSet"}],["15",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"12"},"selectors":{"type":"ValueRef","value":"14"}},"functionName":"Collection.distinct"}],["16",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"15"},"property":"system:time_start"},"functionName":"AggregateFeatureCollection.array"}],["17",{"type":"Invocation","arguments":{"value":{"type":"ArgumentRef","value":"_MAPPING_VAR_0_0"}},"functionName":"Date"}],["18",{"type":"Invocation","arguments":{"date":{"type":"ValueRef","value":"17"},"unit":"year"},"functionName":"Date.get"}],["19",{"type":"Function","argumentNames":["_MAPPING_VAR_0_0"],"body":{"type":"ValueRef","value":"18"}}],["20",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"16"},"baseAlgorithm":{"type":"ValueRef","value":"19"}},"functionName":"List.map"}],["21",{"type":"Invocation","arguments":{},"functionName":"Reducer.frequencyHistogram"}],["22",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"20"},"reducer":{"type":"ValueRef","value":"21"}},"functionName":"List.reduce"}],["23",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"22"}},"functionName":"Dictionary"}],["24",{"type":"Invocation","arguments":{"dictionary":{"type":"ValueRef","value":"23"}},"functionName":"Dictionary.keys"}],["25",{"type":"Invocation","arguments":{"input":{"type":"ArgumentRef","value":"_MAPPING_VAR_0_0"}},"functionName":"String"}],["26",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"25"}},"functionName":"Number.parse"}],["27",{"type":"Function","argumentNames":["_MAPPING_VAR_0_0"],"body":{"type":"ValueRef","value":"26"}}],["28",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"24"},"baseAlgorithm":{"type":"ValueRef","value":"27"}},"functionName":"List.map"}],["29",{"type":"Invocation","arguments":{"year":{"type":"ArgumentRef","value":"_MAPPING_VAR_0_0"},"month":1,"day":1},"functionName":"Date.fromYMD"}],["30",{"type":"Invocation","arguments":{"year":{"type":"ArgumentRef","value":"_MAPPING_VAR_0_0"},"month":12,"day":31},"functionName":"Date.fromYMD"}],["31",{"type":"Invocation","arguments":{"start":{"type":"ValueRef","value":"29"},"end":{"type":"ValueRef","value":"30"}},"functionName":"DateRange"}],["32",{"type":"Invocation","arguments":{"rightField":"system:time_start","leftValue":{"type":"ValueRef","value":"31"}},"functionName":"Filter.dateRangeContains"}],["33",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"12"},"filter":{"type":"ValueRef","value":"32"}},"functionName":"Collection.filter"}],["34",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"33"}},"functionName":"ImageCollection.mosaic"}],["35",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"34"},"geometry":{"type":"ValueRef","value":"4"}},"functionName":"Image.clip"}],["36",["G","N"]],["37",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"35"},"bandNames":{"type":"ValueRef","value":"36"}},"functionName":"Image.normalizedDifference"}],["38",["nd"]],["39",["ndwi"]],["40",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"37"},"bandSelectors":{"type":"ValueRef","value":"38"},"newNames":{"type":"ValueRef","value":"39"}},"functionName":"Image.select"}],["41",{"type":"Invocation","arguments":{"dstImg":{"type":"ValueRef","value":"35"},"srcImg":{"type":"ValueRef","value":"40"}},"functionName":"Image.addBands"}],["42",["N","R"]],["43",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"35"},"bandNames":{"type":"ValueRef","value":"42"}},"functionName":"Image.normalizedDifference"}],["44",["ndvi"]],["45",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"43"},"bandSelectors":{"type":"ValueRef","value":"38"},"newNames":{"type":"ValueRef","value":"44"}},"functionName":"Image.select"}],["46",{"type":"Invocation","arguments":{"dstImg":{"type":"ValueRef","value":"41"},"srcImg":{"type":"ValueRef","value":"45"}},"functionName":"Image.addBands"}],["47",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"33"},"property":"system:time_start"},"functionName":"AggregateFeatureCollection.array"}],["48",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"47"}},"functionName":"List.sort"}],["49",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"48"},"index":0},"functionName":"List.get"}],["50",{"type":"Invocation","arguments":{"value":{"type":"ValueRef","value":"49"}},"functionName":"Date"}],["51",{"type":"Invocation","arguments":{"object":{"type":"ValueRef","value":"46"},"key":"system:time_start","value":{"type":"ValueRef","value":"50"}},"functionName":"Element.set"}],["52",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"33"},"property":"system:time_end"},"functionName":"AggregateFeatureCollection.array"}],["53",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"52"}},"functionName":"List.sort"}],["54",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"53"},"index":-1},"functionName":"List.get"}],["55",{"type":"Invocation","arguments":{"value":{"type":"ValueRef","value":"54"}},"functionName":"Date"}],["56",{"type":"Invocation","arguments":{"object":{"type":"ValueRef","value":"51"},"key":"system:time_end","value":{"type":"ValueRef","value":"55"}},"functionName":"Element.set"}],["57",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"33"}},"functionName":"Collection.size"}],["58",{"type":"Invocation","arguments":{"object":{"type":"ValueRef","value":"56"},"key":"tiles","value":{"type":"ValueRef","value":"57"}},"functionName":"Element.set"}],["59",{"type":"Function","argumentNames":["_MAPPING_VAR_0_0"],"body":{"type":"ValueRef","value":"58"}}],["60",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"28"},"baseAlgorithm":{"type":"ValueRef","value":"59"}},"functionName":"List.map"}],["61",{"type":"Invocation","arguments":{"images":{"type":"ValueRef","value":"60"}},"functionName":"ImageCollection.fromImages"}],["62",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"61"},"property":"tiles"},"functionName":"AggregateFeatureCollection.mean"}],["63",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"62"}},"functionName":"String"}],["64",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"63"}},"functionName":"Number.parse"}],["65",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"61"},"property":"tiles"},"functionName":"AggregateFeatureCollection.total_sd"}],["66",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"65"}},"functionName":"String"}],["67",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"66"}},"functionName":"Number.parse"}],["68",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"67"},"right":1},"functionName":"Number.multiply"}],["69",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"64"},"right":{"type":"ValueRef","value":"68"}},"functionName":"Number.subtract"}],["70",{"type":"Invocation","arguments":{"leftField":"tiles","rightValue":{"type":"ValueRef","value":"69"}},"functionName":"Filter.lessThan"}],["71",{"type":"Invocation","arguments":{"filter":{"type":"ValueRef","value":"70"}},"functionName":"Filter.not"}],["72",{"type":"Invocation","arguments":{"leftField":"tiles","rightValue":15},"functionName":"Filter.lessThan"}],["73",{"type":"Invocation","arguments":{"filter":{"type":"ValueRef","value":"72"}},"functionName":"Filter.not"}],["74",[{"type":"ValueRef","value":"71"},{"type":"ValueRef","value":"73"}]],["75",{"type":"Invocation","arguments":{"filters":{"type":"ValueRef","value":"74"}},"functionName":"Filter.or"}],["76",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"61"},"filter":{"type":"ValueRef","value":"75"}},"functionName":"Collection.filter"}],["77",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"76"}},"functionName":"Collection.size"}],["78",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"77"},"right":1},"functionName":"Number.subtract"}],["79",{"type":"Invocation","arguments":{"start":0,"end":{"type":"ValueRef","value":"78"}},"functionName":"List.sequence"}],["80",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"76"},"count":{"type":"ValueRef","value":"77"}},"functionName":"Collection.toList"}],["81",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"80"},"index":{"type":"ArgumentRef","value":"_MAPPING_VAR_3_0"}},"functionName":"List.get"}],["82",{"type":"Invocation","arguments":{"input":{"type":"ArgumentRef","value":"_MAPPING_VAR_3_0"}},"functionName":"Number.toUint8"}],["83",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"82"}},"functionName":"String"}],["84",{"type":"Invocation","arguments":{"object":{"type":"ValueRef","value":"81"},"key":"system:index","value":{"type":"ValueRef","value":"83"}},"functionName":"Element.set"}],["85",{"type":"Function","argumentNames":["_MAPPING_VAR_3_0"],"body":{"type":"ValueRef","value":"84"}}],["86",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"79"},"baseAlgorithm":{"type":"ValueRef","value":"85"}},"functionName":"List.map"}],["87",{"type":"Invocation","arguments":{"images":{"type":"ValueRef","value":"86"}},"functionName":"ImageCollection.fromImages"}],["88",{"type":"Invocation","arguments":{"nClusters":5},"functionName":"Clusterer.wekaKMeans"}],["89",[0]],["90",{"type":"Invocation","arguments":{"input":{"type":"ArgumentRef","value":"_MAPPING_VAR_0_0"},"bandSelectors":{"type":"ValueRef","value":"89"}},"functionName":"Image.select"}],["91",{"type":"Invocation","arguments":{"value":0},"functionName":"Image.constant"}],["92",{"type":"Invocation","arguments":{"image1":{"type":"ValueRef","value":"90"},"image2":{"type":"ValueRef","value":"91"}},"functionName":"Image.gt"}],["93",{"type":"Invocation","arguments":{"image":{"type":"ValueRef","value":"92"},"mask":{"type":"ValueRef","value":"92"}},"functionName":"Image.updateMask"}],["94",{"type":"Invocation","arguments":{"image":{"type":"ValueRef","value":"93"},"scale":30,"bestEffort":true,"maxPixels":20000000000},"functionName":"Image.reduceToVectors"}],["95",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"94"}},"functionName":"Collection.geometry"}],["96",{"type":"Invocation","arguments":{"region":{"type":"ValueRef","value":"95"},"points":1},"functionName":"FeatureCollection.randomPoints"}],["97",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"96"}},"functionName":"Collection.first"}],["98",{"type":"Invocation","arguments":{"feature":{"type":"ValueRef","value":"97"}},"functionName":"Element.geometry"}],["99",{"type":"Invocation","arguments":{"geometry":{"type":"ValueRef","value":"98"},"distance":5000},"functionName":"Geometry.buffer"}],["100",{"type":"Invocation","arguments":{"image":{"type":"ArgumentRef","value":"_MAPPING_VAR_0_0"},"region":{"type":"ValueRef","value":"99"},"scale":2,"numPixels":5000},"functionName":"Image.sample"}],["101",{"type":"Invocation","arguments":{"clusterer":{"type":"ValueRef","value":"88"},"features":{"type":"ValueRef","value":"100"}},"functionName":"Clusterer.train"}],["102",{"type":"Invocation","arguments":{"image":{"type":"ArgumentRef","value":"_MAPPING_VAR_0_0"},"clusterer":{"type":"ValueRef","value":"101"}},"functionName":"Image.cluster"}],["103",["cluster"]],["104",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"102"},"bandSelectors":{"type":"ValueRef","value":"103"}},"functionName":"Image.select"}],["105",{"type":"Function","argumentNames":["_MAPPING_VAR_0_0"],"body":{"type":"ValueRef","value":"104"}}],["106",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"87"},"baseAlgorithm":{"type":"ValueRef","value":"105"}},"functionName":"Collection.map"}],["107",{"type":"Invocation","arguments":{"id":"JRC/GSW1_0/GlobalSurfaceWater"},"functionName":"Image.load"}],["108",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"107"},"geometry":{"type":"ValueRef","value":"4"}},"functionName":"Image.clip"}],["109",["occurrence"]],["110",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"108"},"bandSelectors":{"type":"ValueRef","value":"109"}},"functionName":"Image.select"}],["111",{"type":"Invocation","arguments":{"value":80},"functionName":"Image.constant"}],["112",{"type":"Invocation","arguments":{"image1":{"type":"ValueRef","value":"110"},"image2":{"type":"ValueRef","value":"111"}},"functionName":"Image.gt"}],["113",{"type":"Invocation","arguments":{},"functionName":"Image.pixelArea"}],["114",{"type":"Invocation","arguments":{"image1":{"type":"ValueRef","value":"112"},"image2":{"type":"ValueRef","value":"113"}},"functionName":"Image.multiply"}],["115",{"type":"Invocation","arguments":{"value":10000},"functionName":"Image.constant"}],["116",{"type":"Invocation","arguments":{"image1":{"type":"ValueRef","value":"114"},"image2":{"type":"ValueRef","value":"115"}},"functionName":"Image.divide"}],["117",{"type":"Invocation","arguments":{},"functionName":"Reducer.sum"}],["118",{"type":"Invocation","arguments":{"image":{"type":"ValueRef","value":"116"},"collection":{"type":"ValueRef","value":"3"},"reducer":{"type":"ValueRef","value":"117"},"scale":30},"functionName":"Image.reduceRegions"}],["119",{"type":"Invocation","arguments":{"collection":"type":"ValueRef","value":"118"},"property":"sum"},"functionName":"AggregateFeatureCollection.sum"}],["120",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"119"},"right":4},"functionName":"Number.lt"}],["121",{"type":"Invocation","arguments":{"image1":{"type":"ValueRef","value":"110"},"image2":{"type":"ValueRef","value":"91"}},"functionName":"Image.gt"}],["122",{"type":"Invocation","arguments":{"condition":{"type":"ValueRef","value":"120"},"trueCase":{"type":"ValueRef","value":"121"},"falseCase":{"type":"ValueRef","value":"112"}},"functionName":"If"}],["123",{"type":"Invocation","arguments":{"image":{"type":"ArgumentRef","value":"_MAPPING_VAR_3_0"},"mask":{"type":"ValueRef","value":"122"}},"functionName":"Image.updateMask"}],["124",{"type":"Invocation","arguments":{"image":{"type":"ValueRef","value":"123"},"reducer":{"type":"ValueRef","value":"21"},"scale":30,"maxPixels":2100000000},"functionName":"Image.reduceRegion"}],["125",{"type":"Invocation","arguments":{"dictionary":{"type":"ValueRef","value":"124"},"key":"cluster"},"functionName":"Dictionary.get"}],["126",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"125"}},"functionName":"Dictionary"}],["127",{"type":"Invocation","arguments":{"dictionary":{"type":"ValueRef","value":"126"}},"functionName":"Dictionary.keys"}],["128",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"127"}},"functionName":"List.size"}],["129",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"128"},"right":1},"functionName":"Number.subtract"}],["130",{"type":"Invocation","arguments":{"start":0,"end":{"type":"ValueRef","value":"129"}},"functionName":"List.sequence"}],["131",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"127"},"index":{"type":"ArgumentRef","value":"_MAPPING_VAR_1_0"}},"functionName":"List.get"}],["132",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"131"}},"functionName":"String"}],["133",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"132"}},"functionName":"Number.parse"}],["134",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"133"},"right":1},"functionName":"Number.add"}],["135",{"type":"Invocation","arguments":{"dictionary":{"type":"ValueRef","value":"126"}},"functionName":"Dictionary.values"}],["136",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"135"},"reducer":{"type":"ValueRef","value":"117"}},"functionName":"List.reduce"}],["137",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"136"},"right":0.2},"functionName":"Number.multiply"}],["138",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"26"},"right":{"type":"ValueRef","value":"137"}},"functionName":"Number.gt"}],["139",{"type":"Function","argumentNames":["_MAPPING_VAR_0_0"],"body":{"type":"ValueRef","value":"138"}}],["140",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"135"},"baseAlgorithm":{"type":"ValueRef","value":"139"}},"functionName":"List.map"}],["141",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"140"},"index":{"type":"ArgumentRef","value":"_MAPPING_VAR_1_0"}},"functionName":"List.get"}],["142",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"134"},"right":{"type":"ValueRef","value":"141"}},"functionName":"Number.multiply"}],["143",{"type":"Function","argumentNames":["_MAPPING_VAR_1_0"],"body":{"type":"ValueRef","value":"142"}}],["144",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"130"},"baseAlgorithm":{"type":"ValueRef","value":"143"}},"functionName":"List.map"}],["145",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"144"},"other":{"type":"ValueRef","value":"89"}},"functionName":"List.removeAll"}],["146",{"type":"Invocation","arguments":{"left":{"type":"ArgumentRef","value":"_MAPPING_VAR_0_0"},"right":1},"functionName":"Number.subtract"}],["147",{"type":"Function","argumentNames":["_MAPPING_VAR_0_0"],"body":{"type":"ValueRef","value":"146"}}],["148",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"145"},"baseAlgorithm":{"type":"ValueRef","value":"147"}},"functionName":"List.map"}],["149",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"148"}},"functionName":"List.size"}],["150",{"type":"Invocation","arguments":{"value":-1,"count":{"type":"ValueRef","value":"149"}},"functionName":"List.repeat"}],["151",{"type":"Invocation","arguments":{"image":{"type":"ArgumentRef","value":"_MAPPING_VAR_3_0"},"from":{"type":"ValueRef","value":"148"},"to":{"type":"ValueRef","value":"150"}},"functionName":"Image.remap"}],["152",{"type":"Invocation","arguments":{"value":-1},"functionName":"Image.constant"}],["153",{"type":"Invocation","arguments":{"image1":{"type":"ValueRef","value":"151"},"image2":{"type":"ValueRef","value":"152"}},"functionName":"Image.eq"}],["154",{"type":"Invocation","arguments":{"image":{"type":"ValueRef","value":"153"},"mask":{"type":"ValueRef","value":"153"}},"functionName":"Image.updateMask"}],["155",{"type":"Function","argumentNames":["_MAPPING_VAR_3_0"],"body":{"type":"ValueRef","value":"154"}}],["156",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"106"},"baseAlgorithm":{"type":"ValueRef","value":"155"}},"functionName":"Collection.map"}],["157",{"type":"Invocation","arguments":{"value":1},"functionName":"Image.constant"}],["158",{"type":"Invocation","arguments":{"image1":{"type":"ArgumentRef","value":"_MAPPING_VAR_6_0"},"image2":{"type":"ValueRef","value":"157"}},"functionName":"Image.eq"}],["159",{"type":"Invocation","arguments":{"input":{"type":"ArgumentRef","value":"_MAPPING_VAR_0_0"},"bandSelectors":{"type":"ValueRef","value":"39"}},"functionName":"Image.select"}],["160",{"type":"Function","argumentNames":["_MAPPING_VAR_0_0"],"body":{"type":"ValueRef","value":"159"}}],["161",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"87"},"baseAlgorithm":{"type":"ValueRef","value":"160"}},"functionName":"Collection.map"}],["162",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"161"}},"functionName":"reduce.mean"}],["163",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"162"},"bandSelectors":{"type":"ValueRef","value":"39"}},"functionName":"Image.select"}],["164",{"type":"Invocation","arguments":{},"functionName":"Reducer.histogram"}],["165",{"type":"Invocation","arguments":{},"functionName":"Reducer.mean"}],["166",{"type":"Invocation","arguments":{"reducer1":{"type":"ValueRef","value":"164"},"reducer2":{"type":"ValueRef","value":"165"},"outputPrefix":null,"sharedInputs":true},"functionName":"Reducer.combine"}],["167",{"type":"Invocation","arguments":{},"functionName":"Reducer.variance"}],["168",{"type":"Invocation","arguments":{"reducer1":{"type":"ValueRef","value":"166"},"reducer2":{"type":"ValueRef","value":"167"},"outputPrefix":null,"sharedInputs":true},"functionName":"Reducer.combine"}],["169",{"type":"Invocation","arguments":{"image":{"type":"ValueRef","value":"163"},"reducer":{"type":"ValueRef","value":"168"},"geometry":{"type":"ValueRef","value":"4"},"scale":2,"bestEffort":true},"functionName":"Image.reduceRegion"}],["170",{"type":"Invocation","arguments":{"dictionary":{"type":"ValueRef","value":"169"},"key":"ndwi_histogram"},"functionName":"Dictionary.get"}],["171",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"170"}},"functionName":"Dictionary"}],["172",{"type":"Invocation","arguments":{"dictionary":{"type":"ValueRef","value":"171"},"key":"bucketMeans"},"functionName":"Dictionary.get"}],["173",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"172"}},"functionName":"Array"}],["174",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"173"}},"functionName":"Array.length"}],["175",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"174"}},"functionName":"Array"}],["176",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"175"},"position":{"type":"ValueRef","value":"89"}},"functionName":"Array.get"}],["177",{"type":"Invocation","arguments":{"start":1,"end":{"type":"ValueRef","value":"176"}},"functionName":"List.sequence"}],["178",{"type":"Invocation","arguments":{"dictionary":{"type":"ValueRef","value":"171"},"key":"histogram"},"functionName":"Dictionary.get"}],["179",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"178"}},"functionName":"Array"}],["180",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"179"},"axis":0,"start":0,"end":{"type":"ArgumentRef","value":"_MAPPING_VAR_5_0"}},"functionName":"Array.slice"}],["181",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"180"}},"functionName":"Array"}],["182",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"181"},"reducer":{"type":"ValueRef","value":"117"},"axes":{"type":"ValueRef","value":"89"}},"functionName":"Array.reduce"}],["183",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"182"}},"functionName":"Array"}],["184",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"183"},"position":{"type":"ValueRef","value":"89"}},"functionName":"Array.get"}],["185",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"173"},"axis":0,"start":0,"end":{"type":"ArgumentRef","value":"_MAPPING_VAR_5_0"}},"functionName":"Array.slice"}],["186",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"185"}},"functionName":"Array"}],["187",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"186"},"right":{"type":"ValueRef","value":"181"}},"functionName":"Array.multiply"}],["188",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"187"}},"functionName":"Array"}],["189",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"188"},"reducer":{"type":"ValueRef","value":"117"},"axes":{"type":"ValueRef","value":"89"}},"functionName":"Array.reduce"}],["190",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"189"}},"functionName":"Array"}],["191",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"190"},"position":{"type":"ValueRef","value":"89"}},"functionName":"Array.get"}],["192",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"191"},"right":{"type":"ValueRef","value":"184"}},"functionName":"Number.divide"}],["193",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"173"},"right":{"type":"ValueRef","value":"179"}},"functionName":"Array.multiply"}],["194",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"193"}},"functionName":"Array"}],["195",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"194"},"reducer":{"type":"ValueRef","value":"117"},"axes":{"type":"ValueRef","value":"89"}},"functionName":"Array.reduce"}],["196",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"195"}},"functionName":"Array"}],["197",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"196"},"position":{"type":"ValueRef","value":"89"}},"functionName":"Array.get"}],["198",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"179"},"reducer":{"type":"ValueRef","value":"117"},"axes":{"type":"ValueRef","value":"89"}},"functionName":"Array.reduce"}],["199",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"198"}},"functionName":"Array"}],["200",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"199"},"position":{"type":"ValueRef","value":"89"}},"functionName":"Array.get"}],["201",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"197"},"right":{"type":"ValueRef","value":"200"}},"functionName":"Number.divide"}],["202",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"192"},"right":{"type":"ValueRef","value":"201"}},"functionName":"Number.subtract"}],["203",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"202"},"right":2},"functionName":"Number.pow"}],["204",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"184"},"right":{"type":"ValueRef","value":"203"}},"functionName":"Number.multiply"}],["205",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"200"},"right":{"type":"ValueRef","value":"184"}},"functionName":"Number.subtract"}],["206",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"184"},"right":{"type":"ValueRef","value":"192"}},"functionName":"Number.multiply"}],["207",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"197"},"right":{"type":"ValueRef","value":"206"}},"functionName":"Number.subtract"}],["208",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"207"},"right":{"type":"ValueRef","value":"205"}},"functionName":"Number.divide"}],["209",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"208"},"right":{"type":"ValueRef","value":"201"}},"functionName":"Number.subtract"}],["210",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"209"},"right":2},"functionName":"Number.pow"}],["211",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"205"},"right":{"type":"ValueRef","value":"210"}},"functionName":"Number.multiply"}],["212",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"204"},"right":{"type":"ValueRef","value":"211"}},"functionName":"Number.add"}],["213",{"type":"Function","argumentNames":["_MAPPING_VAR_5_0"],"body":{"type":"ValueRef","value":"212"}}],["214",{"type":"Invocation","arguments":{"list":{"type":"ValueRef","value":"177"},"baseAlgorithm":{"type":"ValueRef","value":"213"}},"functionName":"List.map"}],["215",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"214"}},"functionName":"Array"}],["216",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"173"},"keys":{"type":"ValueRef","value":"215"}},"functionName":"Array.sort"}],["217",{"type":"Invocation","arguments":{"values":{"type":"ValueRef","value":"216"}},"functionName":"Array"}],["218",[-1]],["219",{"type":"Invocation","arguments":{"array":{"type":"ValueRef","value":"217"},"position":{"type":"ValueRef","value":"218"}},"functionName":"Array.get"}],["220",{"type":"Invocation","arguments":{"number":{"type":"ValueRef","value":"219"},"pattern":"%.4f"},"functionName":"Number.format"}],["221",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"220"}},"functionName":"Number.parse"}],["222",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"221"},"right":0.2},"functionName":"Number.subtract"}],["223",{"type":"Invocation","arguments":{"left":{"type":"ValueRef","value":"222"},"right":0},"functionName":"Number.gt"}],["224",{"type":"Invocation","arguments":{"condition":{"type":"ValueRef","value":"223"},"trueCase":{"type":"ValueRef","value":"222"},"falseCase":0},"functionName":"If"}],["225",{"type":"Invocation","arguments":{"value":{"type":"ValueRef","value":"224"}},"functionName":"Image.constant"}],["226",{"type":"Invocation","arguments":{"image1":{"type":"ValueRef","value":"162"},"image2":{"type":"ValueRef","value":"225"}},"functionName":"Image.gte"}],["227",{"type":"Invocation","arguments":{"image":{"type":"ValueRef","value":"226"},"mask":{"type":"ValueRef","value":"226"}},"functionName":"Image.updateMask"}],["228",{"type":"Invocation","arguments":{"image1":{"type":"ValueRef","value":"227"},"image2":{"type":"ValueRef","value":"157"}},"functionName":"Image.eq"}],["229",{"type":"Invocation","arguments":{"image1":{"type":"ValueRef","value":"158"},"image2":{"type":"ValueRef","value":"228"}},"functionName":"Image.and"}],["230",{"type":"Invocation","arguments":{"image":{"type":"ValueRef","value":"229"},"mask":{"type":"ValueRef","value":"229"}},"functionName":"Image.updateMask"}],["231",{"type":"Function","argumentNames":["_MAPPING_VAR_6_0"],"body":{"type":"ValueRef","value":"230"}}],["232",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"156"},"baseAlgorithm":{"type":"ValueRef","value":"231"}},"functionName":"Collection.map"}],["233",{"type":"Invocation","arguments":{"collection":{"type":"ValueRef","value":"232"}},"functionName":"reduce.sum"}],["234",{"type":"Invocation","arguments":{"value":{"type":"ValueRef","value":"233"}},"functionName":"Image.toInt"}],["235",{"type":"Invocation","arguments":{"input":{"type":"ValueRef","value":"234"},"bandSelectors":{"type":"ValueRef","value":"89"}},"functionName":"Image.select"}]],"value":{"type":"ValueRef","value":"235"}}'

# Turn the result into a feature collection and export it.
taskParams = {
    'driveFolder': 'image',
    'driveFileNamePrefix': 'TylerTest',
    'fileFormat': 'CSV'
}

MyTry = ee.batch.Export.table(values, 'lst_timeseries', taskParams)
MyTry.start()
state = MyTry.status()['state']
while state in ['READY', 'RUNNING']:
    print(state, '...')
    time.sleep(1)
    state = MyTry.status()['state']
print('Done.', MyTry.status())

# Display the map.
Map

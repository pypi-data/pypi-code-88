import requests

class heliRouteService:
    def route(apikey,lst,transport_mode):
		    payload = {'list':'{}'.format(lst),'apikey':'{}'.format(apikey),'transport-mode':'{}'.format(transport_mode)}
		    r = requests.post("https://nav.heliware.co.in/api/route/",data=payload)
		    return  r.json()
    def isochrone(apikey,lat,lon,transport_mode):
        payload = {'lat': lat, 'long':lon,'apikey':'{}'.format(apikey),'transport-mode':'{}'.format(transport_mode)}
        r = requests.get("https://nav.heliware.co.in/api/isochorome/",params=payload)
        return  r.json()

class heliGeoprocessingService:
    
    def Union(apikey,newdata):
        # nd = "{}".format(newdata)
        # data = [{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"name": "I1", "styleUrl": "#msn_ylw-pushpin"}, "geometry": {"type": "Polygon", "coordinates": [[[77.4029103817493, 28.36918941103731, 0.0], [77.40184896262588, 28.3722403721131, 0.0], [77.39922678901301, 28.37081966588294, 0.0], [77.40030856003351, 28.36816909494472, 0.0], [77.4029103817493, 28.36918941103731, 0.0]]]}}], "name": "I1"},{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"name": "i2", "styleUrl": "#msn_ylw-pushpin"}, "geometry": {"type": "Polygon", "coordinates": [[[77.40486731638147, 28.36831967535351, 0.0], [77.40416140548453, 28.37080235923333, 0.0], [77.40218550684746, 28.3699755298779, 0.0], [77.40187364471585, 28.36769815943599, 0.0], [77.40486731638147, 28.36831967535351, 0.0]]]}}], "name": "i2"}]
        payload = {"apikey":apikey,"data":"{}".format(newdata)}
        r = requests.post("https://ai.heliware.co.in/api/geoprocessing/union/",data=payload)
        return  r.json()
    def Intersection(apikey,newdata):
        # nd = "{}".format(newdata)
        # data = [{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"name": "I1", "styleUrl": "#msn_ylw-pushpin"}, "geometry": {"type": "Polygon", "coordinates": [[[77.4029103817493, 28.36918941103731, 0.0], [77.40184896262588, 28.3722403721131, 0.0], [77.39922678901301, 28.37081966588294, 0.0], [77.40030856003351, 28.36816909494472, 0.0], [77.4029103817493, 28.36918941103731, 0.0]]]}}], "name": "I1"},{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"name": "i2", "styleUrl": "#msn_ylw-pushpin"}, "geometry": {"type": "Polygon", "coordinates": [[[77.40486731638147, 28.36831967535351, 0.0], [77.40416140548453, 28.37080235923333, 0.0], [77.40218550684746, 28.3699755298779, 0.0], [77.40187364471585, 28.36769815943599, 0.0], [77.40486731638147, 28.36831967535351, 0.0]]]}}], "name": "i2"}]
        payload = {"apikey":apikey,"data":"{}".format(newdata)}
        r = requests.post("https://ai.heliware.co.in/api/geoprocessing/intersection/",data=payload)
        return  r.json()
    def PointBuffer(apikey,lst,area):
        payload = {"apikey":apikey,"area":area,"latlonglist":"{}".format(lst)}
        r = requests.post("https://ai.heliware.co.in/api/geoprocessing/bufferpolygon/",data=payload)
        return  r.json()

    def LineBuffer(apikey,lst,area):
        payload = {"apikey":apikey,"area":area,"latlonglist":"{}".format(lst)}
        r = requests.post("https://ai.heliware.co.in/api/geoprocessing/bufferline/",data=payload)
        return  r.json()
    def PointWithinPoly(apikey,pointdata,polydata):
        payload = {"apikey":apikey,"pointdata":"{}".format(pointdata),"polygondata":"{}".format(polydata)}
        r = requests.post("https://ai.heliware.co.in/api/geoprocessing/pointcheck/",data=payload)
        return r.json()
    def AliasLinestring(apikey,lsd,gap,quantity):
        payload = {"apikey":apikey,"lsd":"{}".format(lsd),"gap":"{}".format(gap),"quantity":"{}".format(quantity)}
        r = requests.post("https://ai.heliware.co.in/api/dls/",data=payload)
        return r.json()







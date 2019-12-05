import xml.etree.ElementTree as ET

def scale_distance(xml,scale,):
    """function to scale distances and speeds.

    Args:
        xml (xml ElementTree object): the xml tree object extracted from the tcx file
        scale (int): The scalar factor for computing new distances and speeds.
        tags (list of strings): a list of namespaces and tags to modify

    Returns:
        xml ElementTree object: The tree object with scaled speeds and distances
    """
    for t in tags:
        for value in tree.iter(t):
            value.text = str(float(value.text)*scale)
    return tree



# scale factor
scale = 1.230769

# needed garmin namespaces
ns_schemaLocation = "{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}"
ns3 = "{http://www.garmin.com/xmlschemas/ActivityExtension/v2}"

# tags to modify(including namespaces)
tags = [ns_schemaLocation+'DistanceMeters',ns_schemaLocation+'MaximumSpeed',ns3+'AvgSpeed',ns3+'Speed']



# parse the tcx file
filename = 'activity_4307636557'
tree = ET.parse(filename+'.tcx')

# modify the distances and speeds
tree = scale_distance(tree,scale,tags)

# write out the tcx file
tree.write(filename+'_modified.tcx',xml_declaration=True,encoding='UTF-8')

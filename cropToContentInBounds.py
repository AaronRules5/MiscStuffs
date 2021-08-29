#!/usr/bin/env python

from gimpfu import *

def simpleRegister(regDict):
    register(
        regDict["pyname"],
        regDict["description"],
        regDict["description"],
        regDict["author"],
        regDict["author"],
        regDict["date"],
        regDict["name"],
        regDict["imagetypes"],
        regDict["params"],
        regDict["results"],
        regDict["function"],
        menu= "<Image>/" + regDict["location"]
    )

def replaceDictEntries(dict1,dict2):
    for k,v in dict2.items():
        dict1[k] = v

def crop_to_content_in_bounds(image):
    image.undo_group_start()
    x,y = image.active_layer.offsets
    image.active_layer.resize(image.width, image.height, x, y)
    pdb.plug_in_autocrop_layer(image, image.active_layer)
    image.undo_group_end()

def crop_to_content_in_bounds_all(image):
    image.undo_group_start()
    layers = image.layers
    original_layer = image.active_layer
    for x in layers:
        image.active_layer = x
        crop_to_content_in_bounds(image)
    image.active_layer = original_layer
    image.undo_group_end()

defaultdict = {
    "author" : "Aaron Stultz",
    "date" : "2021",
    "imagetypes" : "",
    "results" : [],
    "params" : [(PF_IMAGE, 'image', 'Input image', None)]
}

ctcibdict = {
    "pyname" : "python_fu_ctcib",
    "location" : "Image",
    "name" : "Crop Layer to Content in Bounds",
    "description" : "Crop the current layer to the content inside the canvas bounds.",
    "function" : crop_to_content_in_bounds
}

ctciballdelta = {
    "pyname" : "python_fu_ctciball",
    "name" : "Crop All Layers to Content in Bounds",
    "description" : "Crop all layers to the content inside the canvas bounds.",
    "function" : crop_to_content_in_bounds_all
}

replaceDictEntries(ctcibdict,defaultdict)
ctciballdict = ctcibdict.copy()
replaceDictEntries(ctciballdict,ctciballdelta)

simpleRegister(ctcibdict)
simpleRegister(ctciballdict)

main()
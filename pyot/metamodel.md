# Goals
We want the user to be able to do the following things easily:

1. **Device-Centric**: Create custom interfaces for a class of device, for example, PhillipsHue, and create instances of those classes.
2. **Model-Centric**: Create a structure for the home that allows for easy naming and identification of instances of these devices
3. **User-Centric**: Create scripts that encode complex, interlinked behaviour within and between devices

# Architecture

###DeviceClass and DeviceInstance
How are we going to develop an architecture to meet this specification? \
Clearly, to meet the device-centric goal, we need an object-oriented language, with classes and instances.\
Python seems like the obvious solution for this.\
The problem is then the interface between the .py files that represent the devices and the .pyot files, that focus on the model and user-centric goals.\
Especially to satisfy the model-centric view, we need a way, in the .pyot file, to refer to custom python classes and create new instances of these classes.\
A potential solution might be as follows:
1. Enforce that the .py files containing the devices must be in a particular package in a particular location within the repo. Also enforce that the .pyot file that imports these custom classes is in a particular location. Now we know the relative path from the .pyot file that imports the custom classes to the .py files that contain the code for said custom classes. 
2. Create a "DeviceClass" rule that is linked to an DeviceClass class. The syntax is "import classname=X". Each invocation creates a new instance of the DeviceClass class. The DeviceClass class will expose a method - call it factory - that returns an instance of the custom class found in X.py.
3. Create a "DeviceInstance" rule that is linked to a DeviceInstance class. The syntax "new class=Y(...params)". The rule uses the link reference rule to refer to the instance of DeviceClass with classname Y, and assigns it to an attribute class. In the init method, we call Y.factory(...params), creating an instance of Y with the parameters, and assign it to attribute "instance".
4. The DeviceInstance thus acts as a wrapper for the custom class, and uses the `__attrs__` method to forward method calls to the concrete component stored in attribute "instance"
5. We might also want a Parameter rule for parameters, or if parameters will be the same across all classes then we can make things simpler

###Tags and TagRefs
Having created the DeviceInstances, we want to be able to create tags and 'tag' certain instances with references to said tags.
I suggest we create a Tag rule to match the creation of new Tags, as well as a TagRef rule that is a match ref rule that references the tag.

###Space


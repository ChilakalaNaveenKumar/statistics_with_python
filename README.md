| **KeyTerm**          | **Definition**                                                                                                                                                     |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Attributes**       | The variables inside a class.                                                                                                                                      |
| **Class**            | A way to represent actual objects through programming by listing attributes to describe the characteristics of the object, as well as the methods, which define the actions that the object can perform. An object might be a car, so there is a Car class with attributes such as color, price, gas tank size, and methods such as drive or park. |
| **docstrings**       | A type of comment that describes how a Python module, function, class, or method works.                                                                            |
| **Function**         | A function and a method are very similar. The main difference is that a method is inside of a class whereas a function is outside of a class.                      |
| **Gaussian**         | Being or having the shape of a normal curve or a normal distribution.                                                                                              |
| **Inheritance**      | In object-oriented programming, an object can be a child of a parent object, in which case the child automatically "inherits" all attributes and methods of the parent class. This is used to generalize objects and is especially useful for code reuse. For example, a "Vehicle" parent class might have several child classes such as Train, Truck, and Bicycle. |
| **Magic methods**    | Methods in Python that can be overridden to redefine their default action.                                                                                         |
| **Methods**          | A named collection of code inside a class that provides action and functionality.                                                                                  |
| **Modularized code** | Object-oriented code that has been placed into separate files.                                                                                                     |
| **Object**           | A representation of a real-world thing by using a class.                                                                                                           |
| **Object-oriented programming** | Also called OOP, this is where code is placed into different modularized objects. These objects represent objects in the real world. |
| **Package**          | A collection of modules placed in a single directory.                                                                                                              |
| **Procedural programming** | A program written in a single file where the instructions go from top to bottom.                                                                             |
| **Scikit-learn**     | A library used in predictive data analysis and machine learning in Python.                                                                                         |
| **self**             | Tells Python where to look in the computer's memory for the current object.                                                                                        |
| **Virtual environment** | A simulated computer that is not physical, includes simulated hardware and software, and acts as a real-world object.   


# Project Setup:

cd statistics_python_package  
python setup.py sdist  
pip install twine  

`commands to upload to the pypi test repository`  
twine upload --repository-url https://test.pypi.org/legacy/ dist/*  
pip install --index-url https://test.pypi.org/simple/ dsnd-probability  

`command to upload to the pypi repository`  
twine upload dist/*  
pip install dsnd-probability

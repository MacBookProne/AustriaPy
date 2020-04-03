  <!DOCTYPE html>

  <head>

  # Assignment 2

  </head>

  <body>

  <h1>Object Orientation</h1>

  <h2>Purpose</h2>

  <p>
    The purpose of this in-lab is to introduce you to the concept of object orientation in python.
    To understand the concepts of object orientation such as inheritance, instance variables, and shallow equality.  
    To familiarize yourself with the concepts of object orientation in python.  
    </p>
  <h2>Partners</h2>

  <p>
    You are encouraged to work with one other partner on this assignment.
    If you work with a partner, you must both be in the same lab section.
    Put your names at the top of your assignment and include your lab section.
  </p>

  <h2>Provided Starting Materials</h2>

  <p>
    Create a project named <b>Lab2FirstLast</b> on your lab computer.
    Place the following files into this project <a href="food.py"> food.py</a>,  <a href="candy.py"> candy.py</a>, <a href ="fruits.py"> fruit.py</a>.
    This diagram that is provided will show you how the classes are inheritining from one another <a href="Inheritance.png"> inheritance diagram</a> If you implemented everything correctly running <a href= "calories.py"> calories.py </a> should have the following output <a href= "calories.txt"> calories.txt</a> The functionality checks in file calories.py should not be changed, but feel free to add more checks and functionality.


  </p>

  <h2>Assignment</h2>

  <p>

  </p>

  <p>
    In this assignment, you are going to build a program that uses inheritance and many other object orientated concepts.   
  </p>

  <ul>
    <b><li>Task1:</b> In the file <a href ="food.py"> food.py</a> you'll need to implement a class called Food.<br/>
    A Food object should have the instance variables name and calories, which are assigned by the constructor.<br/>
    Write two getter functions for those variables called, getName(self) and getCalories(self).<br/>
    Turning a Food object into a string should return a string in this format: "[name] has [calories] calories."<br/>
    Turning a Food object into an integer should return the calories of that object.<br/>
    Adding Food objects should return the sum of the calories. (<b<Hint:</b> implement __radd__ and __add__).<br/>
    Food objects should be comparable (by calories), for that overload the <,>,==,!=,<= and >= operators.<br/>
   </li>
    <b><li>Task2:</b>
    The file <a href ="fruits.py"> fruit.py</a> should contain three classes:<br/>
    The class Fruit should inherit from Food.<br/>
    The constructor of the class Fruit should also take a name and calories and then run the constructor of its parent Food with those arguments.<br/>
    Turning a Fruit object into a string should return a string in this format: "[name] is a fruit and has [calories] calories."<br/>
    The class Apple should inherit from Fruit and the constructor should call the Fruit constructor with the name "apple" and 52 calories.<br/>
    The class Banana should inherit from Fruit and the constructor should call the Fruit constructor with the name "banana" and 94 calories.<br/>
</li>
    <b><li>Task3:</b> The file <a href="candy.py"> candy.py</a> should contain three classes:<br/>
    The class Candy should inherit from Food.<br/>
    The constructor of the class Candy should also take a name and calories and then run the constructor of its parent Food with those arguments.<br/>
    Turning a Candy object into a string should return a string in this format: "[name] is candy and has [calories] calories."
    <b>Hint:</b> Task 3 is very similar to Task 2</li>
    The class Snickers should inherit from Candy and the constructor should call the Candy constructor with the   name "Snickers" and 488 calories.<br/>
    The class KitKat should inherit from Candy and the constructor should call the Candy constructor with the name "KitKat" and 518 calories.<br/> </li>


  </ul>

  <p>  
  </p>      
  <h2>Submission</h2>

  <p>
    Before lab ends, e-mail a copy of <b>Lab2FirstLast.py</b> to your
    lab TA.  The subject of the e-mail should be CSCI 111, Lab 2,
    your lab time, your name, your partner's name at the top of your document.
    To receive credit, this e-mail must be sent before your
    lab period finishes.  Partial credit can be earned, but late
    assignments will not be accepted.
  </p>

  <h2>Grading - 10 points possible</h2>

  <ul>
    <b><li>5 points.</b>  One point will be given for correctly implementing a class called food, correctly adding the instance variables, and writing the getter functions.<br/>
    One point will be given for turning a food object into a string, and turning a food object into an integer, One point will be given for adding food objects and two points will be given comparing food objects.</li>
    <b><li>2 points.</b> One point will be given for inheriting the fruit class from food.<br/> One point will be given for the fruit class taking a name and calories, as well as turning a fruit object into a string and then returning the string.</li>
    <b> <li>2 points.</b> One point will be given for correctly inheriting the Snickers, and KitKat candy to the candy class. One point will be given for turning a candy object into a string.</li>
    <b><li>1 point.</b> One point will be given for adding comments explaining implementation of your program. </li>
    </ul>




  <h2>Helpful Links</h2>

  <p>
    <ul>
    <li> <a href="http://blog.teamtreehouse.com/operator-overloading-python">Operator Overloading In Python</a> </li>
    <li> <a href="https://www.tutorialspoint.com/python/python_classes_objects.htm">Python Object Orientation</a> </li>
    <li> <a href="http://www.python-course.eu/object_oriented_programming.php">Object Orientation Resource</a></li>
    </ul>
  </p>

  </body>
  </html>

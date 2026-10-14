Reflection 

1. What does self mean inside a method? What happens if you forget to write self as the first parameter of deposit? 
so in instance method self is a special parameter which reference to object , that define from which object called deposit() method, and if we forgot to add then it will throw an error missing one positional argument

2. What is the difference between an instance attribute (like balance) and a class attribute (like bank_name)? What happened when you changed balance on one object? What would happen if you put transactions = [] as a class attribute instead of inside __init__? 
instance attributes are those attributes which get created after object creation, we can access using objects, we can't access without object, and class attribute are those which related to only class when object get create class attributes automaticlly assign to object.
and when we changed balance on one object then the connection between class and object regarding balance get break now object have his own balance attribute with that object value 
it will work as constructor bcoz we are not assign anything in constructor.

3. Why is validate_amount a static method and not a normal method? Give one example of a method that must use self and explain why.
validate_amount it si a just normal function which check whether is it number or not so we don't need any slef or something just checking value 
and their are so many methods which required self beacuse we are working no instance attributes like balance and those methods are withdraw , deposite 

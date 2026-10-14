## Reflection

**1. What does `self` mean inside a method? What happens if you forget to write `self` as the first parameter of `deposit`?**

In an instance method, `self` is a special parameter that refers to the object calling the method. It defines which object's data the `deposit()` method will work with. If we forget to add `self` as the first parameter, Python will throw an error because of a missing positional argument.

**2. What is the difference between an instance attribute (like `balance`) and a class attribute (like `bank_name`)? What happened when you changed `balance` on one object? What would happen if you put `transactions = []` as a class attribute instead of inside `__init__`?**

Instance attributes belong to individual objects, while class attributes belong to the class and are shared by its instances by default. When we changed the `balance` of one object, that object got its own `balance` attribute, so the change did not affect the other objects.

If we put `transactions = []` as a class attribute instead of inside `__init__`, all objects would share the same list. Transactions added by one object would also appear in the other objects' transaction lists.

**3. Why is `validate_amount` a static method and not a normal method? Give one example of a method that must use `self` and explain why.**

`validate_amount()` is a static method because it only checks the given value and does not need access to instance attributes or class attributes. Therefore, it does not need `self`.

Methods like `deposit()` and `withdraw()` must use `self` because they work with instance attributes such as `balance` and update the balance of the specific object.
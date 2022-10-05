# Handin-test-2
# 1 - Reflections

### 1.1 Computer Mouse
- Check if the mouse connected to your PC or not
- Check if the computer mouse needs driver updates
- Check if it is a wireless mouse or corded mouse
- Check that left-click and right-click are working fine.
- Check if double clicking is working fine.
- Check if the scroll wheel is present
- Check if the scroll wheel is working
### 1.2 Catastrophic Failure
##### Story: 
In 2007, Albert Gonzalez uploaded his packet-sniffing malware into ATM systems, and captured between 130 and 160 million credit card and debit card numbers.

##### Answer: 
A simple test to see if the software might have been susceptible to SQL-injection

# 2 - Two Katas

### 2.1 String Utility

#### Setup
1. Virtual env, from root of project : **Run command in terminal** ````source venv/Scripts/activate````
2. Run the test, from root of project: **Run command in terminal** ```behave ```

In the following directory tree, u will find three ```.feature``` files which represent the tests in a natural language format. 
```
 ├── test-handin-2 
    ├── features                 
    │   ├── lower_string.feature        
    │   ├── reverse_string.feature       
    │   └── upper_string.feature                
    └── ...
```
In the following directory tree u will find three ```.py``` files which represents the tests itself.
```
 ├── test-handin-2 
    ├── features                 
    │   ├── steps
    │      ├── lower_string.py
    │      ├── reverse_string.py
    │      ├── upper_string.py
    └── ...
```

### 2.2 Bowling Game Kata
1. Run the test, from root of directory : **Run command** ```python -m unittest bowling_test.py ```

# 3 - Investigation of Tools

### 3.1 JUnit 5 

* @Tag - You can use this tag for filter tests by tagging a subset of them under a unique tag name. So for instance if you have unit and integration tests, you could easily group the unit tests under the same tag, and the same with integrationtests.

* @Disabled - Is used to signal that the annotated test method is currently disabled and should not be executed.

* @RepeatedTest - Is used to signal that the annotated method is a test template method that should be repeated a specified number of times. It is important to note that the repeated tests work with the same data. Using an alternative such as paramatized tests can be used to work with data variations.

* @BeforeEach is used to signal that a certain method should be executed before the test
* @AfterEach is used to signal that a certain method should be executed after the test

* @BeforeAll is used to signal that a certain method should be executed before all tests
* @AfterAll is used to signal that a certain method should be executed after all tests
* @Display name is used to declare a custom display name for a test (This does not affect the content of the test)
* @Nested is used declare that the class is placed inside another class and therefore arranged in a certain order
* assumeTrue validates the given assumption to be true and if it is true the test continues
* assumeFalse validates the given assumption to be false and if it is false the test continues

### 3.2 Mocking frameworks
Mocking frameworks were made to avoid creating homemade stubs. The purpose of mocking is to "mock" things away using replacements. You can use it to complement unit testing by isolating dependencies to test their functionality

Since we have experience using mock framework using C#, we will evaluate some of them. 

### Moq

As the two mocking frameworks we will compare Moq is the only one that has a dedicated Mock class to represent a mock. It is known for having a simpler syntax.

#### 1. You first create the mock object for which class you want to isolate and test. you specify the type by using generics as seen below: 

```
var movieScore = new Mock<IMovieScore>();
```

#### 2. Next up you can call the *Setup* and *Return* methods to setup any method calls on the mocks and what the should return: 

```
movieScore.Setup(ms => ms.Score(It.IsAny<string>())).Returns(score);
```

#### 3. The setup verification of a method being called with a specific parameter, use the *Verify* method


```
movieScore.Verify(ms => ms.Score(title));
```

#### Advantages

* Widely adopted
* Explicit mocks (optional)

#### Disadvantages

* You have to create a dedicated mock class
* Setup and verification uses lambdas which makes the code more complex to read





### NSubstitute

NSubstitute is a friendly substitute for .NET mocking libraries. It has a simple, succinct syntax to help developers write clearer tests. NSubstitute is designed for Arrange-Act-Assert (AAA) testing and with Test Driven Development (TDD) in mind.

```
//Create:
var calculator = Substitute.For<ICalculator>();

//Set a return value:
calculator.Add(1, 2).Returns(3);
Assert.AreEqual(3, calculator.Add(1, 2));

//Check received calls:
calculator.Received().Add(1, Arg.Any<int>());
calculator.DidNotReceive().Add(2, 2);

//Raise events
calculator.PoweringUp += Raise.Event();
```

#### Advantages

The most simple syntax of the three
Good documentation

#### Disadvantages

Static state can cause problems with multiple tests 


### Which one we prefer?

We have a lot of experience using Moq, however after trying out NSubstitute and the method extensions it uses makes code a lot cleaner and readable. The fact that NSubstitute is also more user friendly is why we would prefer that framework. 



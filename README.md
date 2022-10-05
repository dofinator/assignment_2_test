# handin-test-2
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



### 2.2 Bowling Game Kata


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
Since we have experience using mock framewor

# Software Requirements
[Link to Main README](README.md)

## Vision
* What is the vision of this product?  
    - To help people make food choice decisions without conflicts.  
* What pain point does this project solve?  
    - Helps you decide quickly on a food item to eat
    - Helps you figure out what to eat when you can't decide
* Why should we care about your product?  
    - Our product will save families countless hours of indecisiveness. We take on the hard part of deciding what you want for dinner when you have no real preference. Through some basic set of questions we are able to come to a personalized recommendation for food to eat that meal.
    
---

## Scope (In/Out)  
* IN - What will your product do:  
    - Takes note of who is ordering each time, and checks the history of ordering to ensure everyone has ordered the same amount.  
    - Series of simple questions about food preferences.
    - Based on the user answers, the system will offer an final food option.  
    - The system will search in at least one web page for restaurants that offer the selected food.
    - The system will provide to the user restaurant suggestions on the selelected food.

* OUT - What will your product not do:  
    - Will not order the food for the user.
    - Will not provide wait times and delivery costs.

---

### Minimum Viable Product vs Stretch Goals 
* What will your MVP functionality be?
    - User will select their city
    - User will respond to a series of questions that will refine their search to a specific food item
    - Results from the user decision will be used to search a website for restaurant options

* What are your stretch goals?  
    - Store the name of the user and its food decision, so when the program begins, it shows the last selections and gives an opportunity to change the user.
    - Show restaurants options sorted by price, quality.
    - Use multiple food sites to search and provide results
    - Front-end beyond a terminal interface
    - Map of restaurants.
    - Provide the user the link of the selected restaurant.
    - Get the user's location so do a restaurant search in the area.

---

## Functional Requirements  
1. A user can provide input to a series of questions  
2. A user can see multiple restaurants from a series of search results
3. A developer can update the questions

---

### Data Flow  
![Data Flow](assets/data-flow.png)

---

## Non-Functional Requirements  
1. Usability
    - User prompts will be validated for correct inputs and will be re-prompted if an incorrect response is inputed by the user.
2. Testability
    - Utilizing pytest, we will develop tests that will use a series of inputs to confirm that the correct search query is selected.
3. Compatability
    - There will not be any restrictions that will prevent the use of the application on the majority operating system.
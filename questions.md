# Questions


### 1. Discuss your strategy and decisions implementing the application. Please, considertime complexity, effort cost, technologies used and any other variable that you understand important on your development process.

My strategy was a full-stack application using Django for the backend and React for the frontend.

The idea was on creating a clear separation between the backend and frontend.

*Note: The database chosen for this project was SQLite due to its simplicity and ease of setup, which is ideal for this assignment.*

Tech Stack:
- Frontend: React with TypeScript;
- Backend: Django, Django-REST, SQLite;



### 2. How would you change your solution to account forfuture columns that might be requested, such as “Bill Voted On Date” or“Co-Sponsors”?

I would update the Django models and serializers to include the new fields.

Django ORM makes it easy to manage these relationships, and the Django-REST serializers could easily be extended to include these fields.



### 3. How would you change your solution if instead ofreceiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

Python and Django provides robust support for exporting data.

I would add an endpoint, query the data and generates a CSV file using Python’s csv library or Django’s built-in CSV response functionality.

### 4. How long did you spend working on the assignment?

I spent approximately 5 hours working.
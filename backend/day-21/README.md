<h1 align="center">Blueprints</h1>

<hr>

## What Are Blueprints in Flask?

Imagine building a big puzzle. Instead of putting all the pieces together in one big pile, you organize them into smaller groups based on their colors or patterns. These smaller groups are like blueprints in Flask. Blueprints help you organize your web application by grouping similar parts together.

<br>

### How Do Blueprints Work?

1. Create the Flask App:
   
   Start by creating your Flask app. This is your main application object, and it should be defined at the top of your script.

   ```python
   from flask import Flask, Blueprint
   app = Flask(__name__)
   ```

2. Create a Blueprint:

   Now, create a blueprint using the `Blueprint` class. This blueprint acts as a container for specific parts of your web app.

   ```python
   main_blueprint = Blueprint('main', __name__)
   ```

3. Define Routes and Views within the Blueprint:

   Inside this blueprint, you can define specific pages and what they should show when people visit them. For example, you can create a home page and an about page.

   ```python
   @main_blueprint.route('/')
   def home():
       return "Welcome to the home page"

   @main_blueprint.route('/about')
   def about():
       return "This is the about page"
   ```

4. Register the Blueprint with the App:

   You need to tell your main Flask app that this blueprint is part of it. It's like putting the smaller groups of puzzle pieces back into the big puzzle box.

   ```python
   app.register_blueprint(main_blueprint)
   ```

5. Run the App:

   Finally, run your Flask app to make it active and accessible through a web browser.

   ```python
   if __name__ == '__main__':
       app.run()
   ```

In our example, when you run the Flask app, and you go to these addresses in your web browser:

- http://localhost:5000/ shows "Welcome to the home page."
- http://localhost:5000/about shows "This is the about page."

Blueprints help you keep your web app organized and make it easier to add more features or pages in the future. It's like having different boxes for different parts of your puzzle, making it easier to complete the big picture.

<hr>
Additional Resource:

* <a href="https://www.freecodecamp.org/news/how-to-use-blueprints-to-organize-flask-apps/">How to Use Blueprints to Organize Your Flask Apps</a>




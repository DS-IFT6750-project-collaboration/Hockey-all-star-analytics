# Q3. Widgets

> Take a screenshot of the tool and add it to the blog post, accompanied with a brief (1-2 sentences) description of what your tool does. You do not need to worry about embedding the tool into the blogpost.

To validate and debug the project, two interactive widgets for Jupyter Notebook were created.

The first widget interfaces with our `StorageEngine` class. The values of `start_year` of the season and the index of the game (`game_idx`) can be changed to load a particular stored JSON file and display some game metadata. This allows for quick validation of the queried, stored, and loaded data.

The second widget helped validate the standardization of plays coordinates. The widget is passed a DataFrame of plays data, the parameter `gamePk` and `period_idx` allow to select a particular game and period. The top figure is a scatter plot of the original (*x, y*) coordinates colored by team. The bottom figure displays the standardized coordinate, where all offensive plays are displayed on the right side.
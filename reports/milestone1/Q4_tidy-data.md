# Q4. Tidy data

>In your blog post, include a small snippet of your final dataframe (e.g. using head(10)). You can just include a screenshot rather than fighting to get the tables neatly formatted in HTML/markdown. 

Our tidied DataFrame has 22 columns


> You’ll notice that the “strength” field (i.e. even, power play, short handed) only exists for goals, not shots. Furthermore, it doesn’t include the actual strength of players on the ice (i.e. 5 on 4, or 5 on 3, etc). Discuss how you could add the actual strength information (i.e. 5 on 4, etc.) to both shots and goals, given the other event types (beyond just shots and goals) and features available. You don’t need to implement this for this milestone. 

For *goal* events, the strength field indicate if the number of players on the ice for both teams was *even*, or if the scoring team was in *power play*, or *short handed*. However, it does not detail the number of players on ice.

By examining events of type *penalty*, the number of players on the ice could be inferred. Indeed, for every penalty, the *timestamp* of the event and the length of the penalty in minutes (*penaltyMinutes*) are available. Finally, *goal* events could be contextualized with the time series of penalty data to find the number of players on the ice at the time of the goal.


> In a few sentences, discuss some additional features you could consider creating from the data available in this dataset. We’re not looking for any particular answers, but if you need some inspiration, could a shot or goal be classified as a rebound, or a shot off the rush?

This rich dataset allows for a variety of questions to be asked. For example:
- A binary feature *star_of_the_previous_match* could be added to label if players were designated as star of the previous match. This way, one could explore trends in *stars* over time, and if being a star has an effect on ulterior performance.
- An ordinal feature *n_hits_received* could be added to count the number of hits a player receives during a game. This could explain changes in the number of shots made, or overall performance of a player. Enhancement to this feature could be made by including the type of hits, and the height and weight of both the hitter and the hittee.
- A categorical feature the *handedness* of players and goalees. It would allow to explore if *opposite-side* and *same-side* handedness between players and goaless affects block rates.

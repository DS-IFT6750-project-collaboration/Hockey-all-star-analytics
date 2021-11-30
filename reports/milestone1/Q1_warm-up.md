# Q1. Warm-up

> Sort the goalies by their save percentage (‘SV%’), which is the ratio of their shots saved over the total number of shots they faced. What issues do you notice by using this metric to rank goalies? What could be done to deal with this? Add this discussion to your blog post (no need for the dataframe or a plot yet).
The save percentage *SV%* tells us about the ability of a goalie. However, the *SV%* does not give an idea of which shots were taken against him. To overcome this, a weighted *saves* score could be created by assigning more points to dangerous shots blocked, than for lower danger ones.

> Filter out the goalies using your proposed approach above, and produce a bar plot with player names on the y-axis and save percentage (‘SV%’) on the x-axis. You can keep the top 20 goalies. Include this figure in your blog post; ensure all of the axes are labeled and the title is appropriate.

> Save percentage is obviously not a very comprehensive feature. Discuss what other features could potentially be useful in determining a goalie’s performance. You do not need to implement anything unless you really want to, all that’s required is a short paragraph of discussion.
Other features could be implemented to assess the performance of a goalie. The number of points (P) describe more broadly the contribution of a goalie. The number of game won would also be relevant. Finally, the number of games played, and the number of game started should be considered to contextualize the *SV%* of a goalie. For example, the *SV%* is more convincing for a large number of games. 

# MLB 2019/2020 Data Analysis

MLB data analysis and regression model building using [sklearn](https://scikit-learn.org/stable/index.html). This project analyzes the patterns of players/teams in the MLB to help make predictions on who is going to have a higher likelihood of winnings and losing games.

## Data Sources:

- Datasets: [https://www.rotowire.com/baseball/stats.php](https://www.rotowire.com/baseball/stats.php)

## Snapshot of the data:

- **Pitching Data set:**

    ![MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pitching.png](MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pitching.png)

- **Hitting Data set:**

    ![MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/hitting.png](MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/hitting.png)

---

## Snapshot of Predicted Data:

- **Pitching Data set:**

    ![MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pitching_preds.png](MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pitching_preds.png)

    ![MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pitching_preds_graph.png](MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pitching_preds_graph.png)

- **Hitting Data set:**

    ![MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/hitting_preds.png](MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/hitting_preds.png)

    ![MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/hitting_preds_graph.png](MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/hitting_preds_graph.png)

    - **Statistical Prediction of Pitching Wins and Batting Averages for the Entire 2020 Season**

        ![MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pred_battings.png](MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pred_battings.png)

        ![MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pred_pitching.png](MLB%202019%202020%20Data%20Analysis%20f5afa4c95aab41159c93103717b043bd/pred_pitching.png)

        ***Hitting predictions are not as good as they could be because the season just picked back up and the stats are not filled out as much as they could be.***
        
### Conclusions and Findings
#### DATA:
 - Player data proved to be more wholistic and offered a more accurate representation as compared to aggregated team stats
 
#### MODEL CHOICES:
 - Under-fitting - matches training data but performs poorly on new data or validation
 - Overfitting - unable to capture important patterns/insights from data, model performs poorly on training data from the jump
 
#### FEATURES:
 - Identifying the correct features through heat map correlation proved to be the most effective in our approach
 - Finding the right balance and avoiding the features/variables can eliminate “noise” and create better overall results
 
#### MEASUREMENTS OF ACCURACY:
 - R2 shows how much a dependent variable is explained by independent variable and hence represents how well any model fits a given dataset
 - MAE (Mean average error) = True values – Predicted values where all differences have equal weight
 - MSE (Mean squared error) = average of the square of the differences between original and predicted values and weights larger error/difference more heavily.
 - Accuracy should be used in conjunction with other measurements, models, plots, and statistics to tell the entire story
 
#### RESULTS AND CONCLUSIONS:
 - The best model for predicting the number of pitcher wins over the season was our Linear Regression model, indicated by strong R2 score.
 - The best model to predict batting averages over the season was both the Linear Regression and Ridge models, but still performed poorly when testing with the smaller 2020 season statistics.
 - Less games played resulted in less accurate modeling, with less IP (or Innings pitched) and less AB (or At Bats) during the 2020 season. 
 - As the 2020 season progresses and more data becomes available, regression model should improve.
 
 Deployed: [https://nifty-booth-d3020f.netlify.app/](https://nifty-booth-d3020f.netlify.app/)

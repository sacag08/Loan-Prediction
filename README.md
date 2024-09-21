# Online Shoppers Purchase Prediction Analysis

The Objective of this project is to predict whether online shopper will purchase a product based on their web activity

## About the Data Used in the modeling:

### Description
The data is taken from UCI Machine Learning Repository. The dataset consists of 10 numerical and 8 categorical attributes.
The 'Revenue' attribute is the class label.
### Summary
The dataset consists of feature vectors belonging to 12,330 sessions. 
The dataset was formed so that each session
would belong to a different user in a 1-year period to avoid
any tendency to a specific campaign, special day, user
profile, or period. 

Of the 12,330 sessions in the dataset, 84.5% (10,422) were negative class samples that did not end with shopping, and the rest (1908) were positive class samples ending with shopping.



| Column Name             | Description                                                                                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administrative          | Number of webpages of adminstrative category visited by user in a single session                                                                                                        |
| Administrative_Duration | Total time spent on adminstarative page category                                                                                                                                        |
| Informational           | Number of webpages of informational category visited by user in a single session                                                                                                        |
| Informational_Duration  | Total time spent on informational page category                                                                                                                                         |
| ProductRelated          | Number of webpages of product related category visited by user in a single session                                                                                                      |
| ProductRelated_Duration | Total time spent on product related page category                                                                                                                                       |
| BounceRates             | Percentage of visitors who enter the site from that page and then leave ("bounce") without triggering any other requests during that session. Bounce rate is calculated by dividing the |
| ExitRates               | For all pageviews to the page, the percentage that were the last in the session. Exit rate is calculated by dividing the total number of visits that exit from a page by the total      |
| PageValues              | The average value for a web page that a user visited before completing an e-commerce transaction                                                                                        |
| SpecialDay              | The "Special Day" feature indicates the closeness of the site visiting time to a specific special day (e.g. Mother’s Day, Valentine's Day) in which the sessions are more likely to be  |
| Month                   | Month in which the user session occurred                                                                                                                                                |
| OperatingSystems        | The Operating System of the device user used when visiting the website                                                                                                                  |
| Browser                 | Browser used to visit website                                                                                                                                                           |
| Region                  | Region of the user                                                                                                                                                                      |
| TrafficType             | The sources of internet traffic                                                                                                                                                         |
| VisitorType             | Is user a new user or a returning user                                                                                                                                                                                                                        |
| Weekend                 | The session occurred at a weekend                                                                                                                                                                                                                             |
| Revenue                 | Did user make the purchase. This is the target variable                                                                                                                                                                                                       |

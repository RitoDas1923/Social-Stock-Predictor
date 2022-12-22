# Social-Stock-Predictor

This project aims to derive a correlation between social media sentiment and stock prices of companies. The app pulls data of a company from tweets made in a specific time period (using SNS Twitter modules)
and creates a dataset . Then it pulls daily stock prices of the same company in that same time period(Yahoo Finance) and creates another dataset. Then a merged dataset is created from both of these dataset by their common date properties.
Then sentiment analysis is applied on the tweets and a final dataset is created based on normalized sentiment value vs change in stock prices .
Then a model is selected and a graph is plotted to find out how much public sentiments affect a certain company stock.


A demo of the Apple stock is given using a simple Web Page hosted using Flask API

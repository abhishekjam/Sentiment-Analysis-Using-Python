# Sentiment-Analysis-Using-Python
Orignal DataSet Link:- https://www.kaggle.com/snap/amazon-fine-food-reviews/data
(Size of 251 Mb)

Develop a sample API using Flask having sentimental analysis engine as backend and it will analysis the reviews of any particular product from the e-commerce website. I am using various libraries of machine learning. The major one is Pandas for datafaming, Textbob for text processing. I also use Regular expression for cleaning the data.
1.	E-Commerce, business or company they analyse their product reviews and the output shows that the customer opinion about that product is not good enough to motivate others to purchase this product so using this sentiments the company will decide how to improve the their quality or improve the advertisement quality.
So, from this every service provider adjust their marketing strategy.
2.	Measure ROI (Return on Investment) of your marketing campaign. Success of your marketing campaign is not measured only by the increase in the number of followers, likes, or comments. The success also lies in how many positive discussions you are able to help facilitate amongst your customers. By doing Sentimental Analysis, you can to see how much positive or negative discussions have occurred amongst your audience. By combining the quantitative and the qualitative measurements, you can measure the true ROI of your marketing campaign.

1 Design Details
Main questions to answer here are:
•	Who is the end user of the system?
•	What are we trying to do for the end user of the system?
•	What objectives are we serving? Why is it important?

Only after answering these ‘who’, ‘what’ and ‘why’ questions, you can start thinking about a number of the ‘how’ questions concerning data collection, feature engineering, building models, evaluation and monitoring of the system.

1.1 Data sources
This step does not require specifics of the data we are planning to collect but it forces us to think about the data sources we are going to use. Some examples of data sources that we can consider are internal databases, open data, social media data, commercial data etc.

1.2 Collecting data
Machine learning project cannot exist without a training dataset — preferably, a large dataset with lots of labeled data. It means that our learning system will need both example inputs and their desired outputs. Only after learning from data that is labeled with the correct answer, our ML model can be used to make predictions on new data.

1.3 Feature Engineering
	Once you have the labeled data, we need to convert it to a format that is acceptable to our algorithm. In machine learning, the process is called feature engineering. The initial set of raw features can be redundant and too large to be managed. Therefore, we need to select the most important and informative features to facilitate learning. Feature engineering requires a lot of experimentation and the combination of automated techniques with the intuition and domain expertise.

1.4 Building and updating models
	There are primarily two reasons to continuously update our model. Firstly, new data improve our model. Secondly, it allows us to capture any changes in the phenomenon we are working with. How often our model needs an update will depend on what we are trying to predict.
	Sometimes updates take more time and more processing power than we actually have. In that case, we need to compromise between cost, time and the quality of our model.

1.5 Machine learning task
	If we have to obtain the sentiment of any reviews the we can use two approaches one is machine learning approach and second one is Polarity based approach
1.5.1 Machine Learning Approach
Machine learning algorithms can be addressed as a combination of methods to automatically detect the available pattern in the given set of data. It makes use of undiscovered patterns to forecast the future data (or) to implement the decision making under uncertainty. Machine learning can be performed in 2 ways such as supervised and unsupervised. Supervised learning is performed by considering the target value (i.e. label) and unsupervised learning is conducted by not considering the target value (i.e. label). There are various types of algorithms for supervised learning such as classification (Decision tree, Naive bayes etc) and unsupervised learning algorithm such as clustering (SOM, Neural network).

1.5.2 Polarity Based Approach
Polarity analysis takes into account the amount of positive or negative terms that appear in a given sentence. It is useful to some extent, since it does a good job of structuring data sets.

      Sentiment classification can be performed in 3 stages such as:-
•	Document level
•	Sentence level
•	Feature level
In document and sentence level the sentiment analysis make use of only a single object and extracts only a single opinion from the single opinion holder. But this type of assumptions is not suitable for many situations. Extracting sentiment for entire document/blog will not be efficient as extracting sentiment by considering aspects of each subject in the particular sentence.


1.6 Making Predictions
	If we are going to build a sentiment analysis system then we need cleaned data and for this i have to use proper regular expression set through which I return clean data. After that I have to check the polarity value of every of ever word by word from the cleaned data and it will returns the sentiments value of that sentence. And after that I have to find the whole percentage like positive, negative and neutral percentage of the whole data.

Polarity Algorithm
	There is huge difference between plain polarity and topic-based sentiment analysis. 
Polarity analysis takes into account the amount of positive or negative terms that appear in a given sentence. It is useful to some extent, since it does a good job of structuring data sets.
Let say I have 1000 reviews on my product that I want to analyze. By using polarity I can identify that 30% are negative, 20% are neutral and 50% are positive – and that’s good for segmentation. But I am left with three chunks of 300, 200 and 500 reviews to go through if I want to get more meaningful insights, rather than just a nice looking pie chart.
And imagine if we have 10 times that data, and in multiple languages! Then we are dealing with some really expensive (and not very delighted) employees that have to spend all day reading through reviews.

2.1 Conclusion 
Twitter is a source of vast unstructured and noisy data sets that can be processed to locate interesting patterns and trends. Apache Spark proved prolific in extracting live streams of data and has further capability to store batches of data in HDFS and other major conventional storages. The processing capabilities of Spark make the project flexible to further extend to multiple nodes, thereby supporting distributed computing. Real time data analysis makes it possible for business organizations to keep track of their services and generates opportunities to promote, advertise and improve from time to time.


2.2 Future Work
From future perspective, we would like to extend this project by implementing some machine learning algorithms for applications like election results, product ratings, movies' outcomes and running the project on clusters to expand its functionalities. 
Moreover, we would Like to make a web application for users to input keyword.

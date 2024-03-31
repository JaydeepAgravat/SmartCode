# Unlocking LeetCode With Data : Navigator and Recommender System

**Leetcode**

<center>
    <a href="https://leetcode.com/">
         <img src="https://i.imgur.com/9aLyuqU.png" width=100px style="box-shadow:rgba(52, 64, 77, 0.2) 0px 1px 5px 0px;border-radius:4px;">
    </a>
</center>

LeetCode is an online platform for coding interview preparation. The service provides coding and algorithmic problems intended for users to practice coding. LeetCode has gained popularity among job seekers and coding enthusiasts as a resource for technical interviews and coding competitions. There are 3000+ technical problems on LeetCode.

**Problem Statement**

> 1. Identify areas for improvement within a repository of 3000 problems.
> 2. On the LeetCode platform, users fall into two main categories: those who are passionate about coding and those who aim to ace technical job interviews, or it can be both. With a vast repository of 3000 problems, users face the challenge of selecting which problems to prioritize.
 
**Main objective**

> The main goal of this project is Identify areas for improvement within a repository of 3000 problems & to assist users in making data-driven decisions and solving relevant problems according to their needs.

 - To achieve this objective, it was further broken down into the following 5 technical sub-objectives:
    - Web scraping of the LeetCode website.
    - Execute data preprocessing to ensure the data is appropriately prepared for analysis and aligned with the project's objectives.
    - Perform exploratory data analysis to identify areas for improvement within a repository of 3000 problems.
    - Develop a user-friendly dashboard to helps users in making data-driven decisions.
    - Develop a LeetCode problems recommender system to help user in solving relevant problems.

## Web scraping of the LeetCode website

### **The details i scraped from LeetCode website :**

1. **is_premium**: Indicates whether the problem is available to premium LeetCode users.
2. **title**: The title of the problem.
3. **problem_description**: A detailed description of the problem.
4. **topic_tags**: Tags representing the topics associated with the problem.
5. **difficulty**: The difficulty level of the problem (Easy, Medium, Hard).
6. **similar_questions**: List of similar questions to the current problem.
7. **no_similar_questions**: The number of similar questions.
8. **acceptance**: Acceptance rate for the problem.
9. **accepted**: The number of submissions that have been accepted for the problem.
10. **submission**: The total number of submissions for the problem.
11. **solution**: The total number of solutions submit in the solution section for the problem.
12. **discussion_count**: The count of discussions related to the problem.
13. **likes**: The number of likes received for the problem.
14. **dislikes**: The number of dislikes received for the problem.
15. **problem_URL**: URL to the problem on LeetCode.
16. **solution_URL**: URL to the solution of the problem on LeetCode.
 
This can be done in three section:

#### First section:

<img src="https://i.imgur.com/giQr7yk.png" style="box-shadow:rgba(52, 64, 77, 0.2) 0px 1px 5px 0px;border-radius:10px;" width=63%>

 - I need to scrape the problem set table that contains all the problems.
 - There are over 3000 problems, distributed over 60 pages.
 - The details i scraped from the first section are:
 - Title, Problem_URL, Solution_URL, Acceptance, Difficulty

#### Second section:

<p float="left">
<img src="https://i.imgur.com/5BwD2nb.png" style="box-shadow:rgba(52, 64, 77, 0.2) 0px 1px 5px 0px;border-radius:10px;" width=30%>
<img src="https://i.imgur.com/ozWPDVj.png" style="box-shadow:rgba(52, 64, 77, 0.2) 0px 1px 5px 0px;border-radius:10px;" width=30%>
<img src="https://i.imgur.com/QETFefW.png" style="box-shadow:rgba(52, 64, 77, 0.2) 0px 1px 5px 0px;border-radius:10px;" width=30%>
</p>

 - I need to scrape 3000 web pages for 3000 problems.
 - The details i scraped from the second section are:
 - Premium Status, Title, Problem Description, Topic Tags, Accepted, Submission, Solution, Discussion Count, Likes, Dislikes, Similar Questions

#### Third section:
   - Combine both part of The DataFrame to get desired dataset.
     
## Data Preprocessing

- The set of operations performed on raw data to make it suitable for analysis.
1. Handling Missing Values
2. Feature Engineering
3. Data Format Conversion and Data Type Conversion
4. Column Rearrangement

#### Handling Missing Values

- `is_premium`: Handle the missing values in the is_premium column by replacing them with the boolean value True to accurately denote the premium status.
- `topic_tags`: Fill the null values with the appropriate values, namely "JavaScript" and "pandas".
- `similar_questions`: Fill in the null values for non-premium questions with an empty string, as there are no similar questions for those LeetCode problems.

#### Feature Engineering
  
- `id`: Extracting the problem numbers (IDs) from the title, which can be useful for organizing and analyzing the data.
- `page_number`: it denotes the specific page on the website where the LeetCode problem appear.
- `no_similar_questions`: extracting a numerical feature from the similar_questions column that represents the number of similar questions.

#### Data Format Conversion and Data Type Conversion

- Removing special characters like % and abbreviations like K and M to represent the values as numbers.
- Changing the data type of the columns from object data type to float or int to make them compatible with numerical analysis.

#### Column Rearrangement

- This process involves changing the sequence of columns to make the DataFrame more organized, intuitive and suitable for analysis.

## Exploratory Data Analysis

### Understanding the LeetCode Dataset ###

- `Overview`

    - The dataset I scraped from the LeetCode website provides information about various programming problems available on the platform. Each row in the dataset corresponds to a specific problem and includes details such as problem ID, premium status, title, problem description, topic tags, difficulty level, similar questions, acceptance rate, and more.

- `Key Columns`

    1. **id**: A unique identifier for each problem.
    2. **page_number**: The specific page on the website where the LeetCode problem appears.
    3. **is_premium**: Indicates whether the problem is available to premium LeetCode users.
    4. **title**: The title of the problem.
    5. **problem_description**: A detailed description of the problem.
    6. **topic_tags**: Tags representing the topics associated with the problem.
    7. **difficulty**: The difficulty level of the problem (Easy, Medium, Hard).
    8. **similar_questions**: List of similar questions to the current problem.
    9. **no_similar_questions**: The number of similar questions.
    10. **acceptance**: Acceptance rate for the problem.
    11. **accepted**: The number of submissions that have been accepted for the problem.
    12. **submission**: The total number of submissions for the problem.
    13. **solution**: The total number of solutions submit in the solution section for the problem.
    14. **discussion_count**: The count of discussions related to the problem.
    15. **likes**: The number of likes received for the problem.
    16. **dislikes**: The number of dislikes received for the problem.
    17. **problem_URL**: URL to the problem on LeetCode.
    18. **solution_URL**: URL to the solution of the problem on LeetCode.

### Initial Analysis ###

1. **Dimensionality of the DataFrame**
    - There are a total of 3,000 LeetCode problems.
2. **Overview of Feature**
    - 18 feature
3. **Duplicate Values**
    - 0 duplicate value
4. **Missing Values**
    - There is a lack of additional data available for 840 premium problems.
    - This feature is available for all the problems : `id`, `is_premium`, `title`, `difficulty`, `acceptance`.

### Univariate Analysis ###

1. **Premium Status**
    - Out of a total of 3000 LeetCode problems, the distribution reveals that:
       - **72%** of problems are `non-premium`.
       - **28%** of problems are `premium`.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/PremiumStatus.png" width="60%">
</p>

2. **Page Number**
    - Page number ranges from 1 to 60, per page contains 50 problems, total 3000 problems.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/PageNumber.png" width="40%">
</p>

3. **Problem Title**
    - Most of the problem titles contain both data structure names (e.g., `strings, arrays, subarray and binary trees`) and problem themes (e.g., `number, maximum, minimum, searching, counting, and summing`).

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/ProblemTitle.png" width="40%">
</p>

4. **Difficulty Level**
    - There are **25%** `Easy` problems and **22%** `Hard` problems.
    - The majority, **53%**, fall under the `Medium` problems.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/DifficultyLevel.png" width="60%">
</p>

5. **Acceptance Rate**
    - The `Acceptance Rates` follow a **normal distribution**, It means the majority of the acceptance rates cluster around mean value.
    - The typical acceptance rate is around **55%**, suggesting that about **55%** of submitted solutions are accepted on average.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/AcceptanceRate.png" width="60%">
</p>

6. **Problem Description**
    - The problem descriptions mainly use words like `Example`, `Input`, `Output` and `Explanation`.
    - it means problem description emphasizing clarity and provide examples.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/ProblemDescription.png" width="40%">
</p>

7. **Topic Tags**
    - There are 74 unique topic tag.
    - Top 10 Most Common Topic Tags are `Array`, `String`, `Hash Table`, `Dynamic Programming`, `Math`, `Sorting`, `Greedy`, `Depth-First Search`, `Binary Search` and `Breadth-First Search`.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/TopicTags.png" width="60%">
</p>

8. **Similar Questions**
    - `Two Sum` stands out with the highest similarity count of **11**, showcasing its widespread application in problem-solving.
    - Several problems, including variations of `Stone Game`, `House Robber` and `Longest Increasing Subsequence` with similarity count **8 or 9**, possibly involve dynamic programming or game theory, highlighting versatile problem-solving approaches.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/SimilarQuestions.png" width="60%">
</p>

9. **Number of Similar Questions**
    - LeetCode's collection showcases diversity with **37.6%** unique challenges having no suggested similar questions.
    - Moderately frequent suggestions **1 to 3 suggestions : 25.5%, 16.7%, 10.2%** indicate common links between challenges.
    - As number of similar questions suggestions increase, frequency decreases, Highlighting that it's uncommon for problems to be strongly connected to many others.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/NumberOfSimilarQuestions.png" width="60%">
</p>

10. **Accepted, Submission, Solution, Discussion Count, likes & Dislikes**
    - The distribution of the Accepted, Submission, Solution, Discussion Count, likes & Dislikes values follows a **log-normal distribution**.
    - This means that most of the values are relatively small, but there are some very large values that occur infrequently.
    - **Accepted and Submission**:
       - The median number of accepted and submission counts indicates the typical level of activity on the platform.
       - Median values of **66,300** and **116,900** respectively suggest a moderate level of participation.
    - **Solution**:
       - The median solution count of **706** implies that most problems have several solutions provided by users.
    - **Discussion Count**:
       - The median discussion count of **12** suggests that discussions are relatively sparse compared to other metrics.
       - This may indicate that users are more focused on solving problems rather than engaging in discussions.
    - **Likes and Dislikes**:
       - The median number of likes **1,100** is significantly higher than the median number of dislikes **132**.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/AcceptedSubmissionSolutionDiscussionCountLikesDislikes.png" width="60%">
</p>

### Bivariate Analysis ###

1. **Analysis of Premium and Non-Premium Problem Frequencies Across Pages**
    - The number of premium and non-premium problems on each page is not the same.
    - Pages 45 to 50 exclusively have premium problems.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/b1.png" width="60%">
</p>

2. **Exploring the relation: Page Number and Highest Contribution by Topic Tag**
    - The percentage of each topic tag's contribution varies from page to page, ranging from 11.27% to 26.51%.
    - Most pages have the highest contribution from the topic tag 'Array', except for pages 3 and 53.
    - Page 3's highest contribution comes from 'Binary Tree' (11.49%), while page 53's highest is 'Javascript' (19.59%).
   
<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/b2.png" width="60%">
</p>

3. **Distribution of Difficulty Level in Premium & Non-Premium**
    - In premium problems, 20% are easy, 56.2% are medium, and 23.8% are hard.
    - In non-premium problems, 27.4% are easy, 51.2% are medium, and 21.4% are hard.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/b3.png" width="60%">
</p>

4. **Distribution of Acceptance Rate in Premium and Non-Premium Problem**
    - Premium problems have an average acceptance rate of 58.3%, compared to 53.55% for non-premium problems.
    - Generally, premium problems have higher acceptance rates than non-premium ones.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/b4.png" width="60%">
</p>

5. **Distribution of Acceptance Rate in Difficulty Level**
    - Easy problems have the highest average acceptance rate (65.53%), followed by medium (54.69%) and hard (46.40%).

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/b5.png" width="60%">
</p>

6. **Most Common Topic Tags in Difficulty Levels:**

    - The top 5 most common topic tags across different difficulty levels are 'Array', 'String', 'Hash Table', 'Dynamic Programming', 'Math', 'Sorting', and 'Binary Search'.
        - **Array**: Most seen in medium difficulty, then hard, and less in easy problems.
        - **String**: Mostly in medium, then easy, and less in hard.
        - **Hash Table**: Mostly in medium, then easy, less in hard.
        - **Dynamic Programming**: Most in medium, increasing from easy to hard.
        - **Math**: Frequently in medium, then easy, slightly less in hard.
        - **Sorting**: Mainly in medium, then easy, less in hard.
        - **Binary Search**: More in medium, then hard, less in easy.
        
<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/b6.png" width="60%">
</p>

7. **Distribution of Accepted, Submission, Solution, Discussion Count, Likes, Dislikes in Difficulty Levels:**
    - **Accepted Submissions**: 'Easy' problems have notably more accepted submissions than 'Medium' and 'Hard', indicating their simplicity.
    - **Submission Activity**: Highest submission activity is for 'Easy' problems, then 'Medium', and least for 'Hard'.
    - **Solution Submissions**: More solutions are submitted for 'Easy' problems compared to 'Medium' and 'Hard', reflecting users' willingness to share solutions.
    - **Discussion Engagement**: Discussions are most active for 'Easy' problems, then 'Medium', and least for 'Hard'.
    - **Likes and Dislikes**: 'Medium' problems receive the most likes, while 'Easy' problems get the most dislikes, suggesting 'Medium' problems are more engaging.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/b7.png" width="60%">
</p>

### Multivariate Analysis ###

1. **Exploring Topic Relevance**
   - The top 9 topics with the lowest positive reaction percentages reveal that even niche or complex areas like "Interactive", "Concurrency", and "Randomized" receive relatively high engagement.

<p align="center">
  <img src="https://github.com/JaydeepAgravat/SmartCode/blob/main/Imgs/ExploringTopic%20Relevance.png" width="60%">
</p>

## Dashboard

## LeetCode Recommender System


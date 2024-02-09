# Unlocking LeetCode With Data : Navigator and Recommender System

**Leetcode**

<center>
    <a href="https://leetcode.com/">
         <img src="https://i.imgur.com/9aLyuqU.png" width=100px style="box-shadow:rgba(52, 64, 77, 0.2) 0px 1px 5px 0px;border-radius:4px;">
    </a>
</center>

LeetCode is an online platform for coding interview preparation. The service provides coding and algorithmic problems intended for users to practice coding. LeetCode has gained popularity among job seekers and coding enthusiasts as a resource for technical interviews and coding competitions.



**Problem Statement**

> 1. On the LeetCode platform, users fall into two main categories: those passionate about solving data structures and algorithms problems and those aiming to ace technical job interviews. With a vast repository of 3000 problems, users face the challenge of selecting which problems to prioritize.
> 2. Identify areas for improvement within a repository of 3000 problems.
 
**Main objective**

> The main goal of this project is to assist users in making data-driven decisions and solving relevant problems

To achieve this objective, it was further broken down into the following 4 technical sub-objectives:

1. Web scraping of the LeetCode website.
2. Perform exploratory data analysis to identify areas for improvement within a repository of 3000 problems.
3. Develop a user-friendly dashboard to helps users in making data-driven decisions.
4. Develop a LeetCode problems recommender system to help user in solving relevant problems.

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

<center><a href="https://leetcode.com/problemset/all/"><img src="https://i.imgur.com/giQr7yk.png" style="box-shadow:rgba(52, 64, 77, 0.2) 0px 1px 5px 0px;border-radius:10px;" width=63%></a></center>

 - I need to scrape the problem set table that contains all the problems.
 - There are over 3000 problems, distributed over 60 pages.
 - The details i scraped from the first section are:
    1. Title
    2. Problem_URL
    3. Solution_URL
    4. Acceptance
    5. Difficulty

#### Second section:

<p float="left">
  <img src="https://i.imgur.com/5BwD2nb.png" width="30%" />
  <img src="https://i.imgur.com/ozWPDVj.png" width="30%" />
  <img src="https://i.imgur.com/QETFefW.png" width="30%" />
</p>

 - I need to scrape 3000 web pages for 3000 problems.
 - The details we are scraping from the second section are:
    1. Premium Status
    2. Title
    3. Problem Description 
    4. Topic Tags
    5. Accepted
    6. Submission
    7. Solution
    8. Discussion Count
    9. Likes
    10. Dislikes
    11. Similar Questions

#### Third section:
   - Combine both part of The DataFrame to get desired dataset.

## Exploratory Data Analysis

## Dashboard

## LeetCode Recommender System


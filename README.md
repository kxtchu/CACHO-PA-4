PA # 4

Author: Nathan Josh Cacho

The goal of this activity is to practice data wrangling and data visualization using the Pandas library together with Matplotlib/Seaborn. The tasks required filtering data into new DataFrames and then analyzing how different features affect students’ average grades.

PROBLEM 1

(a). Instru DataFrame
For this part, I was asked to create a DataFrame containing Name, GEAS, and Electronics >70. I applied a conditional filter to keep only rows where the Track is Instrumentation and Hometown is Luzon. After filtering, I added a new column "Electronics >70" that checks if the Electronics score is greater than 70. Finally, I displayed only the three required columns.

(b). Mindy DataFrame
In this step, the conditions were Hometown = Mindanao and Gender = Female. After applying the filter, I computed the average score of the four subjects: Math, Electronics, GEAS, and Communication. Then I created a new column "Average >=55" to indicate whether the student’s average is at least 55. Lastly, I displayed only the columns Name, Track, Electronics, and Average >=55.

PROBLEM 2

For visualization, I needed to show how Track, Gender, and Hometown contribute to the students’ average grade.

First, I created a new column "Average" which is the mean of all four subjects.

I then used boxplots to display the distribution of average scores grouped by Track, Gender, and Hometown. These plots helped compare differences across categories.

Lastly, I computed summary tables using .groupby() and .mean() to find the actual average per group.

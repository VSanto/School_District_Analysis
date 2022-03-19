# School_District_Analysis 

Completed a review of the school district data.  
15 schools with a total of 39,170 students.
Began by cleaning 1,531 student names within the data and removing professional prefixes and suffixes.  
Created an updated DataFrame with the clean data.
Merged the clean student data with the school district data.
Began the analysis of the data to determine the impact.

## Overview of the school district analysis: Explain the purpose of this analysis.
Purpose of this analysis is to determine the impact the incomplete or inaccurate student data made toward the district data.  
The analysis determined that the 9th grade data from Thomas High Charter School had signs of dishonesty.  
By removing the data from the 9th grade students at Thomas High Charter School the below infromation identifies the impact.

###### How is the district summary affected?
The overall percentage is impacted by the skued data from Thomas High School 9th graders.  Below images show the difference in the percentages before and after the data is cleaned.  There is a higher overall percentage before removing the 9th graders grades from Thomas High Charter School.  

<img width="960" alt="data-4-7-1-output-district-summary" src="https://user-images.githubusercontent.com/92495807/159088747-f7afc250-ad09-43a2-b1d0-e03de7a4c927.png">


![District Summary](https://user-images.githubusercontent.com/92495807/159089862-9e866a79-1733-4381-9fb5-8195553f607c.PNG)


###### How is the school summary affected?
Thomas High Charter School had a much higher math passing percentage before cleaning the data.  After cleaning the data the passing math percentage drops from passing to failing.

![data-4-8-5-bug1158-2](https://user-images.githubusercontent.com/92495807/159090288-7ec315f8-a3c7-422e-a0a1-c899f14ec2fd.png)


![per_school_summary](https://user-images.githubusercontent.com/92495807/159089027-cf18ff31-b204-43b7-a182-efe9e7d86dd5.PNG)


###### How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance relative to the other schools?
Thomas High Charter School was ranked #2.  After adjusting the data Thomas High Charter School ranked #8 out of the district.

![data-4-9-1-top_5_schools](https://user-images.githubusercontent.com/92495807/159091589-2748f1cc-12d8-44d9-8684-1f3af5c23f4e.png)

![Top_Five_Schools](https://user-images.githubusercontent.com/92495807/159091597-dd77a48d-3507-43b6-92af-e76be7f555eb.PNG)

###### How does replacing the ninth-grade scores affect the following:

  ###### 1. Math and reading scores by grade  
  
  There is not a real change with the other schools data.  There is a slight increase in the average but not much to make an impact on the school data.  The biggest change is noticed with data from Thomas High Charter School.  Overall percentages went from a high passing rate to failing.  Thomas high has 461 9th grade students taken out of the equation.  
  

  ###### 2. Scores by school spending
  ![data-4-11-4-spending-formatted](https://user-images.githubusercontent.com/92495807/159093796-682a882b-ad42-4334-ab32-97b9b9a05cf1.png)
  
  ![Spending_Summary_per_Student](https://user-images.githubusercontent.com/92495807/159093373-ebd6f219-f99d-4525-98f3-5f80dd773ec1.PNG)



  ###### 3. Scores by school size
  No changes in data with regards to school size.
  
  ![data-4-12-1-formatted-df-avg-by-size](https://user-images.githubusercontent.com/92495807/159093925-3efc7871-e11a-4f15-8f96-256d45433ebf.png)

  ![School_Size_Summary](https://user-images.githubusercontent.com/92495807/159074157-5c064536-f6e4-41a4-b3d3-ea6213eb3bfc.PNG)

  ###### 4.Scores by school type
There is a slight increase in the Charter School Overall ranking.
  
  ![data-4-13-1-school_type_df](https://user-images.githubusercontent.com/92495807/159094107-1fa0c207-56bc-417a-8812-befc9dbd442f.png)
  
  ![School_Type_Summary](https://user-images.githubusercontent.com/92495807/159075116-605fa7a8-12f5-4134-9742-cb1796182336.PNG)

##  Summary : 
In conclusion, the data shows there is an impact to the district data.                                    
Thomas High Charter School overall district ranking went from 2nd spot to the 8th spot.  
The data shows a decline in the scores for Thomas High Charter School when the scores for the 9th graders were removed from the equation.
There is an impact to the spending ranges per student.  Spending ranges $586-$630 and spending ranges $631-$645 shows a slight increase to per student spending.       
There is a slight increase to the overall passing percentage in the Charter School type.


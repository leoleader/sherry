Quiz Building/Taking Web App developed using Django with sqlite3 db, hosted by Heroku. 

Production To Do List:
    - Try to make user uploaded images and static files work with sqlite3 db

Dev To Do List:
    Search Results Page:
        - Make it look better
    Quiz Result Page:
        - Add share results / share quiz button
    My Quizzes:
        - Ability to Edit/Delete Quizzes
    My Profile:
        - Make it look better
    


This is some documentation from development:

so home page displays quiz blurbs, should lead you to new page with quizid when click on each quiz. 
get to quiz and it displays each question with the corresponding quizid and at the end there is a submit button
which leads to the results tab. 

GOALS:
- User ability to add questions to their quizzes
- Adding possible extra information to quizzes
    - User uploaded images (Share/Thumbnail Image, question images, result images)
    - A Title, and a blurb, custom user message at the end of the quiz
    - Correct answer vs Correct Option
    - Ability to change order of questions or maybe even randomize questions ?
    - Less or more than 4 possible options for a questions (!!)

- CRITCAL - Somehow make a data model or differentiation between knowledge quizzes and personality quizzes

Knowledge Quiz - 1 correct answer each question, at the end tally up how many correct vs incorrect
Personality Quiz - Attached to Quiz information there are possible end results (gonna cap it at 8 for now)
                 - and each answer has an associated end result
                 - at the end the end result with the greatest value is selected


So at the end of the day -------------
Quiz Model has fields: title, blurb, thumbnail/share image, type of quiz
2 Question Models
    QuesModel
    PersModel same as QuesModel except for extra fields holding ForeignKey(Personality)
Personality: A model that has a string to identify it and a corresponding assigned Quiz



So like after all this functionality is added and tested I need to make it look good which is a whole nother thing...
GOAL: Implement ALL of these modeling/data/functionality updates by the end of tonight
Then by the end of Friday night clean it up and make it pretty and launch it.
Then over the weekend I add it to my resume/github and update my personal website (which is lowkey a pain in the butt)

Im gonna leave the user uploaded images for their own kinda section of dev time because I have to be careful with the storage
and overall specifications

    
        

    






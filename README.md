# teacher_toolkit
An AI lesson planner that helps teachers generate rigorous and engaging lessons.

## Functionality

Uses an OpenAI API to generate AI generated lesson plans. Engages with the teacher in an ongoing dialogue to determine:
- Class the lesson is for - determines appropriate age 
- Lesson Objectives including outcomes being addressed
- Skills and content to be addressed
- Differentiation needs of learners

The teacher toolkit then generates a lesson taking all of these factors into account. The teacher can request changes from the AI or can publish the lesson to file which writes it into a file for historical record and easy access.

### Configuration Options
- UpdateID <str prompt> - permnanently updates the user ID which is a component of the system prompt. This is used to provide further context for the AI when generating plans. E.g. UPDATEID "You are an expert Year 12 Enterprise Computing teacher". Deletions require manual modification of the UserID file.



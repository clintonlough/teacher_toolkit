# teacher_toolkit
An AI lesson planner that helps teachers generate rigorous and engaging lessons.

## Project Dependencies
All project dependencies are listed in "requirements.txt"
- OpenAI API
- Youtube API
- dotenv

## Functionality

Uses an OpenAI API to generate AI generated lesson plans. Engages with the teacher in an ongoing dialogue to determine:
- Learning Objectives
- Success Criteria
- Direct Instruction Requirements
- Student Activities
- Opportunities for second chance after feedback
- Resources #TODO: Add non video resource creation
- #TODO Differentiation needs of learners

The teacher toolkit then generates a lesson taking all of these factors into account. The teacher can request changes from the AI or can publish the lesson to file in lessons_plans for historical record.

Use the word "quit" during a prompt to exit the program.

### Configuration Options
#TODO - UpdateID <str prompt> - permnanently updates the user ID which is a component of the system prompt. This is used to provide further context for the AI when generating plans. E.g. UPDATEID "You are an expert Year 12 Enterprise Computing teacher". Deletions require manual modification of the UserID file.

### FLAGS
- --verbose = display token usage and estimated billings per response.

### Unit-Tests
All unit tests are stored in the test_files directory. Run from parent by using the test.sh script. **Requires active API keys for OpenAI and YouTube**
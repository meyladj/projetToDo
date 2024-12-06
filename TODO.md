### TODO Tasks for Task Manager Project

#### Initial Setup
1. **Set Up the Django Project**:
   - [ ] Create a new Django project and app for the task manager.
   - [ ] Configure settings (e.g., database, allowed hosts).
   - [ ] Set up URLs for the app.

2. **Set Up the React Project**:
   - [ ] Create a new React application using Create React App.
   - [ ] Organize the folder structure (e.g., create `components` folder).

#### Backend Development
3. **Define the Task Model**:
   - [ ] Create a Task model in `models.py` with fields:
     - Title (CharField)
     - Completed (BooleanField)
     - Created at (DateTimeField)

4. **Create Views for Task Operations**:
   - [ ] Implement a view to list all tasks (GET).
   - [ ] Implement a view to create a new task (POST).
   - [ ] Implement a view to update an existing task (PUT/PATCH).
   - [ ] Implement a view to delete a task (DELETE).

5. **Set Up URL Routing**:
   - [ ] Define URL routes for each of the task views in `urls.py`.

6. **Test Backend Functionality**:
   - [ ] Use Postman or curl to test each endpoint for CRUD operations.

#### Frontend Development
7. **Build the Task List Component**:
   - [ ] Create a `TaskList` component to display tasks fetched from the backend.
   - [ ] Use Axios or Fetch API to call the backend and retrieve tasks.

8. **Build the Task Form Component**:
   - [ ] Create a `TaskForm` component to handle adding and editing tasks.
   - [ ] Implement form validation for task input.

9. **Add Task Management Functionality**:
   - [ ] Implement functionality to add a task using the `TaskForm`.
   - [ ] Implement functionality to update a task.
   - [ ] Implement functionality to delete a task.

10. **Implement Task Status Toggle**:
    - [ ] Allow users to mark tasks as completed or not.
    - [ ] Visually differentiate completed tasks (e.g., strikethrough).

#### User Interface Enhancements
11. **Styling the Application**:
    - [ ] Add CSS to style the task list and form for a better user experience.
    - [ ] Use a CSS framework (like Bootstrap or Tailwind CSS) for responsive design.

12. **Add User Feedback**:
    - [ ] Implement success and error messages for task operations (e.g., task added successfully).
    - [ ] Show loading indicators while tasks are being fetched or updated.

#### Optional Enhancements
13. **Implement User Authentication**:
    - [ ] Add user registration and login functionality (if you're up for it).
    - [ ] Associate tasks with specific users.

14. **Add Filters and Sorting**:
    - [ ] Implement filtering tasks by completion status or category.
    - [ ] Allow sorting tasks by creation date or alphabetically.

15. **Deploy the Application**:
    - [ ] Prepare the Django app for production (e.g., configure allowed hosts, set DEBUG to False).
    - [ ] Deploy the backend (e.g., on Heroku or a VPS).
    - [ ] Deploy the frontend (e.g., on Netlify or Vercel).

16. **Document the Project**:
    - [ ] Update the `README.md` with any new features and usage instructions.
    - [ ] Write comments in the code to explain complex logic.
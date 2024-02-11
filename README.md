# Penn-Apps-Backend

## Models

- Added an `application` field to the `Applicant` class.
- Added fields corresponding to each question in the application (`application.html`).

## URLs

- Added the necessary fields so that each landing page/process is registered.

## Views

### `application_signup` class

- First, it checks if the user is authenticated. If not, it redirects the user to the login page.
- If the request method is POST, it checks if the user has already submitted an application. If so, it displays an error message and redirects the user to the index page.
- Then, it retrieves the form data submitted by the user, including information such as school, year, phone number, birthday, and short answer questions.
- Next, it creates a new `Application` object with the provided data and saves it to the database.
- It updates the `applicant` field of the `Applicant` object (the user who submitted the application) to link it to the newly created application.
- Finally, it checks for team members provided in the form, links them to the application, and saves the changes.
- It redirects the user to the index page after successfully submitting the application.

### `signup` class

- If the request method is POST, it retrieves the form data submitted by the user, including username, email, first name, last name, and password.
- It creates a new `Applicant` object with the provided data and saves it to the database.
- If the email ends with "@upenn.edu", it sets the `is_penn_student` attribute of the user to `True`.
- It redirects the user to the login page after successful signup.

### `login` class

- If the request method is POST, it retrieves the username and password submitted by the user.
- It queries the database to find the `Applicant` object with the provided username.
- If the user is found and the password matches, it logs in the user using Django's authentication system (`auth_login`).
- It redirects the user to the index page after successful login.
- If the username or password is invalid, it displays an error message and redirects the user to the login page.

### `signout` class

- It logs out the current user using Django's logout function.
- It displays a success message indicating that the user has been logged out.
- It redirects the user to the index page after successful logout.

## Templates

- Slight changes in `index` to include whether or not the applicant has an application registered.
- Changed the logout button to log in if the user is not signed in.
- Added the desired landing pages/called classes for each of the buttons in the different HTML files.

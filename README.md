## CvMS
### A simple Flask-based management system.

Project created in the context of the B65-Synthèse course.


### Configuration
Simply create a file ```data.py``` in the repository's root folder with the following info:

```
data = {
    'SECRET_KEY': 'a hard to guess string',
    'DEV_DB_URL': 'URL for the development database',
    'TEST_DB_URL': 'URL for the testing database',
    'PROD_DB_URL': 'URL for the production database'
}
```

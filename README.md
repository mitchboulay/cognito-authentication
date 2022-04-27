# AWS Cognito Bearer Token
Script written in python to generate a AWS Cognito Bearer token.

## To use locally (Mac/Linux):
Prior to running, be sure nodejs, AWS CDK, python3 and virtual environment is installed on your machine.
1. Clone the repository
2. Update the `.json` file with the necessary information
3. Install dependencies
	 * `pip3 install -r requirements.txt`
4. Execute api.py
	* `python3 api.py`

Produced should be token similar to below: 
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`
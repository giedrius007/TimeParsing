
# DBT-DDaT-tech-test-2024

# Introduction to the test

Welcome to the development tech test for DBT DDaT Software Engineers.

This technical test is expected to take around 1 hour of your own time. We code using Python and JavaScript (NodeJS) so we recommend using one of those to complete your test. Please do not use Haskell, Erlang, Perl, C, C++, Matlab or Assembly.

Once you have completed the test please push this to a web-based repository; we use github so ideally that and to be shared with:

- https://github.com/marcelkornblum
- https://github.com/ince-dbt
- https://github.com/dldbt
- https://github.com/morganmaerees

Please complete this task in as near a way as you would in your normal day-to-day work and provide instructions on how to run your code. 

Deadline for returning the test is Friday, 19th July @ 11:55 pm

When assessing your work the panel will score your solution based on multiple factors such as the quality of your code, tests, organization and readability. Any signs of plagiarism can result in an automatic fail. 

# The test
The test is to create a time parsing function in a similar format to splunk.
Splunk uses a special format for "relative time modifiers" which allows you to take a time and modify it.
We would like you to implement a simplified version of this (this is a subset of what splunk supports).

The format we would like you to parse looks like this:
```
now()-1d@d
```

You can see what you need to support in the definitions below.

Please do not use external libraries only internal ones relevant to your selected coding language to achieve this. You may use some libraries to help with testing.

All dates and times are to be treated as UTC.
A parse function, this needs to take in a string and return a date e.g:
```
parse('now()+1d');
```
Definitions

These are all of the scenarios that you need to support for the test.

Operators

| Operator        | Name modifiers   | Description  |
| ------------- |:-------------| -----|
| +      | plus | Add the offset to the date modifier |
| -      | minus      |   Subtract offset from the date modifier |
| @<time_unit> | snap     |    Rounds down to this time unit |


† Splunk supports a lot of modifiers for this test you only need to support now().

Time units†

| Unit        | Name    | 
| ------------- |:-------------| 
| s	| second |
|m	|minute|
| h	| hour|
|d	|day|
|mon|	month|
|y	|year|


† Splunk supports a lot more time units you just need to support the ones in this list.

# Examples

Using a date and time of 2022-01-08T09:00:00Z:

|String|	Date|	Description|
| -------------|-------------| -------------| 
|now()+1d	|2022-01-09T09:00:00.00Z	|Now plus 1 day|
|now()-1d	|2022-01-07T09:00:00.00Z	|Now minus 1 day|
|now()@d	|2022-01-08T00:00:00.00Z	|Now snapped to day|
|now()-1y@mon|2021-01-01T00:00:00.00Z	|Now minus on year snapped to month|
|now()+10d+12h|	2022-01-18T21:00:00.00Z	|Now plus 10 days and 12 hours|


# How to run

Change command in main.py and run. It will print the output to the console.

Unit tests are located in tests folder.



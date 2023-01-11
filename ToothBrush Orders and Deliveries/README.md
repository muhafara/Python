# ToothBrush Orders and Deliveries

This project helps understand order and delivery data for different types of toothbrushes. Additionally, it will help understand customers by analysing data so we can provide a better service. They are wanting a breakdown of their customer’s demographics and buying habits. 

# Technology used:
1. Aws

- ec2 - Python file scheduled on EC2 instance. This file is schedule to be setup by setting up chrone job. This python script reads data from CSV file which consist of different postcode and generate order number, order date, customer age, delivery postcode, billing postcode, delivery date, dispatched date.
- Simple stroage Service (S3) - Once the CSV file is generated the python script performs data cleaning using pandas and upload the CSV file on S3.
- Lambda Function - When any CSV file is uploaded on S3 lambda function is invoke automatically by setting up a trigger on lambda function.
- AWS RedShift - Lambda function then stores the data in RedShift.
- AWS QuickSight - It is connected with RedShift to analyse the data and create data insight.
- Cloud Watch -  Cloud Watch is used to keep track of application.

This involves scheduling a Python script in our cloud AWS environment, transforming the data and scheduling regular refreshes. 

2. ThoughSpot. Thoughtspot is a very usefull tool which help analysing data and created visual. This tool is connected with AWS RedShift for data anlysics. Also, the live board is embeded in the web app using JavaScript which helps to embed live board SDK.

3. Webapp is develope

- HTML
- CSS
- Java Script

# ETL from python script to insight

![Blank diagram](https://user-images.githubusercontent.com/92796969/211846153-7ef55429-337e-496e-a523-8a1f62b8e38f.jpeg)



# CloudResume

Resume Page :
https://resume.ozcanyildiz.link

Challenge Accepted!

1. Certification :
   I've already passed the AWS Devops Prof exam. So in theory I have stunning knowledge. Next Please!

2. HTML :
   I didn't focus on HTML too much I tried my best but at the end of the day, I am not a web designer. Just see what is going on inside.

3. CSS :
   Same as Html. Didn't focus too much either.

4. Static Website :
   It was an easy one to upload files via the AWS console.

5. HTTPS :
   Getting Serious here. I created a Cloudfront Distribution with legacy access identities. so I turned off public files from S3 now we can access web site only via CloudFront.

6. DNS :
   Here cost me 5 bucks! Anyway, I registered a domain from Route53 and under hosted zones records created a subdomain for resume. I added that domain to CloudFront. Also, I created a certificate for the domain to connect only via HTTPS. I added records to route53 for validation. also in CloudFront don't forget to allow connection via HTTPS only.

7. Javascript :
  To be fair here I can say about Java Script I need to study. just for now I copied and pasted a code from the internet.

8. Database :
   just created a DynamoDB, nothing special.

9. API :
   I think I spent here for a week. First I created an API and Lambda Function to get and update data from the DynamoDB table. used Python. I took a course but I can say I need to spend on it more time, especially on; boto3 and Lambda function side. Created an API with GET Method and before starting the frontend side, I tested the Lambda function via invoking from API Gateway. The next step is deploying the API and adding the link to Html.

10. Python :
    Hello From my first Lambda!

11. Tests :
    Tested every minute, I am the king of Unit Tests!

12. Infrastructure as Code :
    I created a YAML file for DynamoDB Table APIGateway and Lambda Function then deployed it with different names in the same region. The test is successful.

13. Source Control :
    I already have GitHub, next, please!

14. CI/CD (Back end), 15. CI/CD (Front end)
    I created a Yaml file for GitHub actions to deploy Backend with sam, also in the same file, I added to update the s3 bucket for Frontend changes. So now when I change frontend or backend, GitHub actions trigger by push and deploy

![Alt text](cloud_resume_challange.png?raw=true "Title")

    To Do List:
    - Set a test stage for CICD


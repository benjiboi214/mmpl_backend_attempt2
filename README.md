# Env Vars
Please record all environment vaariables implemented in this app, so that you can easily tell if there is any need to add a new one or reuse existing env vars.


Internal Port
External Port
External Host Name

### DJANGO_EXTERNAL_PORT_NUM
The port exposed by the external process.
Only used for local testing at this point.

### DJANGO_EXTERNAL_HOST_NAME
The host name for the external process.
Only used for local testing at this point.

### DJANGO_INTERNAL_PORT_NUM
The port number that django runs on inside the container



# Requirements in AWS
High level list of things we needed to set up manually to get the POC working. Ensure that this is moved to terraform config where possible.
Followed this guide: https://aws.amazon.com/blogs/devops/use-aws-codedeploy-to-implement-blue-green-deployments-for-aws-fargate-and-amazon-ecs/

- CodePipeline
- CodeBuild stage
- ECR permissions on created CodeBuilde execution role
- Create ECR repo
- Add Env Vars to CodePipeline

Adding a deploy step
- Create ALB for that application
- Create task definition
- Create codedeploy execution role for ecs


To properly trigger a blue/green deployment, codedeploy needs an ImageDetail.json file as output.
- https://medium.com/@shashank070/in-my-previous-blog-i-have-explained-how-to-do-initial-checks-like-code-review-code-build-cddcc21afd9f
- https://docs.aws.amazon.com/codepipeline/latest/userguide/file-reference.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/file-reference.html

TaskDef Sample
{
  "executionRoleArn": "arn:aws:iam::account_ID:role/ecsTaskExecutionRole",
  "containerDefinitions": [{
    "name": "sample-website",
    "image": "413514076128.dkr.ecr.ap-southeast-2.amazonaws.com/docker_django_aws_deploy:latest",
    "essential": true,
    "portMappings": [{
      "hostPort": 80,
      "protocol": "tcp",
      "containerPort": 80
    }]
  }],
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "networkMode": "awsvpc",
  "cpu": "256",
  "memory": "512",
  "family": "sample-website"
}


Requirements:
- Load Balancer
- Execution Roles
- 
from diagrams import Cluster, Diagram
from diagrams.aws.storage import S3
from diagrams.aws.security import CertificateManager
from diagrams.aws.network import CloudFront
from diagrams.aws.network import Route53
from diagrams.aws.mobile import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.management import Cloudformation
from diagrams.aws.compute import ServerlessApplicationRepository
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.vcs import Github
from diagrams.onprem.client import Client
from diagrams.onprem.client import User
from diagrams.generic.compute import Rack

with Diagram("Cloud Resume Challange", show=False):


    visitor = Client("Visitors")
    web = Rack("ozcanyil.link")

    with Cluster("Serverless Services"):
        r53 = Route53("Route53")
        cf = CloudFront("CloudFront")
        cm = CertificateManager("Certificate Manager")
        s3 = S3("Amazon S3")

        r53 >> cf >> s3
        cm >> cf

    with Cluster("Visitor Counter"):
        api = APIGateway("APIGateway")
        lambd = Lambda("Lambda Function")
        db = Dynamodb("DynamoDB")

        api >> lambd >> db
        api << lambd << db
    
    admn = User("Admin")
    gith = Github("GitHub Repo")
    gitact = GithubActions("GitHub Actions")
    sam = ServerlessApplicationRepository("SAM")
    cft = Cloudformation("Cloud Formation")

    visitor >> web >> r53
    s3 >> api
    s3 << api
    cft << sam << gitact << gith << admn
    s3 << sam 
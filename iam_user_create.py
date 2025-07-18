import boto3

def create_iam_user(username, policy_arn):
    iam = boto3.client('iam')
    iam.create_user(UserName=username)
    iam.attach_user_policy(UserName=username, PolicyArn=policy_arn)
    keys = iam.create_access_key(UserName=username)
    print(f"User {username} created with access key: {keys['AccessKey']['AccessKeyId']}")

# create_iam_user('test-user', 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')

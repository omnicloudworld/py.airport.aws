import boto3

__all__ = [
    'get_client',
    'split_bucket_and_object_names'
]


def get_client(options: dict):


    # Authenticate to AWS using your access keys
    session = boto3.Session(
        aws_access_key_id=options['AWS_KEY'],
        aws_secret_access_key=options['AWS_SECRET'],
    )

    return session.resource("s3")


def split_bucket_and_object_names(place: str) -> tuple[str, str]:
    """
    Extracts the bucket name and object name from a given place string.
    Args:
        place (str): A string representing the AWS S3 location, in the format
            "s3://bucket-name/object-name".
    Returns:
        A tuple containing the bucket name and object name.
    """
    if not place.startswith("s3://"):
        raise ValueError("Invalid S3 location. It should start with 's3://'")
    place = place[5:]
    parts = place.split('/')

    if len(parts) < 1 or not parts[0]:
        raise ValueError("Invalid S3 location. Bucket name is missing.")
    bucket_name = parts[0]
    object_name = '/'.join(parts[1:])

    return bucket_name, object_name

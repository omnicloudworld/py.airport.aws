import json
from omnicloud.airport.abc import Gate
from omnicloud.airport.tools.json import kw4json

from omnicloud.airport.tools.aws import storage as stt


__all__ = ['AWSS3JSON']


class AWSS3JSON(Gate):

    @classmethod
    def arriving(cls, place: str, **options) -> dict | list:

        client = stt.get_client(options)
        bucket_name, object_name = stt.split_bucket_and_object_names(place)

        obj = client.Object(bucket_name, object_name)
        json_string = obj.get()["Body"].read().decode("utf-8")

        return json.loads(json_string)

    @classmethod
    def departure(cls, parcel, place: str, **options):

        json_data = json.dumps(parcel, **kw4json(options))
        client = stt.get_client(options)

        bucket_name, object_name = stt.split_bucket_and_object_names(place)

        client.Object(bucket_name, object_name).put(Body=json_data)

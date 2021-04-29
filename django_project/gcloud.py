from django.conf import settings as django_settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting as storage_setting
from urllib.parse import urljoin


class GoogleCloudMediaFileStorage(GoogleCloudStorage):
    """
    Google file storage class which gives a media file path from MEDIA_URL not google generated one.
    """

    bucket_name = storage_setting('GS_BUCKET_NAME')

    def url(self, name):
        """
        Gives correct MEDIA_URL and ot google generataed url.
        """
        return urljoin(django_settings.MEDIA_URL, name)

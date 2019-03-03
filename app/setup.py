from google.cloud import storage
import pickle
import os


class ModelData(object):

    """Read the trained model into memory."""

    def __init__(
        self,
        projectname="filmreccommendations",
        bucketname="filmreccommendations.appspot.com",
        blobname="pickled_model.pkl",
    ):
        self.projectname = projectname
        self.bucketname = bucketname
        self.blobname = blobname

        self.tmp_filename = "tmp.pkl"

        self.read_data()

    def read_data(self):
        """Reads the pickled data
        """
        client = storage.Client(project=self.projectname)
        bucket = client.get_bucket(self.bucketname)
        blob = bucket.blob(self.blobname)

        blob.download_to_filename(self.tmp_filename)

        unpkl = pickle.load(open(self.tmp_filename, "rb"))

        os.remove(self.tmp_filename)

        self.neighbours = unpkl["neighbours"]
        self.id_to_movie = unpkl["id_to_movie"]
        self.popular_films = unpkl["popular_films"]


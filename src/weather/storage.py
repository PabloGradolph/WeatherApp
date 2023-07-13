import json
import os

class Storage:
    """
    The Storage class provides functionality to store and retrieve data in 
    different storage formats.

    Attributes
    ----------
    file_name : str
        The name of the file to store the data.
    storage_type : str
        The type of storage format, such as "JSON" or "CSV".

    Methods
    -------
    store_in_json(data: dict) -> None:
        Stores the data in JSON format.
    
    retrieve_from_json() -> dict:
        Retrieves the data from JSON format.
    
    storage_config_mapper() -> dict:
        Returns a mapper dictionary that maps storage types to their respective
        read and write methods.
    
    read() -> dict:
        Reads the data from the specified storage format.
    
    write(data: dict) -> None:
        Writes the data to the specified storage format.
    """

    file_name = 'weather_data.json'
    storage_type = "JSON"


    @classmethod
    def store_in_json(cls, data: dict) -> None:
        """
        Stores the data in JSON format.

        Parameters
        ----------
        data : dict
            The data to be stored.

        Returns
        -------
        None

        """

        with open(cls.file_name, 'w') as file:
            json.dump(data, file)
    

    @classmethod
    def retrieve_from_json(cls) -> dict:
        """
        Retrieves the data from JSON format.

        Returns
        -------
        dict
            The retrieved data.

        """

        if os.path.exists(cls.file_name):
            with open(cls.file_name, 'r') as file:
                data = json.load(file)
            return data
        return {}


    @classmethod
    def storage_config_mapper(cls) -> dict:
        """
        Returns a mapper dictionary that maps storage types to their respective
        read and write methods.

        Returns
        -------
        dict
            The storage type mapper dictionary.

        """
                
        mapper = {
            "JSON": {
                "read": cls.retrieve_from_json,
                "write": cls.store_in_json
            }
        }
        return mapper
    

    @classmethod
    def read(cls) -> dict:
        """
        Reads the data from the specified storage format.

        Returns
        -------
        dict
            The retrieved data.

        """
                
        return cls.storage_config_mapper()[cls.storage_type]["read"]()


    @classmethod
    def write(cls, data: dict) -> None:
        """
        Writes the data to the specified storage format.

        Parameters
        ----------
        data : dict
            The data to be written.

        Returns
        -------
        None

        """
                
        return cls.storage_config_mapper()[cls.storage_type]["write"](data)
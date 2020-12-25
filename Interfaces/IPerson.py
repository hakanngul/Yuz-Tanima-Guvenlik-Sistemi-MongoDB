from abc import ABC, abstractmethod


class IPerson(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        self.id = kwargs.get("_id")
        self.tcNo = kwargs.get("tcNo")
        self.full_name = kwargs.get("full_name")
        self.email = kwargs.get("email")
        self.phone = kwargs.get("phone")
        self.user_role = kwargs.get("user_role")
        self.imagePath = kwargs.get("image_path")

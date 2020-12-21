class IPerson:
    def __init__(self, **kwargs):
        self.userid = kwargs.get("userid")
        self.full_name = kwargs.get("full_name")
        self.email = kwargs.get("email")
        self.phone = kwargs.get("phone")
        self.user_role = kwargs.get("user_role")
        self.imagePath = kwargs.get("image_path")

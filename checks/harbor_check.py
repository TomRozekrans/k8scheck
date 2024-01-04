from icheck import ICheck


class HarborCheck(ICheck):

    def identifier(self):
        return "harborcheck"

    def name(self):
        return "Harbor Check"

    def description(self):
        return """
        Check if all images that are using a harbor url are formatted correctly.
        """



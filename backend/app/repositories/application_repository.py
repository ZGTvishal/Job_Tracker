from api import applications


class ApplicationRepository:

    def get_by_id(application_id):
        ...

    def get_by_company_and_role(company_name, role):
        ...

    def create(application):
        ...

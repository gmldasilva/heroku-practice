import uuid
import logging
from sqlalchemy.orm.exc                     import NoResultFound
from sqlalchemy.exc                         import IntegrityError
from controllers.base                       import BaseController
from models.company                         import Company
from models.rule                            import Rule
from models.company_event                   import CompanyEvent
from models.event_type                      import EventType
from models.company_event_version           import CompanyEventVersion
from mappers.company                        import CompanyMapper
from client_exception                       import NotFoundException, ConflictException, BadRequestException

class CompanyController(BaseController):
    def __init__(self, db_session):
        BaseController.__init__(self)
        self.db_session = db_session
        self.logger = logging.getLogger(__name__)

    def create_user_account(self, user_account_source):
        new_company = CompanyMapper.toModel(company_source)
        new_company_dto = CompanyMapper.toDTO(new_company)
        self.db_session.add(new_company)
        self.db_session.commit()
        return new_company_dto

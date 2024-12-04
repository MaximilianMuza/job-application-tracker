from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from typing import Optional
import uuid

class ApplicationStatus(Enum):
    """Enumeration for the possible states of a job application."""
    APPLIED = "Applied"
    UNDER_REVIEW = "Under Review"
    INTERVIEW_SCHEDULED = "Interview Scheduled"
    INTERVIEWING = "Interviewing"
    OFFER_EXTENDED = "Offer Extended"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    WITHDRAWN = "Withdrawn"
    ON_HOLD = "On Hold"
    CLOSED = "Closed"

@dataclass
class Application:
    """Dataclass defined for an application."""
    date: datetime.date
    job_title: str
    company_name: str
    job_posting_url: str
    description: Optional[str] = None
    file_link: Optional[str] = None
    uuid: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: ApplicationStatus = ApplicationStatus.APPLIED

    def to_dict(self) -> dict:
        """Convert the dataclass to a dictionary."""
        result = asdict(self)
        result['status'] = self.status.name
        result['date'] = str(self.date)
        return result

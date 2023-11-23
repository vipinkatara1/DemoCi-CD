from pydantic import BaseModel, StrictInt, Field, EmailStr, AnyHttpUrl
from datetime import datetime


class Email(BaseModel):
    id: str | None = None
    lead_id: str | None = None
    experience_id: str | None = None
    email: EmailStr
    email_hash: str | None = None
    score: int | None = None
    verified: bool | None = None
    domain_type: str | None = None
    domain: str | None = None
    suggested: bool | None = None
    status_sugg_verification: str | None = None
    feedback_up: int | None = None
    feedback_down: int | None = None
    added_at: datetime | None = None
    updated_at: datetime | None = None


class Experience(BaseModel):
    experience_id: str | None = None
    lead_id: str | None = None
    title_id: str | None = None
    company_id: str | None = None
    company_fullname: str | None = None
    location: str | None = None
    date_start: str | None = None
    date_end: str | None = None
    is_current: bool | None = None
    description: str | None = None
    added_at: datetime | None = None
    updated_at: datetime | None = None
    status: str | None = None
    title: str | None = None
    company_uid: str | None = None
    domain: str | None = None


class Education(BaseModel):
    id: str | None = None
    lead_id: str | None = None
    organization_id: str | None = None
    degree_id: str | None = None
    major_id: str | None = None
    date_start: str | None = None
    date_end: str | None = None
    added_at: datetime | None = None
    updated_at: datetime | None = None
    organization: str | None = None
    degree: str | None = None
    major: str | None = None


class Skills(BaseModel):
    skill_id: str | None = None
    added_at: datetime | None = None
    score: int | None = None
    name: str | None = None


class Websites(BaseModel):
    id: str | None = None
    lead_id: str | None = None
    name: str | None = None
    url: AnyHttpUrl | None = None
    url_std: str | None = None
    url_std_hash: str | None = None
    source: str | None = None
    feedback_up: int | None = None
    feedback_down: int | None = None
    added_at: datetime | None = None
    updated_at: datetime | None = None


class Address(BaseModel):
    state_id: int | None = None
    city_id: int | None = None
    address_line1: str | None = None
    address_line2: str | None = None
    city: str | None = None
    state: str | None = None
    postal_code: str | None = None
    country_code: str | None = None
    lat: float | None = None
    lon: float | None = None
    country: str | None = None


class Phone(BaseModel):
    id:	str | None = None
    lead_id:	str | None = None
    phone:	str | None = None
    verified:	bool | None = None
    score:	int | None = None
    label:	str | None = None
    feedback_up:	int | None = None
    feedback_down:	int | None = None
    added_at:	datetime | None = None
    updated_at:	datetime | None = None


class JobDescription(BaseModel):
    company_name: str
    job_title: str
    job_location: str
    job_type: str
    job_qualifications: str
    job_responsibilities: str
    job_benefits: str | None = None


class MainBody(BaseModel):
    lead_id:	str | None = None
    lead_uid:	str | None = None
    fname:	str | None = None
    lname:	str | None = None
    picture_url:	AnyHttpUrl | None = None
    gender:	str | None = None
    yob:	str | None = None
    summary:	str | None = None
    job_desc: JobDescription
    job_type:	str | None = None
    experience_years:	float | None = None
    experience_avg:	float | None = None
    education_score:	int | None = None
    completeness:	int | None = None
    do_not_contact:	bool | None = None
    added_at:	datetime | None = None
    updated_at:	datetime | None = None
    update_check_at:	datetime | None = None
    update_check_source:	str | None = None
    is_pdl:	int | None = None
    is_pdl_total:	int | None = None
    added_at_ago:	str | None = None
    updated_at_ago:	str | None = None
    update_check_at_ago:	str | None = None
    experience_avg_formatted:	str | None = None
    emails:	list[Email] = []
    phones:	list[Phone] = []
    videos:	list = []
    is_contact_lead:	int | None = None
    is_contact_lead_added_at:	datetime | None = None
    is_contact_lead_added_at_ago:	str | None = None
    listings:	list = []
    listings_count:	int | None = None
    listings_latest_added_at:	datetime | None = None
    listings_latest_added_at_ago:	str | None = None
    is_bookmark_lead:	int | None = None
    is_bookmark_lead_rating:	str | None = None
    is_bookmark_lead_added_at:	str | None = None
    is_bookmark_lead_added_at_ago:	str | None = None
    industries:	list = []
    experiences:	list[Experience] = []
    educations:	list[Education] = []
    skills:	list[Skills] = []
    interests:	list = []
    militaries:	list = []
    tags:	list = []
    notes:	list = []
    websites:	list[Websites] = []
    linkedin:	AnyHttpUrl | None = None
    address:	Address | None = None
    timeline:	list = []
    survey:	str | None = None

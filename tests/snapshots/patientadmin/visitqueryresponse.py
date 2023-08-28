# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_parser_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class VisitQueryResponse(EventTypeAbstractModel):
    Meta: "VisitQueryResponseMeta" = Field(...)
    Patients: List["VisitQueryResponsePatient"] = Field(None)


class VisitQueryResponseMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["VisitQueryResponseMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["VisitQueryResponseMetaLog"] = Field(None)
    Message: "VisitQueryResponseMetaMessage" = Field(None)
    Source: "VisitQueryResponseMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "VisitQueryResponseMetaTransmission" = Field(None)


class VisitQueryResponseMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class VisitQueryResponseMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class VisitQueryResponseMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class VisitQueryResponseMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class VisitQueryResponseMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class VisitQueryResponsePatient(RedoxAbstractModel):
    Demographics: "VisitQueryResponsePatientDemographics" = Field(None)
    Identifiers: List["VisitQueryResponsePatientIdentifier"] = Field(None)
    Visits: List["VisitQueryResponsePatientVisit"] = Field(None)


class VisitQueryResponsePatientDemographics(RedoxAbstractModel):
    Address: "VisitQueryResponsePatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DOB: Union[str, None] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "VisitQueryResponsePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class VisitQueryResponsePatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class VisitQueryResponsePatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class VisitQueryResponsePatientIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class VisitQueryResponsePatientVisit(RedoxAbstractModel):
    Location: "VisitQueryResponsePatientVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    Reason: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class VisitQueryResponsePatientVisitLocation(RedoxAbstractModel):
    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "VisitQueryResponsePatientVisitLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "VisitQueryResponsePatientVisitLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class VisitQueryResponsePatientVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class VisitQueryResponsePatientVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


VisitQueryResponse.update_forward_refs()
VisitQueryResponseMeta.update_forward_refs()
VisitQueryResponsePatient.update_forward_refs()
VisitQueryResponsePatientDemographics.update_forward_refs()
VisitQueryResponsePatientVisit.update_forward_refs()
VisitQueryResponsePatientVisitLocation.update_forward_refs()

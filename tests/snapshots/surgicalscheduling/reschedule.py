# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_parser_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Reschedule(EventTypeAbstractModel):
    Meta: "RescheduleMeta" = Field(...)
    Patient: "ReschedulePatient" = Field(...)
    Procedures: List["RescheduleProcedure"] = Field(...)
    SurgeryStaff: List["RescheduleSurgeryStaff"] = Field(None)
    SurgicalCase: "RescheduleSurgicalCase" = Field(None)
    SurgicalInfo: List["RescheduleSurgicalInfo"] = Field(None)
    Visit: "RescheduleVisit" = Field(...)


class RescheduleMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["RescheduleMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["RescheduleMetaLog"] = Field(None)
    Message: "RescheduleMetaMessage" = Field(None)
    Source: "RescheduleMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "RescheduleMetaTransmission" = Field(None)


class RescheduleMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class RescheduleMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class RescheduleMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class RescheduleMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class RescheduleMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class ReschedulePatient(RedoxAbstractModel):
    Demographics: "ReschedulePatientDemographics" = Field(None)
    Identifiers: List["ReschedulePatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class ReschedulePatientDemographics(RedoxAbstractModel):
    Address: "ReschedulePatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "ReschedulePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class ReschedulePatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class ReschedulePatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class ReschedulePatientIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class RescheduleProcedure(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DateTime: str = Field(...)
    Description: Union[str, None] = Field(None)
    Duration: Number = Field(...)
    ProcedureInfo: List["RescheduleProcedureProcedureInfo"] = Field(None)


class RescheduleProcedureProcedureInfo(RedoxAbstractModel):
    Description: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class RescheduleSurgeryStaff(RedoxAbstractModel):
    Address: "RescheduleSurgeryStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    Duration: Union[Number, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "RescheduleSurgeryStaffLocation" = Field(None)
    PhoneNumber: "RescheduleSurgeryStaffPhoneNumber" = Field(None)
    Role: "RescheduleSurgeryStaffRole" = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class RescheduleSurgeryStaffAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class RescheduleSurgeryStaffLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "RescheduleSurgeryStaffLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "RescheduleSurgeryStaffLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleSurgeryStaffLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class RescheduleSurgeryStaffLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class RescheduleSurgeryStaffPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class RescheduleSurgeryStaffRole(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class RescheduleSurgicalCase(RedoxAbstractModel):
    Number: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)


class RescheduleSurgicalInfo(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class RescheduleVisit(RedoxAbstractModel):
    AccountNumber: Union[str, None] = Field(None)
    AttendingProvider: "RescheduleVisitAttendingProvider" = Field(None)
    Diagnoses: List["RescheduleVisitDiagnosis"] = Field(None)
    Duration: Union[Number, None] = Field(None)
    Equipment: List["RescheduleVisitEquipment"] = Field(None)
    Location: "RescheduleVisitLocation" = Field(...)
    Notes: List[str] = Field(None)
    PatientClass: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: str = Field(...)


class RescheduleVisitAttendingProvider(RedoxAbstractModel):
    Address: "RescheduleVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "RescheduleVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "RescheduleVisitAttendingProviderPhoneNumber" = Field(None)


class RescheduleVisitAttendingProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class RescheduleVisitAttendingProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "RescheduleVisitAttendingProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "RescheduleVisitAttendingProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleVisitAttendingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class RescheduleVisitAttendingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class RescheduleVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class RescheduleVisitDiagnosis(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleVisitEquipment(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Duration: Union[Number, None] = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class RescheduleVisitLocation(RedoxAbstractModel):
    Bed: Union[str, None] = Field(None)
    Department: str = Field(...)
    DepartmentIdentifiers: List["RescheduleVisitLocationDepartmentIdentifier"] = Field(
        None
    )
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["RescheduleVisitLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class RescheduleVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


Reschedule.update_forward_refs()
RescheduleMeta.update_forward_refs()
ReschedulePatient.update_forward_refs()
ReschedulePatientDemographics.update_forward_refs()
RescheduleProcedure.update_forward_refs()
RescheduleSurgeryStaff.update_forward_refs()
RescheduleSurgeryStaffLocation.update_forward_refs()
RescheduleVisit.update_forward_refs()
RescheduleVisitAttendingProvider.update_forward_refs()
RescheduleVisitAttendingProviderLocation.update_forward_refs()
RescheduleVisitLocation.update_forward_refs()

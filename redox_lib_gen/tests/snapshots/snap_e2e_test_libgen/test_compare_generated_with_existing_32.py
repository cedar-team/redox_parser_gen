# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..field_types import Number
from ..redox_abstract_model import RedoxAbstractModel


class Reschedule(RedoxAbstractModel):

    AppointmentInfo: List["RescheduleAppointmentInfo"] = Field(None)
    Meta: "RescheduleMeta" = Field(...)
    Patient: "ReschedulePatient" = Field(None)
    Visit: "RescheduleVisit" = Field(...)


class RescheduleAppointmentInfo(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


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
    Identifiers: List["ReschedulePatientIdentifier"] = Field(None)
    Notes: List[str] = Field(None)


class ReschedulePatientDemographics(RedoxAbstractModel):

    Address: "ReschedulePatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    DOB: Union[str, None] = Field(None)
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
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


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

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class RescheduleVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AdditionalStaff: List["RescheduleVisitAdditionalStaff"] = Field(None)
    AttendingProvider: "RescheduleVisitAttendingProvider" = Field(None)
    ConsultingProvider: "RescheduleVisitConsultingProvider" = Field(None)
    Diagnoses: List["RescheduleVisitDiagnosis"] = Field(None)
    Duration: Number = Field(...)
    Equipment: List["RescheduleVisitEquipment"] = Field(None)
    Instructions: List[str] = Field(None)
    Location: "RescheduleVisitLocation" = Field(...)
    OldDateTime: Union[str, None] = Field(None)
    OldVisitNumber: Union[str, None] = Field(None)
    PatientClass: Union[str, None] = Field(None)
    Reason: Union[str, None] = Field(None)
    ReferringProvider: "RescheduleVisitReferringProvider" = Field(None)
    Status: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    VisitDateTime: str = Field(...)
    VisitNumber: str = Field(...)
    VisitProvider: "RescheduleVisitVisitProvider" = Field(None)


class RescheduleVisitAdditionalStaff(RedoxAbstractModel):

    Address: "RescheduleVisitAdditionalStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    Duration: Union[Number, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "RescheduleVisitAdditionalStaffLocation" = Field(None)
    PhoneNumber: "RescheduleVisitAdditionalStaffPhoneNumber" = Field(None)
    Role: "RescheduleVisitAdditionalStaffRole" = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class RescheduleVisitAdditionalStaffAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class RescheduleVisitAdditionalStaffLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class RescheduleVisitAdditionalStaffRole(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


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
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class RescheduleVisitConsultingProvider(RedoxAbstractModel):

    Address: "RescheduleVisitConsultingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "RescheduleVisitConsultingProviderLocation" = Field(None)
    PhoneNumber: "RescheduleVisitConsultingProviderPhoneNumber" = Field(None)


class RescheduleVisitConsultingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class RescheduleVisitConsultingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleVisitConsultingProviderPhoneNumber(RedoxAbstractModel):

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

    Department: str = Field(...)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleVisitReferringProvider(RedoxAbstractModel):

    Address: "RescheduleVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "RescheduleVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "RescheduleVisitReferringProviderPhoneNumber" = Field(None)


class RescheduleVisitReferringProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class RescheduleVisitReferringProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleVisitReferringProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class RescheduleVisitVisitProvider(RedoxAbstractModel):

    Address: "RescheduleVisitVisitProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "RescheduleVisitVisitProviderLocation" = Field(None)
    PhoneNumber: "RescheduleVisitVisitProviderPhoneNumber" = Field(None)


class RescheduleVisitVisitProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class RescheduleVisitVisitProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class RescheduleVisitVisitProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


Reschedule.update_forward_refs()
RescheduleMeta.update_forward_refs()
ReschedulePatient.update_forward_refs()
ReschedulePatientDemographics.update_forward_refs()
RescheduleVisit.update_forward_refs()
RescheduleVisitAdditionalStaff.update_forward_refs()
RescheduleVisitAttendingProvider.update_forward_refs()
RescheduleVisitConsultingProvider.update_forward_refs()
RescheduleVisitReferringProvider.update_forward_refs()
RescheduleVisitVisitProvider.update_forward_refs()

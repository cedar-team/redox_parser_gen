# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_parser_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Delete(EventTypeAbstractModel):
    Meta: "DeleteMeta" = Field(...)
    Note: "DeleteNote" = Field(...)
    Orders: List["DeleteOrder"] = Field(None)
    Patient: "DeletePatient" = Field(...)
    Visit: "DeleteVisit" = Field(None)


class DeleteMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["DeleteMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["DeleteMetaLog"] = Field(None)
    Message: "DeleteMetaMessage" = Field(None)
    Source: "DeleteMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "DeleteMetaTransmission" = Field(None)


class DeleteMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DeleteMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class DeleteMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class DeleteMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DeleteMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class DeleteNote(RedoxAbstractModel):
    Authenticator: "DeleteNoteAuthenticator" = Field(None)
    Availability: Union[str, None] = Field(None)
    Components: List["DeleteNoteComponent"] = Field(None)
    ContentType: str = Field(...)
    DocumentDescription: Union[str, None] = Field(None)
    DocumentID: str = Field(...)
    DocumentType: str = Field(...)
    DocumentationDateTime: Union[str, None] = Field(None)
    FileName: Union[str, None] = Field(None)
    FileType: Union[str, None] = Field(None)
    Notifications: List["DeleteNoteNotification"] = Field(None)
    Provider: "DeleteNoteProvider" = Field(...)
    ServiceDateTime: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)


class DeleteNoteAuthenticator(RedoxAbstractModel):
    Address: "DeleteNoteAuthenticatorAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DeleteNoteAuthenticatorLocation" = Field(None)
    PhoneNumber: "DeleteNoteAuthenticatorPhoneNumber" = Field(None)


class DeleteNoteAuthenticatorAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DeleteNoteAuthenticatorLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "DeleteNoteAuthenticatorLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "DeleteNoteAuthenticatorLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DeleteNoteAuthenticatorLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DeleteNoteAuthenticatorLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DeleteNoteAuthenticatorPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class DeleteNoteComponent(RedoxAbstractModel):
    Comments: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class DeleteNoteNotification(RedoxAbstractModel):
    Address: "DeleteNoteNotificationAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DeleteNoteNotificationLocation" = Field(None)
    PhoneNumber: "DeleteNoteNotificationPhoneNumber" = Field(None)


class DeleteNoteNotificationAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DeleteNoteNotificationLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "DeleteNoteNotificationLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "DeleteNoteNotificationLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DeleteNoteNotificationLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DeleteNoteNotificationLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DeleteNoteNotificationPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class DeleteNoteProvider(RedoxAbstractModel):
    Address: "DeleteNoteProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: str = Field(...)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DeleteNoteProviderLocation" = Field(None)
    PhoneNumber: "DeleteNoteProviderPhoneNumber" = Field(None)


class DeleteNoteProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DeleteNoteProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "DeleteNoteProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["DeleteNoteProviderLocationFacilityIdentifier"] = Field(
        None
    )
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DeleteNoteProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DeleteNoteProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DeleteNoteProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class DeleteOrder(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DeletePatient(RedoxAbstractModel):
    Demographics: "DeletePatientDemographics" = Field(None)
    Identifiers: List["DeletePatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class DeletePatientDemographics(RedoxAbstractModel):
    Address: "DeletePatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "DeletePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class DeletePatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DeletePatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class DeletePatientIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class DeleteVisit(RedoxAbstractModel):
    AccountNumber: Union[str, None] = Field(None)
    AdditionalStaff: List["DeleteVisitAdditionalStaff"] = Field(None)
    Location: "DeleteVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class DeleteVisitAdditionalStaff(RedoxAbstractModel):
    Address: "DeleteVisitAdditionalStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DeleteVisitAdditionalStaffLocation" = Field(None)
    PhoneNumber: "DeleteVisitAdditionalStaffPhoneNumber" = Field(None)
    Role: "DeleteVisitAdditionalStaffRole" = Field(None)


class DeleteVisitAdditionalStaffAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DeleteVisitAdditionalStaffLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "DeleteVisitAdditionalStaffLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "DeleteVisitAdditionalStaffLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DeleteVisitAdditionalStaffLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DeleteVisitAdditionalStaffLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DeleteVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class DeleteVisitAdditionalStaffRole(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class DeleteVisitLocation(RedoxAbstractModel):
    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List["DeleteVisitLocationDepartmentIdentifier"] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["DeleteVisitLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DeleteVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DeleteVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


Delete.update_forward_refs()
DeleteMeta.update_forward_refs()
DeleteNote.update_forward_refs()
DeleteNoteAuthenticator.update_forward_refs()
DeleteNoteAuthenticatorLocation.update_forward_refs()
DeleteNoteNotification.update_forward_refs()
DeleteNoteNotificationLocation.update_forward_refs()
DeleteNoteProvider.update_forward_refs()
DeleteNoteProviderLocation.update_forward_refs()
DeletePatient.update_forward_refs()
DeletePatientDemographics.update_forward_refs()
DeleteVisit.update_forward_refs()
DeleteVisitAdditionalStaff.update_forward_refs()
DeleteVisitAdditionalStaffLocation.update_forward_refs()
DeleteVisitLocation.update_forward_refs()

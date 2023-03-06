# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from pyredox import clinicaldecisions
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _ClinicalDecisions(GenericEventTypeAbstractModel):
    _redox_module = clinicaldecisions


class Request(_ClinicalDecisions):
    AuthorizingProvider: generic.AuthorizingProvider = Field(None)
    Meta: generic.Meta = Field(...)
    OrderingProvider: generic.OrderingProvider = Field(None)
    Patient: generic.Patient = Field(...)
    Session: generic.Session = Field(None)
    UnsignedMedicationOrders: List[generic.UnsignedMedicationOrder] = Field(...)
    UnsignedProcedureOrders: List[generic.UnsignedProcedureOrder] = Field(...)


class Response(_ClinicalDecisions):
    Advisories: List[generic.Advisory] = Field(...)
    Meta: generic.Meta = Field(...)

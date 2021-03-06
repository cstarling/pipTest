# Python stubs generated by omniidl from DCM_Types.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "_GlobalIDL"
#
__name__ = "_GlobalIDL"
_0__GlobalIDL = omniORB.openModule("_GlobalIDL", r"DCM_Types.idl")
_0__GlobalIDL__POA = omniORB.openModule("_GlobalIDL__POA", r"DCM_Types.idl")


# enum eBoardType
_0__GlobalIDL.BoardType_GbE = omniORB.EnumItem("BoardType_GbE", 0)
_0__GlobalIDL.BoardType_ASI = omniORB.EnumItem("BoardType_ASI", 1)
_0__GlobalIDL.eBoardType = omniORB.Enum("IDL:eBoardType:1.0", (_0__GlobalIDL.BoardType_GbE, _0__GlobalIDL.BoardType_ASI,))

_0__GlobalIDL._d_eBoardType  = (omniORB.tcInternal.tv_enum, _0__GlobalIDL.eBoardType._NP_RepositoryId, "eBoardType", _0__GlobalIDL.eBoardType._items)
_0__GlobalIDL._tc_eBoardType = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_eBoardType)
omniORB.registerType(_0__GlobalIDL.eBoardType._NP_RepositoryId, _0__GlobalIDL._d_eBoardType, _0__GlobalIDL._tc_eBoardType)

# enum eBoardType_V2
_0__GlobalIDL.BoardType_V2_GbE = omniORB.EnumItem("BoardType_V2_GbE", 0)
_0__GlobalIDL.BoardType_V2_ASI = omniORB.EnumItem("BoardType_V2_ASI", 1)
_0__GlobalIDL.BoardType_V2_IP_AdapterVideo = omniORB.EnumItem("BoardType_V2_IP_AdapterVideo", 2)
_0__GlobalIDL.BoardType_V2_ASI_SFN = omniORB.EnumItem("BoardType_V2_ASI_SFN", 3)
_0__GlobalIDL.BoardType_V2_TC = omniORB.EnumItem("BoardType_V2_TC", 4)
_0__GlobalIDL.BoardType_V2_GbE_GW = omniORB.EnumItem("BoardType_V2_GbE_GW", 5)
_0__GlobalIDL.BoardType_V2_ASI_GW = omniORB.EnumItem("BoardType_V2_ASI_GW", 6)
_0__GlobalIDL.BoardType_V2_9036_VSE_APP = omniORB.EnumItem("BoardType_V2_9036_VSE_APP", 7)
_0__GlobalIDL.BoardType_V2_9036_MIO = omniORB.EnumItem("BoardType_V2_9036_MIO", 8)
_0__GlobalIDL.BoardType_V2_9036_MVI = omniORB.EnumItem("BoardType_V2_9036_MVI", 9)
_0__GlobalIDL.BoardType_V2_9036_MVC = omniORB.EnumItem("BoardType_V2_9036_MVC", 10)
_0__GlobalIDL.BoardType_V2_9036_MVA = omniORB.EnumItem("BoardType_V2_9036_MVA", 11)
_0__GlobalIDL.BoardType_V2_DRD_VSB = omniORB.EnumItem("BoardType_V2_DRD_VSB", 12)
_0__GlobalIDL.BoardType_V2_MFP = omniORB.EnumItem("BoardType_V2_MFP", 13)
_0__GlobalIDL.BoardType_V2_SFN_MKII = omniORB.EnumItem("BoardType_V2_SFN_MKII", 14)
_0__GlobalIDL.BoardType_V2_DRD_DVBS2 = omniORB.EnumItem("BoardType_V2_DRD_DVBS2", 15)
_0__GlobalIDL.BoardType_V2_9036_PCA = omniORB.EnumItem("BoardType_V2_9036_PCA", 16)
_0__GlobalIDL.BoardType_V2_IP_AdapterAudio = omniORB.EnumItem("BoardType_V2_IP_AdapterAudio", 17)
_0__GlobalIDL.BoardType_V2_DGIO10_IN = omniORB.EnumItem("BoardType_V2_DGIO10_IN", 18)
_0__GlobalIDL.BoardType_V2_DGIO10_OUT = omniORB.EnumItem("BoardType_V2_DGIO10_OUT", 19)
_0__GlobalIDL.BoardType_V2_MFP2 = omniORB.EnumItem("BoardType_V2_MFP2", 20)
_0__GlobalIDL.BoardType_V2_DGIO10_GbE = omniORB.EnumItem("BoardType_V2_DGIO10_GbE", 21)
_0__GlobalIDL.BoardType_V2_DGIO10_SdiIn = omniORB.EnumItem("BoardType_V2_DGIO10_SdiIn", 22)
_0__GlobalIDL.BoardType_V2_XGRESS = omniORB.EnumItem("BoardType_V2_XGRESS", 23)
_0__GlobalIDL.BoardType_V2_XCODE = omniORB.EnumItem("BoardType_V2_XCODE", 24)
_0__GlobalIDL.BoardType_V2_DGIO10_Proc = omniORB.EnumItem("BoardType_V2_DGIO10_Proc", 25)
_0__GlobalIDL.BoardType_V2_VIRTUAL_MFP = omniORB.EnumItem("BoardType_V2_VIRTUAL_MFP", 26)
_0__GlobalIDL.ReservedBoardType_V2_28 = omniORB.EnumItem("ReservedBoardType_V2_28", 27)
_0__GlobalIDL.ReservedBoardType_V2_29 = omniORB.EnumItem("ReservedBoardType_V2_29", 28)
_0__GlobalIDL.ReservedBoardType_V2_Unknown = omniORB.EnumItem("ReservedBoardType_V2_Unknown", 29)
_0__GlobalIDL.eBoardType_V2 = omniORB.Enum("IDL:eBoardType_V2:1.0", (_0__GlobalIDL.BoardType_V2_GbE, _0__GlobalIDL.BoardType_V2_ASI, _0__GlobalIDL.BoardType_V2_IP_AdapterVideo, _0__GlobalIDL.BoardType_V2_ASI_SFN, _0__GlobalIDL.BoardType_V2_TC, _0__GlobalIDL.BoardType_V2_GbE_GW, _0__GlobalIDL.BoardType_V2_ASI_GW, _0__GlobalIDL.BoardType_V2_9036_VSE_APP, _0__GlobalIDL.BoardType_V2_9036_MIO, _0__GlobalIDL.BoardType_V2_9036_MVI, _0__GlobalIDL.BoardType_V2_9036_MVC, _0__GlobalIDL.BoardType_V2_9036_MVA, _0__GlobalIDL.BoardType_V2_DRD_VSB, _0__GlobalIDL.BoardType_V2_MFP, _0__GlobalIDL.BoardType_V2_SFN_MKII, _0__GlobalIDL.BoardType_V2_DRD_DVBS2, _0__GlobalIDL.BoardType_V2_9036_PCA, _0__GlobalIDL.BoardType_V2_IP_AdapterAudio, _0__GlobalIDL.BoardType_V2_DGIO10_IN, _0__GlobalIDL.BoardType_V2_DGIO10_OUT, _0__GlobalIDL.BoardType_V2_MFP2, _0__GlobalIDL.BoardType_V2_DGIO10_GbE, _0__GlobalIDL.BoardType_V2_DGIO10_SdiIn, _0__GlobalIDL.BoardType_V2_XGRESS, _0__GlobalIDL.BoardType_V2_XCODE, _0__GlobalIDL.BoardType_V2_DGIO10_Proc, _0__GlobalIDL.BoardType_V2_VIRTUAL_MFP, _0__GlobalIDL.ReservedBoardType_V2_28, _0__GlobalIDL.ReservedBoardType_V2_29, _0__GlobalIDL.ReservedBoardType_V2_Unknown,))

_0__GlobalIDL._d_eBoardType_V2  = (omniORB.tcInternal.tv_enum, _0__GlobalIDL.eBoardType_V2._NP_RepositoryId, "eBoardType_V2", _0__GlobalIDL.eBoardType_V2._items)
_0__GlobalIDL._tc_eBoardType_V2 = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_eBoardType_V2)
omniORB.registerType(_0__GlobalIDL.eBoardType_V2._NP_RepositoryId, _0__GlobalIDL._d_eBoardType_V2, _0__GlobalIDL._tc_eBoardType_V2)

# enum ePsigType
_0__GlobalIDL.SaPsig = omniORB.EnumItem("SaPsig", 0)
_0__GlobalIDL.CaVendorPsig = omniORB.EnumItem("CaVendorPsig", 1)
_0__GlobalIDL.ePsigType = omniORB.Enum("IDL:ePsigType:1.0", (_0__GlobalIDL.SaPsig, _0__GlobalIDL.CaVendorPsig,))

_0__GlobalIDL._d_ePsigType  = (omniORB.tcInternal.tv_enum, _0__GlobalIDL.ePsigType._NP_RepositoryId, "ePsigType", _0__GlobalIDL.ePsigType._items)
_0__GlobalIDL._tc_ePsigType = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_ePsigType)
omniORB.registerType(_0__GlobalIDL.ePsigType._NP_RepositoryId, _0__GlobalIDL._d_ePsigType, _0__GlobalIDL._tc_ePsigType)

#
# Start of module "DCM"
#
__name__ = "DCM"
_0_DCM = omniORB.openModule("DCM", r"DCM_Types.idl")
_0_DCM__POA = omniORB.openModule("DCM__POA", r"DCM_Types.idl")


# interface BaseControl
_0_DCM._d_BaseControl = (omniORB.tcInternal.tv_objref, "IDL:DCM/BaseControl:1.0", "BaseControl")
omniORB.typeMapping["IDL:DCM/BaseControl:1.0"] = _0_DCM._d_BaseControl
_0_DCM.BaseControl = omniORB.newEmptyClass()
class BaseControl :
    _NP_RepositoryId = _0_DCM._d_BaseControl[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_DCM.BaseControl = BaseControl
_0_DCM._tc_BaseControl = omniORB.tcInternal.createTypeCode(_0_DCM._d_BaseControl)
omniORB.registerType(BaseControl._NP_RepositoryId, _0_DCM._d_BaseControl, _0_DCM._tc_BaseControl)

# BaseControl object reference
class _objref_BaseControl (CORBA.Object):
    _NP_RepositoryId = BaseControl._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

omniORB.registerObjref(BaseControl._NP_RepositoryId, _objref_BaseControl)
_0_DCM._objref_BaseControl = _objref_BaseControl
del BaseControl, _objref_BaseControl

# BaseControl skeleton
__name__ = "DCM__POA"
class BaseControl (PortableServer.Servant):
    _NP_RepositoryId = _0_DCM.BaseControl._NP_RepositoryId


    _omni_op_d = {}

BaseControl._omni_skeleton = BaseControl
_0_DCM__POA.BaseControl = BaseControl
omniORB.registerSkeleton(BaseControl._NP_RepositoryId, BaseControl)
del BaseControl
__name__ = "DCM"

# exception MaxClientsReached
_0_DCM.MaxClientsReached = omniORB.newEmptyClass()
class MaxClientsReached (CORBA.UserException):
    _NP_RepositoryId = "IDL:DCM/MaxClientsReached:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_DCM.MaxClientsReached = MaxClientsReached
_0_DCM._d_MaxClientsReached  = (omniORB.tcInternal.tv_except, MaxClientsReached, MaxClientsReached._NP_RepositoryId, "MaxClientsReached")
_0_DCM._tc_MaxClientsReached = omniORB.tcInternal.createTypeCode(_0_DCM._d_MaxClientsReached)
omniORB.registerType(MaxClientsReached._NP_RepositoryId, _0_DCM._d_MaxClientsReached, _0_DCM._tc_MaxClientsReached)
del MaxClientsReached

# exception TimeOut
_0_DCM.TimeOut = omniORB.newEmptyClass()
class TimeOut (CORBA.UserException):
    _NP_RepositoryId = "IDL:DCM/TimeOut:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_DCM.TimeOut = TimeOut
_0_DCM._d_TimeOut  = (omniORB.tcInternal.tv_except, TimeOut, TimeOut._NP_RepositoryId, "TimeOut")
_0_DCM._tc_TimeOut = omniORB.tcInternal.createTypeCode(_0_DCM._d_TimeOut)
omniORB.registerType(TimeOut._NP_RepositoryId, _0_DCM._d_TimeOut, _0_DCM._tc_TimeOut)
del TimeOut

# exception OutOfRange
_0_DCM.OutOfRange = omniORB.newEmptyClass()
class OutOfRange (CORBA.UserException):
    _NP_RepositoryId = "IDL:DCM/OutOfRange:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_DCM.OutOfRange = OutOfRange
_0_DCM._d_OutOfRange  = (omniORB.tcInternal.tv_except, OutOfRange, OutOfRange._NP_RepositoryId, "OutOfRange")
_0_DCM._tc_OutOfRange = omniORB.tcInternal.createTypeCode(_0_DCM._d_OutOfRange)
omniORB.registerType(OutOfRange._NP_RepositoryId, _0_DCM._d_OutOfRange, _0_DCM._tc_OutOfRange)
del OutOfRange

# exception InvalidSelection
_0_DCM.InvalidSelection = omniORB.newEmptyClass()
class InvalidSelection (CORBA.UserException):
    _NP_RepositoryId = "IDL:DCM/InvalidSelection:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_DCM.InvalidSelection = InvalidSelection
_0_DCM._d_InvalidSelection  = (omniORB.tcInternal.tv_except, InvalidSelection, InvalidSelection._NP_RepositoryId, "InvalidSelection")
_0_DCM._tc_InvalidSelection = omniORB.tcInternal.createTypeCode(_0_DCM._d_InvalidSelection)
omniORB.registerType(InvalidSelection._NP_RepositoryId, _0_DCM._d_InvalidSelection, _0_DCM._tc_InvalidSelection)
del InvalidSelection

# exception OpNotSucceeded
_0_DCM.OpNotSucceeded = omniORB.newEmptyClass()
class OpNotSucceeded (CORBA.UserException):
    _NP_RepositoryId = "IDL:DCM/OpNotSucceeded:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_DCM.OpNotSucceeded = OpNotSucceeded
_0_DCM._d_OpNotSucceeded  = (omniORB.tcInternal.tv_except, OpNotSucceeded, OpNotSucceeded._NP_RepositoryId, "OpNotSucceeded")
_0_DCM._tc_OpNotSucceeded = omniORB.tcInternal.createTypeCode(_0_DCM._d_OpNotSucceeded)
omniORB.registerType(OpNotSucceeded._NP_RepositoryId, _0_DCM._d_OpNotSucceeded, _0_DCM._tc_OpNotSucceeded)
del OpNotSucceeded

# exception OpNotAllowed
_0_DCM.OpNotAllowed = omniORB.newEmptyClass()
class OpNotAllowed (CORBA.UserException):
    _NP_RepositoryId = "IDL:DCM/OpNotAllowed:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_DCM.OpNotAllowed = OpNotAllowed
_0_DCM._d_OpNotAllowed  = (omniORB.tcInternal.tv_except, OpNotAllowed, OpNotAllowed._NP_RepositoryId, "OpNotAllowed")
_0_DCM._tc_OpNotAllowed = omniORB.tcInternal.createTypeCode(_0_DCM._d_OpNotAllowed)
omniORB.registerType(OpNotAllowed._NP_RepositoryId, _0_DCM._d_OpNotAllowed, _0_DCM._tc_OpNotAllowed)
del OpNotAllowed

# exception OpNotSupported
_0_DCM.OpNotSupported = omniORB.newEmptyClass()
class OpNotSupported (CORBA.UserException):
    _NP_RepositoryId = "IDL:DCM/OpNotSupported:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_DCM.OpNotSupported = OpNotSupported
_0_DCM._d_OpNotSupported  = (omniORB.tcInternal.tv_except, OpNotSupported, OpNotSupported._NP_RepositoryId, "OpNotSupported")
_0_DCM._tc_OpNotSupported = omniORB.tcInternal.createTypeCode(_0_DCM._d_OpNotSupported)
omniORB.registerType(OpNotSupported._NP_RepositoryId, _0_DCM._d_OpNotSupported, _0_DCM._tc_OpNotSupported)
del OpNotSupported

# exception LicenseError
_0_DCM.LicenseError = omniORB.newEmptyClass()
class LicenseError (CORBA.UserException):
    _NP_RepositoryId = "IDL:DCM/LicenseError:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_DCM.LicenseError = LicenseError
_0_DCM._d_LicenseError  = (omniORB.tcInternal.tv_except, LicenseError, LicenseError._NP_RepositoryId, "LicenseError")
_0_DCM._tc_LicenseError = omniORB.tcInternal.createTypeCode(_0_DCM._d_LicenseError)
omniORB.registerType(LicenseError._NP_RepositoryId, _0_DCM._d_LicenseError, _0_DCM._tc_LicenseError)
del LicenseError

# exception OperationFailed
_0_DCM.OperationFailed = omniORB.newEmptyClass()
class OperationFailed (CORBA.UserException):
    _NP_RepositoryId = "IDL:DCM/OperationFailed:1.0"

    def __init__(self, Info):
        CORBA.UserException.__init__(self, Info)
        self.Info = Info

_0_DCM.OperationFailed = OperationFailed
_0_DCM._d_OperationFailed  = (omniORB.tcInternal.tv_except, OperationFailed, OperationFailed._NP_RepositoryId, "OperationFailed", "Info", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_octet, 0))
_0_DCM._tc_OperationFailed = omniORB.tcInternal.createTypeCode(_0_DCM._d_OperationFailed)
omniORB.registerType(OperationFailed._NP_RepositoryId, _0_DCM._d_OperationFailed, _0_DCM._tc_OperationFailed)
del OperationFailed

#
# End of module "DCM"
#
__name__ = "_GlobalIDL"


# typedef ... Uuid_t
class Uuid_t:
    _NP_RepositoryId = "IDL:Uuid_t:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.Uuid_t = Uuid_t
_0__GlobalIDL._d_Uuid_t  = (omniORB.tcInternal.tv_array, omniORB.tcInternal.tv_octet, 16)
_0__GlobalIDL._ad_Uuid_t = (omniORB.tcInternal.tv_alias, Uuid_t._NP_RepositoryId, "Uuid_t", (omniORB.tcInternal.tv_array, omniORB.tcInternal.tv_octet, 16))
_0__GlobalIDL._tc_Uuid_t = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_Uuid_t)
omniORB.registerType(Uuid_t._NP_RepositoryId, _0__GlobalIDL._ad_Uuid_t, _0__GlobalIDL._tc_Uuid_t)
del Uuid_t

# typedef ... UuidList_t
class UuidList_t:
    _NP_RepositoryId = "IDL:UuidList_t:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.UuidList_t = UuidList_t
_0__GlobalIDL._d_UuidList_t  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Uuid_t:1.0"], 0)
_0__GlobalIDL._ad_UuidList_t = (omniORB.tcInternal.tv_alias, UuidList_t._NP_RepositoryId, "UuidList_t", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Uuid_t:1.0"], 0))
_0__GlobalIDL._tc_UuidList_t = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_UuidList_t)
omniORB.registerType(UuidList_t._NP_RepositoryId, _0__GlobalIDL._ad_UuidList_t, _0__GlobalIDL._tc_UuidList_t)
del UuidList_t

#
# End of module "_GlobalIDL"
#
__name__ = "DCM_Types_idl"

_exported_modules = ( "DCM", "_GlobalIDL")

# The end.

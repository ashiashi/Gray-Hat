from ctypes import *
from test.test_buffer import struct
from ctypes.wintypes import LONG

BYTE = c_ubyte
WORD =c_ushort
DWORD =c_ulong
LPBYTE =POINTER(c_ubyte)
LPTSTR =POINTER(c_char)
HANDLE =c_void_p
PVOID       = c_void_p
ULONG_PTR   = c_ulong
LPVOID    = c_void_p
UINT_PTR  = c_ulong
SIZE_T    = c_ulong
DWORD64 = c_uint64

DEBUG_PROCESS =0x00000010
CREATE_NEW_CONSOLE          = 0x00000010
PROCESS_ALL_ACCESS          = 0x001F0FFF
INFINITE                    = 0xFFFFFFFF
DBG_CONTINUE                = 0x00010002
DBG_EXCEPTION_NOT_HANDLE    = 0x80010001
#CONTEXT_FULL                   = 0x00010007
#CONTEXT_DEBUG_REGISTERS        = 0x00010010
TH32CS_SNAPTHREAD   = 0x00000004
THREAD_ALL_ACCESS = 0x001F03FF
CONTEXT_AMD64 = 0x100000
CONTEXT_CONTROL = (CONTEXT_AMD64 | 0x1 )
CONTEXT_INTEGER = (CONTEXT_AMD64 | 0x2 )
CONTEXT_SEGMENTS = (CONTEXT_AMD64 | 0x4 )
CONTEXT_FLOATING_POINT = (CONTEXT_AMD64 | 0x8)
CONTEXT_DEBUG_REGISTERS = (CONTEXT_AMD64 | 0x10)
CONTEXT_FULL = ( CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_FLOATING_POINT )
CONTEXT_ALL = ( CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_SEGMENTS | CONTEXT_FLOATING_POINT | CONTEXT_DEBUG_REGISTERS)


class STARTUPINFO(Structure):
    _fields_=[
        ("cb",DWORD),
        ("lpReserved",LPTSTR),
        ("lpDesktop",LPTSTR),
        ("lpTitle",LPTSTR),
        ("dwX",DWORD),
        ("dwY",DWORD),
        ("dwXSize",DWORD),
        ("dwYSize",DWORD),
        ("dwXCountChars",DWORD),
        ("dwYCountChars",DWORD),
        ("dwFillAttribute",DWORD),
        ("dwFlags",DWORD),
        ("wShowWindow",WORD),
        ("cbReserved2",WORD),
        ("lpReserved2",LPBYTE),
        ("hStdInput",HANDLE),
        ("hStdOnput",HANDLE),
        ("hStdError",HANDLE),
        ]
class PROCESS_INFORMATION(Structure):
    _fields_=[
        ("hProcess",HANDLE),
        ("hThread",HANDLE),
        ("dwProcessId",DWORD),
        ("dwThreadId",DWORD),
        ]

# When the dwDebugEventCode is evaluated

class EXCEPTION_RECORD(Structure):
    pass

EXCEPTION_RECORD._fields_ = [
    ("ExceptionCode",           DWORD),
    ("ExceptionFlags",          DWORD),
    ("ExceptionRecord",         POINTER(EXCEPTION_RECORD)),
    ("ExceptionAddress",        PVOID),
    ("NumberParameters",        DWORD),
    ("ExceptionInformation",    ULONG_PTR * 15),
]

# Exceptions
class EXCEPTION_DEBUG_INFO(Structure):
    _fields_ = [
        ("ExceptionRecord", EXCEPTION_RECORD),
        ("dwFirstChance",   DWORD),
    ]

# it populates this union appropriately
class DEBUG_EVENT_UNION(Union):
    _fields_ = [
        ("Exception",           EXCEPTION_DEBUG_INFO),
#        ("CreateThread"         CREATE_THREAD_DEBUG_INFO),
#        ("CreateProcessInfo",   CREATE_PROCESS_DEBUG_INFO),
#        ("ExitThread",          EXIT_THREAD_DEBUG_INFO),
#        ("ExitProcess",         EXIT_PROCESS_DEBUG_INFO),
#        ("LoadDll",             LOAD_DLL_DEBUG_INFO),
#        ("UnloadDll",           UNLOAD_DLL_DEBUG_INFO),
#        ("DebugString",         OUTPUT_DEBUG_STRING_INFO),
#        ("RipInfo",             RIP_INFO),
    ]

# DEBUG_EVENT describes a debugging event
# that the debugger has trapped
class DEBUG_EVENT(Structure):
    _fields_ = [
        ("dwDebugEventCode",    DWORD),
        ("dwProcessId",         DWORD),
        ("dwThreadId",          DWORD),
        ("u",                   DEBUG_EVENT_UNION),
    ]
    
class THREADENTRY32(Structure):
    _fields_ = [
        ("dwSize",             DWORD),
        ("cntUsage",           DWORD),
        ("th32ThreadID",       DWORD),
        ("th32OwnerProcessID", DWORD),
        ("tpBasePri",          DWORD),
        ("tpDeltaPri",         DWORD),
        ("dwFlags",            DWORD),
    ]

class M128A(Structure):
    _fields_ = [
            ("Low", DWORD64),
            ("High", DWORD64)
    ] 

class XMM_SAVE_AREA32(Structure):
    _pack_ = 1 
    _fields_ = [  
                ('ControlWord', WORD), 
                ('StatusWord', WORD), 
                ('TagWord', BYTE), 
                ('Reserved1', BYTE), 
                ('ErrorOpcode', WORD), 
                ('ErrorOffset', DWORD), 
                ('ErrorSelector', WORD), 
                ('Reserved2', WORD), 
                ('DataOffset', DWORD), 
                ('DataSelector', WORD), 
                ('Reserved3', WORD), 
                ('MxCsr', DWORD), 
                ('MxCsr_Mask', DWORD), 
                ('FloatRegisters', M128A * 8), 
                ('XmmRegisters', M128A *16), 
                ('Reserved4', BYTE * 96)
    ] 
 

class DUMMYSTRUCTNAME(Structure):
    _fields_=[
              ("Header", M128A * 2),
              ("Legacy", M128A * 8),
              ("Xmm0", M128A),
              ("Xmm1", M128A),
              ("Xmm2", M128A),
              ("Xmm3", M128A),
              ("Xmm4", M128A),
              ("Xmm5", M128A),
              ("Xmm6", M128A),
              ("Xmm7", M128A),
              ("Xmm8", M128A),
              ("Xmm9", M128A),
              ("Xmm10", M128A),
              ("Xmm11", M128A),
              ("Xmm12", M128A),
              ("Xmm13", M128A),
              ("Xmm14", M128A),
              ("Xmm15", M128A)
    ]

class DUMMYUNIONNAME(Union):
    _fields_=[
              ("FltSave", XMM_SAVE_AREA32),
              ("DummyStruct", DUMMYSTRUCTNAME)
    ]
    
class WOW64_CONTEXT(Structure):
    _pack_ = 16
    _fields_ = [
            ("P1Home", DWORD64),
            ("P2Home", DWORD64),
            ("P3Home", DWORD64),
            ("P4Home", DWORD64),
            ("P5Home", DWORD64),
            ("P6Home", DWORD64),
 
            ("ContextFlags", DWORD),
            ("MxCsr", DWORD),
 
            ("SegCs", WORD),
            ("SegDs", WORD),
            ("SegEs", WORD),
            ("SegFs", WORD),
            ("SegGs", WORD),
            ("SegSs", WORD),
            ("EFlags", DWORD),
 
            ("Dr0", DWORD64),
            ("Dr1", DWORD64),
            ("Dr2", DWORD64),
            ("Dr3", DWORD64),
            ("Dr6", DWORD64),
            ("Dr7", DWORD64),
 
            ("Rax", DWORD64),
            ("Rcx", DWORD64),
            ("Rdx", DWORD64),
            ("Rbx", DWORD64),
            ("Rsp", DWORD64),
            ("Rbp", DWORD64),
            ("Rsi", DWORD64),
            ("Rdi", DWORD64),
            ("R8", DWORD64),
            ("R9", DWORD64),
            ("R10", DWORD64),
            ("R11", DWORD64),
            ("R12", DWORD64),
            ("R13", DWORD64),
            ("R14", DWORD64),
            ("R15", DWORD64),
            ("Rip", DWORD64),
 
            ("DebugControl", DWORD64),
            ("LastBranchToRip", DWORD64),
            ("LastBranchFromRip", DWORD64),
            ("LastExceptionToRip", DWORD64),
            ("LastExceptionFromRip", DWORD64),
 
            ("DUMMYUNIONNAME", DUMMYUNIONNAME),
 
            ("VectorRegister", M128A * 26),
            ("VectorControl", DWORD64)
    ]

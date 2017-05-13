import my_debugger
debugger = my_debugger.debugger()
#debugger.load(b"C:\\WINDOWS\\system32\\calc.exe")
pid = input('Enter the PID of the process to attach to:')
debugger.attach(int(pid))
list = debugger.enumerate_threads()
print("num of list array:%x"%len(list))
for thread in list:
    thread_context = debugger.get_thread_context(thread)
    print("[*] Dumping registers for thread ID: 0x%08x" % thread)
    print("[**] RIP: 0x%016x" % thread_context.Rip)
    print("[**] RSP: 0x%016x" % thread_context.Rsp)
    print("[**] RBP: 0x%016x" % thread_context.Rbp)
    print("[**] RAX: 0x%016x" % thread_context.Rax)
    print("[**] RBX: 0x%016x" % thread_context.Rbx)
    print("[**] RCX: 0x%016x" % thread_context.Rcx)
    print("[**] RDX: 0x%016x" % thread_context.Rdx)
    print("[**] ContextFlags: 0x%08x" % thread_context.ContextFlags)
    
    
    print("[*] END DUMP")
    
debugger.detach()

#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansiexkernel
IPKernelApp.launch_instance(kernel_class=jansiexkernel)

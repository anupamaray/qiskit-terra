# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.


"""
===============================
Utilities (:mod:`qiskit.utils`)
===============================

.. currentmodule:: qiskit.utils

.. autosummary::
   :toctree: ../stubs/

   deprecate_arguments
   deprecate_function
   local_hardware_info
   is_main_process
   apply_prefix
   detach_prefix
   wrap_method

Algorithm Utilities
===================

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   summarize_circuits
   get_entangler_map
   validate_entangler_map
   has_ibmq
   has_aer
   name_args
   algorithm_globals

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   QuantumInstance
   Entanglement

A QuantumInstance holds the Qiskit `backend` as well as a number of compile and
runtime parameters controlling circuit compilation and execution. Quantum
:mod:`algorithms <qiskit.algorithms>`
are run on a device or simulator by passing a QuantumInstance setup with the desired
backend etc.

A Entanglement holds the function for calculating the the entanglement capability
of a parametric circuit using Meyer-wallach measure and Von-Neumann measure
as required by the user.

Optional Depedency Checkers (:mod:`qiskit.utils.optionals`)
===========================================================

.. automodule:: qiskit.utils.optionals
"""

from .quantum_instance import QuantumInstance
from .deprecation import deprecate_arguments
from .deprecation import deprecate_function
from .multiprocessing import local_hardware_info
from .multiprocessing import is_main_process
from .units import apply_prefix, detach_prefix
from .classtools import wrap_method
from .lazy_tester import LazyDependencyManager, LazyImportTester, LazySubprocessTester

from . import optionals

from .circuit_utils import summarize_circuits, Entanglement
from .entangler_map import get_entangler_map, validate_entangler_map
from .backend_utils import has_ibmq, has_aer
from .name_unnamed_args import name_args
from .algorithm_globals import algorithm_globals


__all__ = [
    "LazyDependencyManager",
    "LazyImportTester",
    "LazySubprocessTester",
    "QuantumInstance",
    "summarize_circuits",
    "Entanglement",
    "get_entangler_map",
    "validate_entangler_map",
    "has_ibmq",
    "has_aer",
    "name_args",
    "algorithm_globals",
    "deprecate_arguments",
    "deprecate_function",
    "local_hardware_info",
    "is_main_process",
    "apply_prefix",
]

"""Semiotics registry and deterministic interpretation matching."""

from .engine import Registry, RegistryError, load_registry

__all__ = ["Registry", "RegistryError", "load_registry"]

# The Cube

The Cube is a symbolic state-space system combined with a dynamic field runtime.

## Structure

packages/

- cube-core  
  Symbolic hypercube system:
  - traversal
  - scoring
  - attractors
  - Hamiltonian paths
  - visualization

- field-core  
  Adaptive field runtime:
  - agents
  - attractors
  - topology
  - runtime loop
  - API (/state, /step, /seed_concept, /timeline)

## Architecture

concept → cube → vector → field → evolution over time

## Status

- cube-core: stable
- field-core: functional (v1)
- timeline tracking: active
- API: running

Further layers (apps, UI, persistence) will be added on top.

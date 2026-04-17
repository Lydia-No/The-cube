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
  - API

apps/

- arctopia  
  Governance and legitimacy application layer (scaffolded)

- ecoarq  
  Ecological sensing and verification application layer (scaffolded)

- realert  
  Monitoring and alert application layer (scaffolded)

## Architecture

concept → cube → vector → field → evolution over time

## Status

- cube-core: stable
- field-core: functional (v1)
- apps layer: scaffolded

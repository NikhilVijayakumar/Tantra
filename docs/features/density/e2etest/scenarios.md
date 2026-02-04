# Density Module E2E Scenarios

## Overview
These scenarios verify the Density Analyzer's ability to calculate information density and entropy.

## Scenarios

### 1. Happy Path: Information Density
**ID:** DEN-E2E-001
**Description:** Verify density calculation.
**Input:** "This is a sentence with information."
**Expected Output:**
- `entropy`: Float > 0.
- `density_score`: Float.

### 2. Corner Case: Repetitive Text
**ID:** DEN-E2E-002
**Description:** Verify low entropy.
**Input:** "A A A A A."
**Expected Output:**
- `entropy`: Low or Zero.

### 3. Edge Case: Empty Input
**ID:** DEN-E2E-003
**Description:** Verify empty input.
**Input:** ""
**Expected Output:**
- `entropy`: 0.0

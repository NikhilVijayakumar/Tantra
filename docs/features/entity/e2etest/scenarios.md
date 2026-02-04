# Entity Module E2E Scenarios

## Overview
These scenarios verify the end-to-end functionality of the Entity Analyzer, ensuring it identifies named entities in text.

## Scenarios

### 1. Happy Path: Standard Extraction
**ID:** ENT-E2E-001
**Description:** Verify extraction of known entities.
**Input:** "Apple Inc. is testing a new iPhone."
**Expected Output:**
- `entities`: Dictionary containing detected entities.
- `ORG`: Should contain "Apple Inc.".

### 2. Corner Case: Empty Input
**ID:** ENT-E2E-002
**Description:** Verify behavior when analyzing empty text.
**Input:** "" (Empty String)
**Expected Output:**
- `entities`: Empty dictionary.

### 3. Edge Case: No Entities
**ID:** ENT-E2E-003
**Description:** Verify valid response when text has no named entities.
**Input:** "running jumping fast."
**Expected Output:**
- `entities`: Empty dictionary (assuming RegEx adapter doesn't match common words).

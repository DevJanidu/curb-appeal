#!/usr/bin/env python3
"""Validate a Curb Appeal project-state file against the schema.

Usage:
    python scripts/validate_state.py <path-to-project-state.json>
    python scripts/validate_state.py --self-test

The state file lives in a user's project at .curb-appeal/project-state.json,
never in this plugin repo. --self-test validates built-in valid and invalid
samples so CI can exercise the schema without a real project.
"""
import json
import sys

REQUIRED = {
    "schemaVersion", "classification", "stack", "projectType",
    "currentStage", "completedStages", "updatedAt",
}
CLASSIFICATION = {"new", "existing-website", "existing-unknown", "mixed"}
STACK = {
    "astro", "laravel-blade", "laravel-livewire", "laravel-inertia-react",
    "react-vite", "vue", "svelte", "static-html", "unknown",
}
PROJECT_TYPE = {"brochure", "booking", "erp"}
STAGES = {
    "DETECT", "INTAKE", "CLASSIFY", "RECOMMEND", "CONFIRM", "PLAN", "PREPARE",
    "BUILD", "CONTENT", "IMAGES", "INTEGRATIONS", "SEO", "RESPONSIVE",
    "TEST", "FIX", "HANDOFF", "COMPLETE",
}
FORBIDDEN = {"secret", "secrets", "password", "apiKey", "token", "credentials", "customerMessages"}


def validate(state):
    errs = []
    if not isinstance(state, dict):
        return ["state must be a JSON object"]
    missing = REQUIRED - state.keys()
    if missing:
        errs.append(f"missing required keys: {sorted(missing)}")
    if state.get("schemaVersion") != 1:
        errs.append("schemaVersion must be 1")
    for key, allowed in (
        ("classification", CLASSIFICATION), ("stack", STACK),
        ("projectType", PROJECT_TYPE), ("currentStage", STAGES),
    ):
        if key in state and state[key] not in allowed:
            errs.append(f"{key}={state[key]!r} not in {sorted(allowed)}")
    for stage in state.get("completedStages", []):
        if stage not in STAGES:
            errs.append(f"completedStages has unknown stage {stage!r}")
    leaked = FORBIDDEN & set(state.keys())
    if leaked:
        errs.append(f"state must not store {sorted(leaked)}")
    return errs


def self_test():
    valid = {
        "schemaVersion": 1, "classification": "new", "stack": "astro",
        "projectType": "brochure", "currentStage": "BUILD",
        "completedStages": ["DETECT", "INTAKE", "CLASSIFY"],
        "updatedAt": "2026-07-18T00:00:00Z",
    }
    assert validate(valid) == [], validate(valid)
    assert validate({"schemaVersion": 2}), "should reject bad schema"
    assert validate({**valid, "stack": "django"}), "should reject unknown stack"
    assert validate({**valid, "password": "x"}), "should reject secret key"
    print("OK: state schema self-test passed")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        self_test()
        sys.exit(0)
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    errs = validate(json.loads(open(sys.argv[1], encoding="utf-8").read()))
    if errs:
        print("\n".join(f"ERROR: {e}" for e in errs))
        sys.exit(1)
    print("OK: state file valid")

#!/usr/bin/env python3
"""Validate speckit metadata."""

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = {"name": str, "command": str, "description": str, "pypi_package": str, "cli_commands": list, "source": str}
OPTIONAL_FIELDS = {"repository": str, "author": str, "version": str, "tags": list, "slash_commands": list, "installed_path": str, "is_builtin": bool}

def validate_speckit(data: dict) -> list[str]:
    """Validate speckit metadata."""
    errors = []
    
    # Check required fields
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in data:
            errors.append(f"Missing required field: {field}")
        elif not isinstance(data[field], expected_type):
            errors.append(f"Field '{field}' must be {expected_type.__name__}")
    
    # Validate source
    if data.get("source") not in ["local", "builtin", "community"]:
        errors.append("Field 'source' must be 'local', 'builtin', or 'community'")
    
    # Validate description length
    desc = data.get("description", "")
    if len(desc) < 10 or len(desc) > 500:
        errors.append("Description must be 10-500 characters")
    
    # Validate tags
    tags = data.get("tags", [])
    if not isinstance(tags, list):
        errors.append("Tags must be a list")
    elif len(tags) > 10:
        errors.append("Maximum 10 tags allowed")
    
    return errors

def main():
    """Validate all JSON files in speckits/."""
    speckits_dir = Path(__file__).parent.parent / "speckits"
    
    all_valid = True
    for json_file in speckits_dir.glob("*.json"):
        print(f"\nValidating {json_file.name}...")
        
        try:
            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"  ❌ Invalid JSON: {e}")
            all_valid = False
            continue
        
        errors = validate_speckit(data)
        if errors:
            print("  ❌ Validation errors:")
            for error in errors:
                print(f"     - {error}")
            all_valid = False
        else:
            print("  ✅ Valid")
    
    sys.exit(0 if all_valid else 1)

if __name__ == "__main__":
    main()


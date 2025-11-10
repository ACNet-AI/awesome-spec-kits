# AGENTS.md

This file provides guidance for AI coding agents working on the Awesome Spec Kits project.

## Project Overview

**Awesome Spec Kits** is a curated registry of specification toolkits (speckits) that drive AI to generate content. The core philosophy is:

**Specs → AI → X (Anything)**

Where specifications serve as the single source of truth that drives AI to generate code, docs, protocols, configs, tests, and more.

## Core Concepts

### What is "Spec-Driven"?

A toolkit is "Spec-Driven" if it satisfies ALL four criteria:
1. **Has formal specifications** - Clear, structured spec format (not just config)
2. **Specs DRIVE** - Specs generate/validate, not just describe
3. **Spec → Output relationship** - Changing spec changes output
4. **Spec is authority** - Everything derives from specification

### SD-X Categories (Examples, Not Exhaustive)

The "X" in SD-X can be anything. Common examples include:

- **SD-Development** - Specs → AI → Code, tests, implementations
- **SD-Design** - Specs → AI → UI designs, architectures
- **SD-Protocol** - Specs → AI → Protocol definitions, standards
- **SD-Documentation** - Specs → AI → Docs, guides, tutorials
- **SD-API** - API specs → AI → Client SDKs, server implementations
- **SD-Config** - Config specs → AI → System configurations
- **SD-Test** - Test specs → AI → Test cases, scenarios

**Note**: This is not a fixed taxonomy. New SD-X categories can emerge as the community discovers new applications of spec-driven AI generation.

## Project Structure

```
awesome-spec-kits/
├── README.md              # User-facing documentation (keep concise)
├── CONTRIBUTING.md        # Contributor guide (detailed, ~500 lines)
├── AGENTS.md             # This file - guidance for AI agents
├── speckits.json         # Main registry file (JSON format)
├── examples/
│   └── example-speckit.json  # Metadata template
├── scripts/
│   ├── validate_speckit.py   # Validates Python projects via pyproject.toml
│   └── add_to_registry.py    # Adds entries to speckits.json
└── .github/
    ├── workflows/
    │   └── auto-register.yml  # Automated registration via Issues
    └── ISSUE_TEMPLATE/
        └── register-speckit.yml  # Registration form

```

## Key Design Decisions

### 1. Framework Agnostic
- Do NOT require MetaSpec or any specific framework
- Welcome speckits built from scratch in any language
- MetaSpec is ONE option, not mandatory

### 2. Language Agnostic
- Automated validation currently supports Python (pyproject.toml)
- Manual registration supports ALL languages (Node.js, Go, Rust, etc.)
- Never bias toward one language or framework

### 3. Open to Implementations
- From-scratch implementations ✅
- Any framework ✅
- Any language ✅
- Adapted existing tools ✅

### 4. AI-Centric Philosophy
- Always emphasize "Specs → AI → Content"
- AI is the generator/automaton in spec-driven systems
- Specs provide BOTH input AND validation for AI

## Documentation Guidelines

### README.md
- **Purpose**: Quick overview for users
- **Target**: ~150 lines
- **Keep**: Concise, high-level, welcoming
- **Avoid**: Implementation details, long explanations

### CONTRIBUTING.md
- **Purpose**: Detailed guide for contributors
- **Target**: ~500 lines
- **Keep**: Comprehensive validation/review process
- **Include**: "What Makes a Speckit Spec-Driven?" section

### Content Consistency
- SD-X example lists must be IDENTICAL in README and CONTRIBUTING
- Always use the same 7 examples: Development, Design, Protocol, Documentation, API, Config, Test
- Make clear these are EXAMPLES, not a fixed taxonomy
- Emphasize "X can be anything" - the list is illustrative, not exhaustive
- Resources sections should reference same projects

## Development Workflow

### File Editing
When editing documentation:
1. Check BOTH README.md and CONTRIBUTING.md for related content
2. Keep SD-X examples synchronized
3. Maintain consistent terminology
4. No Chinese text in any files (English only)

### Python Scripts
Located in `scripts/`:
- **validate_speckit.py**: Validates GitHub repos with pyproject.toml
- **add_to_registry.py**: Adds validated speckits to speckits.json

To test validation locally:
```bash
export ISSUE_BODY="repository_url"
python scripts/validate_speckit.py
```

### Registry Format (speckits.json)
Required fields for each speckit:
```json
{
  "name": "package-name",
  "version": "1.0.0",
  "description": "Clear, searchable description",
  "repository": "https://github.com/user/repo",
  "pypi_package": "package-name",
  "cli_command": "command-name",
  "license": "MIT",
  "tags": ["tag1", "tag2"],
  "created_at": "2025-11-09",
  "updated_at": "2025-11-09",
  "status": "active"
}
```

## Testing & Validation

### Before Committing
1. Check for Chinese text: `grep -r "[\u4e00-\u9fff]" README.md CONTRIBUTING.md`
2. Verify SD-X lists are identical: `grep "SD-Development" README.md CONTRIBUTING.md`
3. Check no duplicate Resources sections: `grep -n "## .*Resources" CONTRIBUTING.md`
4. Run linter on Python scripts: `ruff check scripts/` (if ruff available)

### Validation Rules
When evaluating if a toolkit is "Spec-Driven":
- ❌ Config file readers - Just parse config, don't generate
- ❌ Template engines - Templates without formal specs
- ❌ Manual code generators - Human writes code, not spec-driven
- ✅ OpenAPI generators - API spec → Client/Server code
- ✅ Protocol Buffers - Protocol spec → Multiple language implementations
- ✅ Schema validators - Schema spec → Validation logic

## Git Workflow

### Commit Messages
Follow conventional commits:
- `docs:` - Documentation changes
- `feat:` - New features
- `fix:` - Bug fixes
- `refactor:` - Code restructuring

Good examples:
```
docs: unify SD-X examples across README and CONTRIBUTING
feat: add support for Go projects validation
fix: correct MetaSpec repository URL
```

Avoid:
- Mentioning language/translation changes
- Vague messages like "update docs"
- Mixing multiple unrelated changes

### PR Guidelines
1. Ensure all SD-X lists are synchronized
2. No Chinese text in any documentation
3. Update both README and CONTRIBUTING if concept changes
4. Test validation scripts if modified
5. Keep changes focused and atomic

## Important Constraints

### Never Do
1. ❌ Add Chinese text to documentation
2. ❌ Make MetaSpec mandatory
3. ❌ Require specific frameworks or languages
4. ❌ Create conflicting SD-X example lists
5. ❌ Duplicate Resources sections in CONTRIBUTING.md
6. ❌ Change core "Spec-Driven" definition without discussion

### Always Do
1. ✅ Maintain "Specs → AI → Content" messaging
2. ✅ Keep documentation accessible and welcoming
3. ✅ Test scripts before committing changes
4. ✅ Synchronize SD-X examples across files
5. ✅ Reference key projects: GitHub Spec-Kit, MetaSpec
6. ✅ Use 4-question self-test for spec-driven validation

## Reference Projects

When discussing or evaluating speckits, reference these exemplars:
- **GitHub Spec-Kit** (46.6k+ stars) - Official Spec-Driven Development toolkit
- **MetaSpec** - Meta-specification framework for generating speckits
- Use these as examples of what spec-driven means in practice

## Questions or Uncertainty?

If unsure about:
- **"Is this spec-driven?"** - Apply the 4-question test
- **"Should this be in README or CONTRIBUTING?"** - README = user-facing, CONTRIBUTING = contributor details
- **"What about X language?"** - All languages welcome, use manual registration
- **"Framework requirements?"** - None, completely optional

Default to being inclusive and welcoming. When in doubt, err on the side of accepting contributions.

